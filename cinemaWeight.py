import json
from pprint import pprint

cinema_time = {'군자': 1663, '동대문': 1604, '마곡': 2491, '성수': 1560, '센트럴': 717, '신촌': 2453, '이수': 1271, '코엑스': 645, '홍대': 2268, '강남': 559, '더 부티크 목동현대백화점': 2219, '목동': 2171, '상암월드컵경기장': 1842, '상봉': 1595, '송파파크하비오': 1755, '화곡': 2363}
goods_list = [{'goods_name': '모아나 2 오리지널 티켓', 'goods_info': [{'region': '서울 (2)', 'branch': '군자', 'stock_status': '준비중'}, {'region': '서울 (2)', 'branch': '동대문', 'stock_status': '보유'}]},
              {'goods_name': '에드워드 호퍼 오리지널 슬라이드', 'goods_info': [{'region': '서울 (7)', 'branch': '마곡', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '성수', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '센트럴', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '신촌', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '이수', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '코엑스', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '홍대', 'stock_status': '보유'}]},
              {'goods_name': '컨택트 오리지널 티켓', 'goods_info': [{'region': '서울 (15)', 'branch': '강남', 'stock_status': '소량보유'}, {'region': '서울 (15)', 'branch': '더 부티크 목동현대백화점', 'stock_status': '보유'}]},
              {'goods_name': '글레디에이터2 MX4D 포스터', 'goods_info': [{'region': '서울 (1)', 'branch': '코엑스', 'stock_status': '보유'}]},
              {'goods_name': '글레디에이터2 돌비 포스터','goods_info': [{'region': '서울 (4)', 'branch': '목동', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '상암월드컵경기장', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '성수', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '코엑스', 'stock_status': '보유'}]},
              {'goods_name': '톰보이 드로잉 카드', 'goods_info': [{'region': '서울 (16)', 'branch': '강남', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '군자', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '더 부티크 목동현대백화점', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '동대문', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '마곡', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '목동', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '상봉', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '상암월드컵경기장', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '송파파크하비오', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '신촌', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '이수', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '코엑스', 'stock_status': '소량보유'}]}, 
              {'goods_name': '청설 오리지널티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '동대문', 'stock_status': '소량보유'}, {'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}, {'region': '서울 (18)', 'branch': '화곡', 'stock_status': '소량보유'}]},
              {'goods_name': '베놈: 라스트 댄스 오리지널 티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}]}]
weights = {
    "보유": 3,
    "소량보유": 4,
    "준비중": 5}
final_dict = {}
for goods in goods_list:
    name = goods['goods_name']
    priority_dict = {cinema: {"time": time, "score": 0, "stock_status": "없음"} for cinema, time in cinema_time.items()}
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

    # print(goods['goods_name'])
    final_dict[name] = {
        cinema: {
            'score': info['score'],
            'time': info['time'],
            'stock': info['stock_status']
        }
        for cinema, info in sorted_cinemas[:5]
    }
    sorted_final_dict = {
    goods_name: cinemas
    for goods_name, cinemas in sorted(
        final_dict.items(),
        key=lambda item: min(cinema["score"] for cinema in item[1].values())
    )
    }
        # print(f"{cinema}: 총 점수 {info['score']}, 소요시간 {info['time']}초, 재고 {info['stock_status']}")
print(sorted_final_dict)