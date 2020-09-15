## 다음영화 - 예매순위 페이지(http://ticket2.movie.daum.net/Movie/MovieRankList.aspx)에서 영화별 상세페이지에 접속하여 (빠른예매-> 예매순위)
## 영화의 제목 / 평점 / 장르 / 감독 / 배우 데이터를 수집하기

# 예매순위 페이지에서 각 영화 상세페이지로 들어갈 수 있는 링크를 찾습니다.
# 상세페이지에서 원하는 데이터(제목, 평점, 장르, 감독, 배우)를 찾을 수 있는 선택자를 찾습니다.
# 코딩을 통해 데이터 수집기를 완성합니다.
# 심화: 검색결과를 파일 형식으로 저장해보기

import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 div.desc_boxthumb     #모범답안: ul.list_boxthumb > li (포스터까지 포함)
# 제목 strong.tit_join a

container = html.select("div.desc_boxthumb")

for c in container:
    title = c.select_one("strong.tit_join > a")
    url = title.attrs["href"]
    # 제목 링크 href="http://movie.daum.net/movie/redirect?ticketId=M000077324"

    each_raw = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    # 상세페이지
    # 제목 div.subject_movie strong.tit_movie
    # 평점 div.subject_movie a.raking_grade > em.emph_grade
    # 장르 dl.list_movie > dd:nth-of-type(1)
    # 감독 dl.list_movie > dd:nth-of-type(5) a
    # 배우 dl.list_movie > dd:nth-of-type(6) a

    title = each_html.select_one("div.subject_movie strong.tit_movie").text.strip()
    metascore = each_html.select_one("div.subject_movie a.raking_grade>em.emph_grade").text

    genre = each_html.select_one("dl.list_movie dd:nth-of-type(1)").text
    director = each_html.select("dl.list_movie dd:nth-of-type(5) a")
    actor = each_html.select("dl.list_movie dd:nth-of-type(6) a")

    print("제목:", title)
    print("평점: ", metascore)
    print("장르: ", genre)

    print("감독: ")
    for d in director:
        print(d.text)

    print("배우: ")
    for a in actor:
        print(a.text)

    print("="*50)