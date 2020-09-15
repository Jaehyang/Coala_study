# 네이버 시리즈 e북 TOP100 데이터 수집하기
#컨테이너, 제목, 저자
# 컨테이너: div#content li
# 제목: div#content li a strong
# 저자: span.writer

import requests
from bs4 import BeautifulSoup

for i in range(1, 6) :
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div#content li")       # 모범답안: div.lst_thum_wrap li

    for bk in books :
        title = bk.select_one("a strong").text
        writer = bk.select_one("span.writer").text
        print(title, "/", writer)



