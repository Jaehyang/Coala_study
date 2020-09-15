# IMDb(https://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth)의 현재 상영중 영화목록에서 현재 상영중 영화의 상세페이지에 접속해 포스터를 저장합니다.
# 상세 페이지에 접속할 수 있는 링크주소를 수집합니다.
# 상세 페이지의 포스터를 선택할 수 있는 선택자를 찾습니다.
# 포스터 이미지가 저장되어 있는 속성을 찾아 포스터를 다운 받습니다.

import requests
from bs4 import BeautifulSoup

from urllib.request import urlretrieve

# src = "https://m.media-amazon.com/images/M/MV5BNTM5YWZiMzQtNDQxZS00ODI0LWJjNTQtZmQ3OWU3Njg4NWYyXkEyXkFqcGdeQXVyNzc4NTU3Njg@._V1_UX182_CR0,0,182,268_AL_.jpg"
# urlretrieve(src, "scoob!.png")

# IMDb 홈페이지에 데이터 요청하기
raw = requests.get("https://www.imdb.com/list/ls016522954/?ref_=nv_tvv_dvd", headers={"User-Agent" : "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 수집하기
container = html.select("div.lister-item-content")

for c in container :
    title = c.select_one("h3.lister-item-header>a")

    # 제목에서 링크 연결주소를 가져와 저장하기
    url = title.attrs["href"]

    print("제목: ", title.text)
    # https: // www.imdb.com / title / tt3152592 /?ref_ = ttls_li_tt
    # href = "/title/tt3152592/?ref_=ttls_li_tt"

    # 링크 안 데이터 수집하기 (상세페이지에 접속해서 데이터를 요청하기)
    each_raw = requests.get("https://www.imdb.com" + url, headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 포스터 데이터를 선택해서 src값 가져오기
    poster = each_html.select_one("div.poster img")
    poster_src = poster.attrs["src"]
    print(poster_src)      #링크 잘 나오는지 확인
    print("="*50)

    # urlretrieve 함수를 사용해서 이미지 저장하기
    # IMDbposter 폴더 안에 이미지 저장하기
    urlretrieve(poster_src, "IMDbposter/" + title.text[:4] + ".png")
