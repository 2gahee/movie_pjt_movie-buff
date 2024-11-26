cinema_time = {'군자': 1351, '동대문': 1603, '마곡': 3132, '성수': 1942, '센트럴': 806, '신촌': 2231, '이수': 1353, '코엑스': 1199, '홍대': 2010, '강남': 741, '더 부티크 목동현대백화점': 2416, '목동': 2547, '상암월드컵경기장': 1898, '상봉': 1440, '송파파크하비오': 2367, '화곡': 2627}
goods_list = [{'goods_name': '모아나 2 오리지널 티켓', 'goods_info': [{'region': '서울 (2)', 'branch': '군자', 'stock_status': '준비중'}, {'region': '서울 (2)', 'branch': '동대문', 'stock_status': '보유'}]},
              {'goods_name': '에드워드 호퍼 오리지널 슬라이드', 'goods_info': [{'region': '서울 (7)', 'branch': '마곡', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '성수', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '센트럴', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '신촌', 'stock_status': '보유'}, {'region': '서울 (7)', 'branch': '이수', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '코엑스', 'stock_status': '준비중'}, {'region': '서울 (7)', 'branch': '홍대', 'stock_status': '보유'}]},
              {'goods_name': '컨택트 오리지널 티켓', 'goods_info': [{'region': '서울 (15)', 'branch': '강남', 'stock_status': '소량보유'}, {'region': '서울 (15)', 'branch': '더 부티크 목동현대백화점', 'stock_status': '보유'}]},
              {'goods_name': '글레디에이터2 MX4D 포스터', 'goods_info': [{'region': '서울 (1)', 'branch': '코엑스', 'stock_status': '보유'}]},
              {'goods_name': '글레디에이터2 돌비 포스터','goods_info': [{'region': '서울 (4)', 'branch': '목동', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '상암월드컵경기장', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '성수', 'stock_status': '소량보유'}, {'region': '서울 (4)', 'branch': '코엑스', 'stock_status': '보유'}]},
              {'goods_name': '톰보이 드로잉 카드', 'goods_info': [{'region': '서울 (16)', 'branch': '강남', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '군자', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '더 부티크 목동현대백화점', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '동대문', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '마곡', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '목동', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '상봉', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '상암월드컵경기장', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '송파파크하비오', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '신촌', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '이수', 'stock_status': '보유'}, {'region': '서울 (16)', 'branch': '코엑스', 'stock_status': '소량보유'}]}, 
              {'goods_name': '청설 오리지널티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '동대문', 'stock_status': '소량보유'}, {'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}, {'region': '서울 (18)', 'branch': '화곡', 'stock_status': '소량보유'}]},
              {'goods_name': '베놈: 라스트 댄스 오리지널 티켓', 'goods_info': [{'region': '서울 (18)', 'branch': '센트럴', 'stock_status': '소량보유'}]}]

for goods in goods_list:
    name = goods['goods_name']
    info = goods['goods_info']
    for cinema in info:
        dist = cinema_time[cinema['branch']]
        weight = 5 if cinema['stock_status'] == '소량보유' else weight = 3
        