from bs4 import BeautifulSoup
import requests

# API URL
url = "https://megabox.co.kr/on/oh/ohe/Event/selectGoodsStockPrco.do"

# 요청에 사용할 goodsNo
payload = {
    "goodsNo": "FG000251"  # 굿즈 ID 예시
}

# 요청 헤더 설정
headers = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "https://megabox.co.kr/event/detail?eventNo=16544",  # 참조 URL
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
}

# POST 요청
response = requests.post(url, headers=headers, data=payload)

# 응답 HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 결과 저장할 리스트
goods_stock_info = []

# 지점 정보 추출
areas = soup.find_all("li", class_="area-cont on")  # 지역별 구분

for area in areas:
    region_name = area.find("button").text.strip()  # 지역 이름
    branches = area.find_all("li", class_="brch")  # 지점 목록

    for branch in branches:
        branch_name = branch.find("a").text.strip()  # 지점 이름
        stock_status = branch.find("span", class_="act").text.strip()  # 보유 상태

        # 정보 저장
        goods_stock_info.append({
            "region": region_name,
            "branch": branch_name,
            "stock_status": stock_status
        })

# 결과 출력
for info in goods_stock_info:
    print(f"지역: {info['region']}, 지점: {info['branch']}, 상태: {info['stock_status']}")
