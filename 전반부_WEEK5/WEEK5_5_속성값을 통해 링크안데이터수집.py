### 속성 값을 통해 링크 안 데이터 수집하기

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one(" dt.tit > a")
    url = title.attrs["href"]           #attribute 속성
    print("="*50)
    print(title.text)

    # 링크 안 데이터 수집하기
    each_raw = requests.get("https://movie.naver.com"+url, headers={"User-Agent" : "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 컨테이너 div.score_result > ul > li
    # 평점 div.star_score em
    # 리뷰 div.score_reple p

    reviews = each_html.select("div.score_result > ul > li")
    for r in reviews:
        stars = r.select_one("div.star_score em").text.strip()     #select_one으로 했으니 .text를 통해 문자 데이터로 바꿔주기
        reple = r.select_one("div.score_reple p").text.strip()

        print(stars, reple)               #왜 리뷰와 평점이 다섯개씩밖에 안나오는지

    #포스터 div.mv_info_area div.poster img

    poster =  each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    print(poster_src)

    # print("https://movie.naver.com"+url)
    # https: // movie.naver.com / movie / bi / mi / basic.nhn?code = 193804
    # href = "/movie/bi/mi/basic.nhn?code=193804"
    # 복습(html): <a href="">여기</a> ->태그와 속성