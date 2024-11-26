# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework import status
# from django.shortcuts import get_object_or_404, get_list_or_404
# from django.shortcuts import render
# from .models import UserMovie, MoviePicks
# from .serializers import MoviePicksSerializer
import requests
# from rest_framework.exceptions import NotFound
# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from rest_framework.permissions import AllowAny

from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from django.http import JsonResponse

# def megaboxEvents(reqeust):
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
                    if stock_status == "보유" or "소량보유":
                    # 정보 저장
                        goods_stock_info.append({
                            "region": region_name,
                            "branch": branch_name,
                            "stock_status": stock_status
                        })
            if len(goods_stock_info):
                goods_list.append({"goods_name": goodsBtn["data-nm"], "goods_info": goods_stock_info})
print(goods_list)
driver.quit()
    # return JsonResponse(goods_list, safe=False)

