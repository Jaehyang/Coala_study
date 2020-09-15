## 네이버 시리즈 e북 TOP100 데이터 수집결과를 csv 또는 excel로 저장하기

#csv
f = open("naverseries.csv", "w")       # naverseries.csv 파일을 쓰기(w) 모드로 열어주기
f.write("제목, 작가\n")      # 데이터의 헤더 부분을 써주기

import requests
from bs4 import BeautifulSoup

for i in range(1, 6) :
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")

    for bk in books :
        title = bk.select_one("a strong").text
        writer = bk.select_one("span.writer").text
        print(title, "/", writer)

        title = title.replace(",", "")           # ,로 데이터가 구분되지 않도록 수집한 제목/저자에서 ,를 삭제해주기
        writer = writer.replace(",", "")

        f.write(title + ',' + writer + '\n')        # 수집한 제목/저자를 파일에 써주기
f.close()       #csv파일을 닫아주기



#excel
import requests
from bs4 import BeautifulSoup
import openpyxl           # openpyxl 패키지 불러오기

# 엑셀 파일 작성을 위해서 Workbook, Sheet 구성해주기
wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["제목", "작가"])     # 파일에 헤더 입력해주기

for i in range(1, 6) :
    raw = requests.get("https://series.naver.com/ebook/top100List.nhn?page="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    books = html.select("div.lst_thum_wrap li")

    for bk in books :
        title = bk.select_one("a strong").text
        writer = bk.select_one("span.writer").text
        print(title, "/", writer)

        sheet.append([title, writer])         # 수집한 제목, 저자를 엑셀 파일에 추가하기


wb.save("naverseries.xlsx")