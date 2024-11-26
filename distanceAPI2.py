import requests
import json

goods_list = [
    {'goods_name': '베놈: 라스트 댄스 오리지널 티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}]}
]
KAKAO_API_KEY = '5244812f340e17fb3d1929b739bf8ff8'
cd_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
route_url = "https://apis-navi.kakaomobility.com/v1/directions/multi"  # 다중 목적지 API
origin = {'lng': 127.012207, 'lat': 37.508130}  # 사용자의 위치 (임시)
map_dict = dict()
destinations = []  # 다중 목적지 리스트

# 영화관 위치 검색 및 목적지 좌표 추출
for goods in goods_list:
    name = goods['goods_name']
    for info in goods['goods_info']:
        branch = info['branch']
        branch_string = '메가박스' + branch
        headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
        cd_params = {"query": branch_string}
        response = requests.get(cd_url, headers=headers, params=cd_params)

        if response.status_code == 200:
            data = response.json()
            if data["documents"]:
                coords = data["documents"][0]
                destination = {'x': float(coords['x']), 'y': float(coords['y'])}
                destinations.append(destination)
                print(f"{branch} 좌표: {destination}")
            else:
                print(f"No coordinates found for branch: {branch_string}")
                continue
        else:
            print(f"Error fetching coordinates for {branch_string}: {response.status_code}, {response.text}")

# 다중 목적지 길찾기 요청
if destinations:
    route_params = {
        "origin": f"{origin['lng']},{origin['lat']}",
        "destinations": destinations,
        "priority": "FAST"  # 경로 우선순위 설정
    }

    # POST 요청 보내기
    response = requests.post(route_url, headers=headers, data=json.dumps(route_params))

    if response.status_code == 200:
        data = response.json()
        for idx, route in enumerate(data["routes"]):
            branch_name = goods_list[0]['goods_info'][idx]['branch']
            duration = route['summary']['duration']  # 소요 시간
            map_dict[branch_name] = duration
            print(f"{branch_name}까지의 소요 시간: {duration}초")
    else:
        print(f"API 요청 오류: {response.status_code}, {response.text}")

print(map_dict)
