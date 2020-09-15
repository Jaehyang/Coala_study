##조건에 따른 데이터 수집하기 -> 네이버 영화 중 평점이 8.5 이상이며, 장르가 액션인 영화 데이터 수집(제목, 평점, 장르, 감독, 배우)

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

movies = html.select("dl.lst_dsc")

for m in movies:
    title = m.select_one(" dt.tit > a").text
    score = m.select_one("div.star_t1 a span.num").text
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")  # 꺼내와서 다시 a를 선택할 필요 없이 a를 그대로 쓸 수 있음. 숫자를 1부터 셈.
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    if float(score) < 8.5:
        continue                #for문에 따라 데이터 수집하다가, 밑에를 출력하지 않고 다음단계의 반복문으로 지나가겠다는 뜻

    genre_all = m.select_one("dl.info_txt1 dd:nth-of-type(1) span.link_txt")
    if "액션" not in genre_all.text:             #genre_all은 태그데이터 안에서 선택했으므로 .text 붙여줘야함.
        continue

    print("제목:", title)
    print("평점:", score)

    print("장르:")
    for g in genre:
        print(g.text)

    print("감독:")
    for d in director:
        print(d.text)

    print("배우:")
    for a in actor:
        print(a.text)

    print("=" * 50)