import requests
from bs4 import BeautifulSoup
import openpyxl

keyword = input("검색어를 입력해주세요: ")

try:                     #이 파일 불러오는 걸 시도해보기 -> 기존의 파일이 있을 경우 잘 작동
    wb = openpyxl.load_workbook("navernews.xlsx")      #수집된 데이터가 누적되어 저장됨
    sheet = wb.active
    print("불러오기 완료")
except:            #if 시도시 에러 발생했을 때, 새로운 파일에 데이터 저장
    wb = openpyxl.Workbook()           #새로운 워크북(엑셀)을 만들기
    sheet = wb.active                  #워크북.active   ->  현재 활성화된 엑셀 파일의 시트 선택
    sheet.append(["제목", "언론사"])           # 헤더 넣어주기(데이터 처음 만들때만 필요)
    print("새로운 파일을 만들었습니다.")

page = 1
for page in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query="+keyword+"&start="+str(page), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: ul.type01 > li
    # 기사제목: a._sp_each_title
    # 언론사: span._sp_each_source

    #1. 컨테이너 수집
    articles = html.select("ul.type01 > li")

    #2. 기사 데이터 수집     #3. 반복하기
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text
        print(title, source)
        sheet.append([title, source])        #시트.append(리스트) 데이터 행별로 저장

wb.save("navernews.xlsx")         #해당하는 워크북을 원하는 이름으로 저장