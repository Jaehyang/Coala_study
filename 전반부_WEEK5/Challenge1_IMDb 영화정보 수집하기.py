## IMDb 페이지에서 현재 상영 중인 영화정보 수집하기  https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd

## 제목, 평점(metascore), 감독, 배우 찾기
# 제목: h3.lister-item-header>a
# 평점: div.ipl-rating-widget div.small > span.ipl-rating-star__rating
# 감독: p.text-muted.text-small>a
# 배우: p.text-muted.text-small>a
# 장르: p.text-muted.text-small>span.genre

## 코드를 통해 데이터 수집하기(select함수 이용)
'''
import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd", headers={"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.lister-item-content")
for c in container :
    title = c.select_one("h3.lister-item-header>a").text
    metascore = c.select_one(" div.ipl-rating-widget div.small > span.ipl-rating-star__rating")
    info = c.select("p.text-muted.text-small")
    director = info[1].select("a")
    genre = info[0].select("span.genre")

    print("제목: ", title)
    print("평점: ", metascore.text)
    print("감독 및 배우: ")
    for d in director:
        print(d.text)
    for g in genre:
        print(g.text)
    print("="*50)

##### 평점 안적힌 영화 오류 해결 방법은???
'''

## 액션 장르의 영화만 출력하기(선택자 사용)

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd", headers={"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.lister-item-content")
for c in container :
    title = c.select_one("h3.lister-item-header>a").text
    metascore = c.select_one(" div.ipl-rating-widget div.small > span.ipl-rating-star__rating")
    director = c.select("div.lister-item-content p:nth-of-type(3) a")
    genre = c.select_one("div.lister-item-content p:nth-of-type(1) span.genre")

    if "Action" not in genre.text:
        continue

    print("제목: ", title)

    if metascore is not None:
        print( "\n평점:", metascore.text.strip())
    else:
        print("\n평점이 없습니다.")
        #
        # print("평점: ", metascore.text)

    print("\n장르: ")
    for g in genre:
        print(g.strip())       #g는 .text 붙이면 에러뜸.

    print("\n감독 및 배우: ")
    for d in director:
        print(d.text)

    print("="*20)

