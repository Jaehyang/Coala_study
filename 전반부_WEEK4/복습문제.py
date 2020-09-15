#이화 뉴스 홍보영상라이브러리에서 저장한 데이터 엑셀파일로 저장하기

import requests
from bs4 import BeautifulSoup

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "요약", "날짜", "조회수"])


for i in range(0, 50,10) :
    raw = requests.get("http://www.ewha.ac.kr/ewha/news/movie.do?mode=list&&articleLimit=10&article.offset="+str(i), headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    promovideo = html.select("div.b-box02")

    for pr in promovideo :
        title = pr.select_one("a.b-title").text.strip()
        summary = pr.select_one("div.b-text-box").text.strip()
        date = pr.select_one("li.b-date").text.strip()
        view = pr.select_one("li.b-hit").text.strip()
        print(title, '\n', summary, '\n', date, '\n', view)
        print("="*50)

        date = date.replace("등록일", "")
        view = view.replace("조회수", "")
        sheet.append([title, summary, date, view])

wb.save("ewhanews.xlsx")