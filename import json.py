import json

# 원본 JSON 데이터
data = [
    {
        "id": 670,
        "title": "올드보이",
        "poster_path": "/xpa9ybm6tYGna5LseqSXvKpSSJn.jpg"
    },
    {
        "id": 705996,
        "title": "헤어질 결심",
        "poster_path": "/rXEJ28XDQsogIGqwVEgwM2oDdpl.jpg"
    },
    {
        "id": 475557,
        "title": "조커",
        "poster_path": "/wrCwH6WOvXQvVuqcKNUrLDCDxdw.jpg"
    },
    {
        "id": 155,
        "title": "다크 나이트",
        "poster_path": "/f6dNinWX8rBM79JXKcShkfSh2oA.jpg"
    },
    {
        "id": 278,
        "title": "쇼생크 탈출",
        "poster_path": "/oAt6OtpwYCdJI76AVtVKW1eorYx.jpg"
    },
    {
        "id": 807,
        "title": "세븐",
        "poster_path": "/izzk8dbmrLowcoGbFaebqJvzyXg.jpg"
    },
    {
        "id": 496243,
        "title": "기생충",
        "poster_path": "/eRM0PykovgtK4lin1D4BUql8TBa.jpg"
    },
    {
        "id": 27205,
        "title": "인셉션",
        "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg"
    },
    {
        "id": 299534,
        "title": "어벤져스: 엔드게임",
        "poster_path": "/z7ilT5rNN9kDo8JZmgyhM6ej2xv.jpg"
    },
    {
        "id": 354912,
        "title": "코코",
        "poster_path": "/pQu93NuwR90AaCULzglVD5Ge4Ml.jpg"
    },
    {
        "id": 872585,
        "title": "오펜하이머",
        "poster_path": "/jpD6z9fgNe7OqsHoDeAWQWoULde.jpg"
    },
    {
        "id": 20453,
        "title": "세 얼간이",
        "poster_path": "/9zQdFVyDoXqFmGYXp4obna6FEMh.jpg"
    },
    {
        "id": 2062,
        "title": "라따뚜이",
        "poster_path": "/zFah4LNeWw68y7RRGi20CQlGByY.jpg"
    },
    {
        "id": 18438,
        "title": "김씨 표류기",
        "poster_path": "/eccgbNOv2FhfWgQv4Q5iS4haGVQ.jpg"
    },
    {
        "id": 58,
        "title": "캐리비안의 해적: 망자의 함",
        "poster_path": "/6tD4oT7C01aZLVfoZDz5VFVbJCi.jpg"
    },
    {
        "id": 489999,
        "title": "서치",
        "poster_path": "/7TgR6Ipwnvu8AjxAm2gPpaqediA.jpg"
    },
    {
        "id": 1124,
        "title": "프레스티지",
        "poster_path": "/rwEc7SgXu7b5Yo8Co4CvSinF91v.jpg"
    },
    {
        "id": 9502,
        "title": "쿵푸팬더",
        "poster_path": "/c3Dzd3A3QE0LkKb5HMOHTzs2Fyg.jpg"
    },
    {
        "id": 122906,
        "title": "어바웃 타임",
        "poster_path": "/cLfuuK1Y5FjX1xXDrrEa9ppnKuy.jpg"
    },
    {
        "id": 37165,
        "title": "트루먼 쇼",
        "poster_path": "/AsUv4pFf1UQuOLKf7nYUXgmgCNf.jpg"
    },
    {
        "id": 89501,
        "title": "범죄와의 전쟁: 나쁜놈들 전성시대",
        "poster_path": "/4tJYmvn7VgDsrAYHgB3qebVWTut.jpg"
    },
    {
        "id": 133200,
        "title": "광해, 왕이 된 남자",
        "poster_path": "/6Pg5AwsJUqeGanGOWcaljQXGe5g.jpg"
    },
    {
        "id": 360551,
        "title": "검은 사제들",
        "poster_path": "/3zYZ5hZUNHwgObdqbDYlS8l24FE.jpg"
    },
    {
        "id": 660360,
        "title": "노량: 죽음의 바다",
        "poster_path": "/WqgLrAbPnEfgn7WP7J2IvL1Z9V.jpg"
    },
    {
        "id": 603692,
        "title": "존 윅 4",
        "poster_path": "/h3LsdSBzhRnBebz4BTpAhh63PD3.jpg"
    },
    {
        "id": 4935,
        "title": "하울의 움직이는 성",
        "poster_path": "/3sVFlmzBCZpwlsosKHxyK4d9oDw.jpg"
    },
    {
        "id": 9806,
        "title": "인크레더블",
        "poster_path": "/11Byg6rHkKIvSehlW3R4pcUj8J.jpg"
    },
    {
        "id": 419430,
        "title": "겟 아웃",
        "poster_path": "/paPvmoLgUUQojsSdAZmf7dwkKGT.jpg"
    },
    {
        "id": 82695,
        "title": "레미제라블",
        "poster_path": "/hSjWT9LsyNJ9H3d1Tn9Hx02hnQD.jpg"
    },
    {
        "id": 271110,
        "title": "캡틴 아메리카: 시빌 워",
        "poster_path": "/vaMRzME3Dt73robEjOtDw4SPJGA.jpg"
    },
    {
        "id": 100402,
        "title": "캡틴 아메리카: 윈터 솔져",
        "poster_path": "/qBuAglXtjBW9JBpIJ3W40nY58Am.jpg"
    },
    {
        "id": 284053,
        "title": "토르: 라그나로크",
        "poster_path": "/jwswXltzpGaKZCtz1CiDjXHQYAs.jpg"
    },
    {
        "id": 177677,
        "title": "미션 임파서블: 로그네이션",
        "poster_path": "/wqHiuRRkjJ8vyjKOm0IjHhyzISy.jpg"
    },
    {
        "id": 76341,
        "title": "매드맥스: 분노의 도로",
        "poster_path": "/cadVm6gKYYukmPysHGCwrawUHHa.jpg"
    },
    {
        "id": 1244492,
        "title": "룩백",
        "poster_path": "/ehl2Du38qbg9M2cqfoVPUKgVDTy.jpg"
    },
    {
        "id": 10528,
        "title": "셜록 홈즈",
        "poster_path": "/57lDlyrA7tWDyscroixKSJRerFU.jpg"
    },
    {
        "id": 680,
        "title": "펄프 픽션",
        "poster_path": "/6lXRHGoEbnnBUKsuqpL9JxD4DzT.jpg"
    },
    {
        "id": 13,
        "title": "포레스트 검프",
        "poster_path": "/xdJxoq0dtkchOkUz5UVKuxn7a2V.jpg"
    },
    {
        "id": 324857,
        "title": "스파이더맨: 뉴 유니버스",
        "poster_path": "/d9V6Q9vpVpmaca7vwSUbCajtDb3.jpg"
    },
    {
        "id": 128,
        "title": "모노노케 히메",
        "poster_path": "/gEVSN7rzQsypG4YfYObsPmMtYpP.jpg"
    },
    {
        "id": 244786,
        "title": "위플래쉬",
        "poster_path": "/sNoZ3DAjOtCtpGvaEubMELDNtaS.jpg"
    },
    {
        "id": 77,
        "title": "메멘토",
        "poster_path": "/vqxdADPdy0ZVJr8dMB3mh6C5Vsv.jpg"
    },
    {
        "id": 603,
        "title": "매트릭스",
        "poster_path": "/yI9r0iz2XvlevxUzxvdoQmv3yce.jpg"
    },
    {
        "id": 447365,
        "title": "가디언즈 오브 갤럭시 Volume 3",
        "poster_path": "/zK0FTsXvkWVS3yubZkbenbAFcnY.jpg"
    },
    {
        "id": 361743,
        "title": "탑건: 매버릭",
        "poster_path": "/jeqXUwNilvNqNXqAHsdwm5pEfae.jpg"
    },
    {
        "id": 269149,
        "title": "주토피아",
        "poster_path": "/fZcab1yiKXsjx3S8D4KRHZsnMGC.jpg"
    },
    {
        "id": 346646,
        "title": "베테랑",
        "poster_path": "/idCfJB8mTZfy49Yb6lX3FfEzvV7.jpg"
    },
    {
        "id": 40171,
        "title": "전우치",
        "poster_path": "/48QvXMsVeNlEEL55jUixVnX09KS.jpg"
    },
    {
        "id": 124157,
        "title": "도둑들",
        "poster_path": "/ujIHEzt2EEboVzjQoWZBMYdAt1v.jpg"
    },
    {
        "id": 12445,
        "title": "해리 포터와 죽음의 성물 2",
        "poster_path": "/ehUeFvQeo8Vr2aDIKLsLbC8okcw.jpg"
    }
]

# 변환된 데이터를 담을 리스트
converted_data = []

# 데이터를 변환
for idx, movie in enumerate(data, 1):
    converted_data.append({
        "model": "movies.moviepicks", 
        "pk": idx,  # pk는 1부터 시작
        "fields": {
            "movie_id": movie["id"], 
            "title": movie["title"], 
            "poster_path": movie["poster_path"]
        }
    })

# 변환된 데이터를 JSON 형식으로 출력
converted_json = json.dumps(converted_data, ensure_ascii=False, indent=4)

# 결과 출력
print(converted_json)
