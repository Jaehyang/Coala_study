## 네이버 영화 데이터 수집(제목, 평점, 장르, 감독, 배우 데이터) https://movie.naver.com/movie/running/current.nhn

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://movie.naver.com/movie/running/current.nhn", headers={"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

#컨테이너 dl.lst_dsc
movies = html.select("dl.lst_dsc")

for m in movies:
    # 제목 dt.tit > a
    title = m.select_one(" dt.tit > a").text
    # 평점 div.star_t1 a span.num
    score = m.select_one("div.star_t1 a span.num").text

    ### 선택자를 구분할 수 없을 때 원하는 데이터를 특정하는 방법 두가지

    ## 1. select함수 이용하는 방법 : select함수는 데이터를 리스트 형태로 저장하므로, 리스트에 저장된 데이터를 인덱싱 방법을 활용하여 특정 순서의 데이터를 수집함.
    # 장르 dl.lst_dsc dl.info_txt1 dd a
    # 감독 dl.lst_dsc dl.info_txt1 dd a
    # 배우 dl.lst_dsc dl.info_txt1 dd a
    
    info = m.select("dl.info_txt1 dd")          # 장르, 감독, 배우 데이터를 리스트 형식으로 저장. 0부터 셈.
    # 장르
    genre = info[0].select("a")
    # 감독
    director = info[1].select("a")
    # 배우
    actor = info[2].select("a")

    print(title)
    print(score)
    for g in genre:
        print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("="*50)       # 해당 데이터가 없을시 에러가 뜸.


    ## 2. 선택자를 사용하는 방법 : 태그이름: nth-of-type(순서)  -> 클래스나 id는 쓸 수 없음.
    # dl.lst_dsc dl.info_txt1 dd:nth-of-type(1)  -> dl.lst_dsc dl.info_txt1 이 가지고 있는 n번째 dd

    # 장르 dl.info_txt1 dd a
    genre = m.select("dl.info_txt1 dd:nth-of-type(1) a")       # 꺼내와서 다시 a를 선택할 필요 없이 a를 그대로 쓸 수 있음. 숫자를 1부터 셈.
    # 감독 dl.info_txt1 dd a
    director = m.select("dl.info_txt1 dd:nth-of-type(2) a")
    # 배우 dl.info_txt1 dd a
    actor = m.select("dl.info_txt1 dd:nth-of-type(3) a")

    print(title)
    print(score)
    for g in genre:
        print(g.text)
    for d in director:
        print(d.text)
    for a in actor:
        print(a.text)

    print("="*50)      # 해당 데이터가 없을시에도 에러가 안뜸. 해당 데이터가 없을때 빈 리스트가 들어가기 때문
