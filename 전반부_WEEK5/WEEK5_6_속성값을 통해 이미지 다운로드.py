## 속성 값을 통해 이미지 다운로드 받기
# img 태그의 src 복습하기
# urlretrieve를 활용하여 이미지 파일 저장하기

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

# import ssl                                        #만약 컴퓨터 환경 방화벽 등 문제로 안될 때 같이 써주기
# ssl._create_default_https_context = ssl._create_unverified_context


src = "https://movie-phinf.pstatic.net/20200428_196/1588038709486FYyHu_JPEG/movie_image.jpg?type=m203_290_2"
urlretrieve(src, "프리즌이스케이프.png")                     #현재 코드가 있는 위치에 원하는 파일 이름으로 이미지 저장

raw = requests.get("https://movie.naver.com/movie/running/current.nhn", headers={"User-Agent" : "Mozilla/5.0"})
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

    # reviews = each_html.select("div.score_result > ul > li")
    # for r in reviews:
    #     stars = r.select_one("div.star_score em").text.strip()     #select_one으로 했으니 .text를 통해 문자 데이터로 바꿔주기
    #     reple = r.select_one("div.score_reple p").text.strip()
    #
    #     print(stars, reple)               #왜 리뷰와 평점이 다섯개씩밖에 안나오는지

    #포스터 div.mv_info_area div.poster img

    poster = each_html.select_one("div.mv_info_area div.poster img")
    poster_src = poster.attrs["src"]
    # print(poster_src)
    # urlretrieve(poster_src, "poster.png")             #영화 리스트의 모든 포스터가 아닌 마지막 영화 포스터만 저장됨.
                                                        # 모든 포스터가 "poster.png"로 저장되고 있기 때문에 계속해서 같은 파일이름으로 덮어쓰여짐
                                                        # ->파일경로를 설정하고 이름을 바꿔야함.(각각의 포스터를 따로 저장하고, 별도의 디렉토리 안에 저장) -> 디렉토리 미리 만들어야함
    urlretrieve(poster_src, "poster/"+title.text[:2]+".png")      #파일이름(경로)에서 /는 디렉토리 구조를 이야기하므로 "poster 디렉토리 안에 제목.png로 저장해줘!" 라는 의미
                                                                  #파일이름에는 ₩ / : ? 등의 문자를 사용할 수 없음.