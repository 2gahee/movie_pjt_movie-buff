from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
# from .models import UserMovie, MoviePicks
# from .serializers import MoviePicksSerializer
import requests, json, re
from rest_framework.exceptions import NotFound
from django.conf import settings
# from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny

from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def megaboxEvents(reqeust):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 브라우저를 숨긴 상태로 실행 (옵션)

    # ChromeDriver 초기화
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),  # ChromeDriver 설치 및 경로 지정
        options=chrome_options                            # 옵션 전달
    )

    driver.get("https://www.google.com")
    User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    url = "https://www.megabox.co.kr/event/megabox"
    driver.get(url)

    # 페이지 로드 후 HTML 소스 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 이벤트 리스트 가져오기
    a_tags = soup.select("#event-list-wrap > div > div > ul > li > a")    
    event_no_list = [tag['data-no'] for tag in a_tags if 'data-no' in tag.attrs]
    goods_list = []
    goods_url = "https://megabox.co.kr/on/oh/ohe/Event/selectGoodsStockPrco.do"
    for num in event_no_list:
        event_url = f"https://www.megabox.co.kr/event/detail?eventNo={num}"
        headers = {
        "User-agent" : User_Agent
        }
        # URL에 HTTP 요청 보내기
        response = requests.get(event_url, headers=headers)
        if response.status_code == 200:
            html = response.text
            event_soup = BeautifulSoup(html, 'html.parser')
            h2_content = event_soup.select_one("#contents > div > h2").text
            result = re.search(r"<(.*?)>", h2_content)
            if result:
                movie_title = result.group(1)
            goodsBtn = event_soup.select_one("#btnSelectGoodsStock")
            if goodsBtn:
                payload = {
                    "goodsNo": goodsBtn["data-pn"]
                }   
                goods_headers = {
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Referer": event_url,
                    "User-agent" : User_Agent
                }
                # POST 요청
                goods_response = requests.post(goods_url, headers=headers, data=payload)
                # 응답 HTML 파싱
                soup = BeautifulSoup(goods_response.text, "html.parser")
                # 결과 저장할 리스트
                goods_stock_info = []
                # 지점 정보 추출
                areas = soup.find_all("li", class_="area-cont on")  # 지역별 구분
                for area in areas:
                    region_name = area.find("button").text.strip()  # 지역 이름
                    branches = area.find_all("li", class_="brch")  # 지점 목록
                    for branch in branches:
                        branch_name = branch.find("a").text.strip()  # 지점 이름
                        stock_status = branch.find("span").text.strip()  # 보유 상태
                        if stock_status != "소진":
                        # 정보 저장
                            goods_stock_info.append({
                                "region": region_name,
                                "branch": branch_name,
                                "stock_status": stock_status
                            })
                if len(goods_stock_info):
                    goods_list.append({"goods_name": goodsBtn["data-nm"], "movie_title": movie_title, "goods_info": goods_stock_info})
    driver.quit()
    return goods_list

@csrf_exempt
def goodsAPI(request):
    KAKAO_API_KEY = settings.KAKAO_API_KEY
    cd_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
    route_url = "https://apis-navi.kakaomobility.com/v1/directions"
    if request.method == 'POST':
        try:
            # Parse the incoming request data
            data = json.loads(request.body)
            
            # Extract origin coordinates from request
            origin_latitude = data.get('latitude', 37.5095296)  # Default to your initial coordinates
            origin_longitude = data.get('longitude', 127.0317056)
            
            map_dict = dict()
            goods_list = megaboxEvents(request)
            
            for goods in goods_list:
                # name = goods['goods_name']
                # title = goods['goods_title']
                for info in goods['goods_info']:
                    branch = info['branch']
                    if branch not in map_dict:
                        branch_string = '메가박스' + branch
                        headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
                        cd_params = {"query": branch_string}
                        
                        response = requests.get(cd_url, headers=headers, params=cd_params)
                        if response.status_code == 200:
                            location_data = response.json()
                            if location_data["documents"]:
                                coords = location_data["documents"][0]
                                
                                # Debugging print statements
                                print(f"Origin Coordinates: {origin_longitude}, {origin_latitude}")
                                print(f"Destination Coordinates: {coords['x']}, {coords['y']}")
                                
                                route_params = {
                                    "origin": f"{origin_longitude},{origin_latitude}",  # Note the order: longitude,latitude
                                    "destination": f"{coords['x']},{coords['y']}",
                                    "priority": "RECOMMEND", 
                                }

                                route_headers = {
                                    "Authorization": f"KakaoAK {KAKAO_API_KEY}",
                                    "Content-Type": "application/json"
                                }
                                
                                # Use requests.get with proper headers and params
                                response = requests.get(
                                    route_url, 
                                    headers=route_headers, 
                                    params=route_params
                                )
                                
                                if response.status_code == 200:
                                    route_data = response.json()
                                    time = route_data["routes"][0]["summary"]["duration"]
                                    map_dict.update({branch: time})
                                else:
                                    print(f"Route API Error: {response.status_code}")
                                    print(f"Response Text: {response.text}")
                            else:
                                print(f"No coordinates found for branch: {branch_string}")
                                continue
                        else:
                            print(f"Kakao Local API Error: {response.status_code}")
                            print(f"Response Text: {response.text}")
        
        except Exception as e:
            print(f"Full Error Details: {e}")
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        weights = {
        "보유": 3,
        "소량보유": 4,
        "준비중": 5}
        final_dict = {}
        for goods in goods_list:
            name = goods['goods_name']
            title = goods['movie_title']
            print(title)
            priority_dict = {cinema: {"time": time, "score": 0, "stock_status": "없음"} for cinema, time in map_dict.items()}
            for cinema in priority_dict.keys():
                # 현재 극장에 해당 굿즈가 있는지 확인
                goods_info = next((item for item in goods["goods_info"] if item["branch"] == cinema), None)
                
                if goods_info:
                    # 굿즈가 있는 경우 가중치 적용
                    status = goods_info["stock_status"]
                    weight = weights.get(status, 5)
                    priority_dict[cinema]["stock_status"] = status
                else:
                    # 굿즈가 없는 경우 기본 가중치 적용
                    weight = 5

                # 점수 계산: 소요 시간 * 가중치
                priority_dict[cinema]["score"] += priority_dict[cinema]["time"] * weight

            sorted_cinemas = sorted(priority_dict.items(), key=lambda x: x[1]["score"])

            final_dict[name] = {
                "title": title,
                "cinemas":{
                cinema: {
                    'score': info['score'],
                    'time': info['time'],
                    'stock': info['stock_status']
                }
                for cinema, info in sorted_cinemas[:5]
            }}
            sorted_final_dict = [{
                goods_name: cinemas
                for goods_name, cinemas in sorted(
                    final_dict.items(),
                    key=lambda item: min(cinema['score'] for cinema in item[1]['cinemas'].values())  # 'cinemas'에서 'score'를 찾아 정렬
                )
            }]
    return JsonResponse(sorted_final_dict, safe=False)

