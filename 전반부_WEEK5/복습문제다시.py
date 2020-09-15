# 네이버 장르별 웹툰 데이터 수집하기 https://comic.naver.com/webtoon/genre.nhn

import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

raw = requests.get("https://comic.naver.com/webtoon/genre.nhn", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 ul.img_list li
# 제목 ul.img_list li dt a

container = html.select("ul.img_list li")

for c in container:
    title = c.select_one("ul.img_list li dt a")
    url = title.attrs["href"]
    # 제목 링크 href="/webtoon/list.nhn?titleId=733766"
    # https://comic.naver.com/webtoon/list.nhn?titleId=651673
    each_raw = requests.get("https://comic.naver.com"+url, headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    #제목 div.detail h2
    #작가 div.detail h2 span:nth-of-type(2)
    #장르 span.genre

    title = each_html.select_one("div.detail h2").text.strip()
    writer = each_html.select("div.detail h2 span:nth-of-type(2)")
    genre = each_html.select("span.genre")

    print("제목:", title.strip())

    print("작가: ")
    for w in writer:
        print(w.text.strip())

    print("장르: ")
    for g in genre:
        print(g.text)

    print("="*10)

    # 포스터 div.thumb a img
    poster = each_html.select_one("div.thumb a img")
    poster_src = poster.attrs["src"]
    urlretrieve(poster_src, "webtoonposter/" + title[:2] + ".png")