#다음뉴스 기사 데이터 수집결과 저장하기(1~3페이지)

import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()           #새로운 워크북(엑셀)을 만들기
sheet = wb.active                  #워크북.active   ->  현재 활성화된 엑셀 파일의 시트 선택
sheet.append(["제목", "요약"])

for i in range(1,4) :
    raw = requests.get("https://search.daum.net/search?w=news&q=%EC%BD%94%EC%95%8C%EB%9D%BC&DA=PGD&spacing=0&p="+str(i))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("ul#clusterResultUL li")

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text
        print(title, "\n", summary)
        print("=" * 100)

        sheet.append([title, summary])

wb.save("daumnews.xlsx")