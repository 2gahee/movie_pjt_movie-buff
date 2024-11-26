import requests

goods_list = [{'goods_name': '모아나 2 오리지널 티켓', 'goods_info': [{'region': '서울 (2)', 'branch': '군자', 'stock_status': '준비중'}, {'region': '서울 (2)', 'branch': '동대문', 'stock_status': '보유'}]},
              {'goods_name': '에드워드 호퍼 오리지널 슬라이드', 'goods_info': [{'region': '서울 (7)', 'branch': '마곡', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '성수', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '센트럴', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '신촌', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '이수', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '코엑스', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '홍대', 'stock_status': '보유'}]},
              {'goods_name': '컨택트 오리지널 티켓', 'goods_info': [{'region': '서울 (15)', 'branch': '강남', 'stock_status': '소량보유'}, {'region': '서울 (15)', 'branch': '더 부티크 목동현대백화점', 'stock_status': '보유'}]},
              {'goods_name': '글레디에이터2 MX4D 포스터', 'goods_info': [{'region': '서울 (1)', 'branch': '코엑스', 'stock_status': '보유'}]},
              {'goods_name': '글레디에이터2 돌비 포스터','goods_info': [{'region': '서울 (4)', 'branch': '목동', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '상암월드컵경기장', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '성수', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '코엑스', 'stock_status': '보유'}]},
              {'goods_name': '톰보이 드로잉 카드', 'goods_info': [{'region': '서울 (16)', 'branch': '강남', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '군자', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '더 부티크 목동현대백화점', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '동대문', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '마곡', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '목동', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '상봉', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '상암월드컵경기장', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '송파파크하비오', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '신촌', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '이수', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '코엑스', 'stock_status': '소량보유'}]}, 
              {'goods_name': '청설 오리지널티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '동대문', 'stock_status': '소량보유'}, {'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}, {'region': '서울 (18)', 'branch': '화곡', 'stock_status': '소량보유'}]},
              {'goods_name': '베놈: 라스트 댄스 오리지널 티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}]}]
KAKAO_API_KEY = '5244812f340e17fb3d1929b739bf8ff8'
cd_url = "https://dapi.kakao.com/v2/local/search/keyword.json"
route_url = "https://apis-navi.kakaomobility.com/v1/directions"
origin = {'lng': 127.012207, 'lat': 37.508130} # temp
map_dict = dict()
for goods in goods_list:
    name = goods['goods_name']
    for info in goods['goods_info']:
        branch = info['branch']
        if branch not in map_dict:
            branch_string = '메가박스' + branch
            headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
            cd_params = {"query": branch_string}
            response = requests.get(cd_url, headers=headers, params=cd_params)
            if response.status_code == 200:
                data = response.json()
                if data["documents"]:
                    coords = data["documents"][0]
                    print(branch, coords)
                else:
                    print(f"No coordinates found for branch: {branch_string}")
                    continue
            route_params = {
                "origin": f"{origin['lng']},{origin['lat']}",
                "destination": f"{float(coords['x'])},{float(coords['y'])}",
                "priority": "RECOMMEND", 
            }

            response = requests.get(route_url, headers=headers, params=route_params)
            if response.status_code == 200:
                data = response.json()
                # print(data)
                time =  data["routes"][0]["summary"]["duration"]
                map_dict.update({branch : time})
            else:
                print(f"Error fetching coordinates for {branch_string}: {response.status_code}, {response.text}")
print(map_dict)                

