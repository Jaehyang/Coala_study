##김윤서
#다음영화 영화별 상세페이지에 들어가서 영화의 제목, 장르, 누적관객수 데이터 수집하기
#누적관객수가 5만명 이상인 영화의 데이터만 엑셀에 저장하기
'''
import requests
from bs4 import BeautifulSoup
import openpyxl

raw = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("ul.list_boxthumb li")

for c in container:
    title = c.select_one("strong.tit_join>a")
    url = title.attrs["href"]
    # 제목 링크 href="http://movie.daum.net/movie/redirect?ticketId=M000077324"

    each_raw = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    title = each_html.select_one("div.subject_movie strong.tit_movie").text
    genre = each_html.select("dl.list_movie dd:nth-of-type(1)")
    audience = each_html.select("dl.list_placing dd:nth-of-type(2)").text
    audience = audience[:-1]

    if float(audience) < 50000 :
        continue

    print("<제목>\n", title)

    print("<장르>")
    for g in genre:
        print(g.text)

    print("<누적관객수>")
    for a in audience:
        print(a.text)

    print('-'*15)
'''

## 박지연 http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page=1
#1000대기업 공채 정보를 1페이지-20페이지까지 가져와 출력하기
'''
import requests
from bs4 import BeautifulSoup

for i in range(1,21) :
    raw = requests.get("http://www.jobkorea.co.kr/Starter/?JoinPossible_Stat=0&schOrderBy=0&LinkGubun=0&LinkNo=0&schType=0&schGid=0&Page="+str(i))
    html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너 ul.filterList li
# 회사이름 div.coTit a
# 채용 정보 div.tit a
# 채용 세부 정보 div.sTit
    container = html.select("ul.filterList li")
    for c in container:
        name = c.select_one("div.coTit a").text
        info = c.select_one("div.tit a").text.strip()
        subinfo = c.select("div.sTit span")

        print("- 회사이름: ", name)
        print("- 채용 정보: ", info)
        print("- 세부 채용 정보: ", end="")        # 세부 채용 정보를 한 줄에 가져오기 위해
        for s in subinfo:
            print(s.text.strip(), end=" / ")
        print()

        print("-"*5)
    print("="*30)
'''

## 성혜원 http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes
#페스티벌별 상세 페이지에 접속하여 페스티벌의 제목/장소/가격 데이터를 수집하기
'''
import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.stit tbody > tr")

for c in container:
    title = c.select_one("span.fw_bold a")
    url = title.attrs["href"]

    each_raw = requests.get("http://ticket.interpark.com" + url, headers={"User-Agent": "Mozilla/5.0"})
    each_html = BeautifulSoup(each_raw.text, 'html.parser')

    title = each_html.select("div.dt_Name span:nth-of-type(1)")

    print("<페스티벌 이름>")
    for t in title:
        print(t.text.replace("|", ""))

    temp = each_html.select("li.item")
    for t in temp:                           # 장소 데이터 가져올때, 부제, 장소, 기간 등이 페스티벌마다 달라서...
        text1 = t.text.strip()
        if "장소" in text1:                  # '장소'라는 단어가 text1에 있으면 place 리스트에 저장
            place = text1[2:]
            break
    print("<장소>\n", place)

    price = each_html.select_one("td.costTd")

    if price is not None:
        print("<가격>", price.text.strip())
    else:
        print("\n가격이 없습니다.")
    print("="*30)

###가격이 안나옴??????
'''

## 윤희준 http://lib.ewha.ac.kr/digicol/list/5083
# 학교 도서관 추천도서 페이지에서, 제목만 가져오기
'''
import requests
from bs4 import BeautifulSoup

raw = requests.get("http://ticket.interpark.com/TPGoodsList.asp?Ca=Liv&SubCa=Fes", headers={"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("li.items dl")
for c in container:
    title = c.select_one("dd.title").text
    
    print(title)
#제목: dd.title
'''

## 이미경 -> 셀레니움으로 해보기
''' -> beautifulsoup으로 한거
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

keyword = input("검색어: ")
raw = requests.get("https://search.naver.com/search.naver?where=image&sm=tab_jum&query="+keyword, headers={"User-Agent":"Mozilla/5.0"})
html= BeautifulSoup(raw.text, "html.parser")

for i in range(10):
    photo = html.select("div#main_pack div div a img") #컨테이너처럼 받고
    for p in photo:
        photo_url = p.attrs["src"]
        urlretrieve(photo_url, "hi/" + str(i+1) + ".png")
'''

# 셀레니움으로
from selenium import webdriver
import time

keyword = input("검색어를 입력하세요: ")
driver = webdriver.Chrome("./chromedriver")
time.sleep(1)

driver.get("https://www.naver.com/")

# 원하는 키워드 입력
keyword_input = driver.find_element_by_css_selector("input#query")
keyword_input.send_keys(keyword)
button = driver.find_element_by_css_selector("button#search_btn")
button.click()

# 이미지 사이트로 가기
image_site = driver.find_element_by_css_selector("li.lnb2 a")
image_site.click()

# 이미지 10개 다운받기
for i in range(10):
    images = driver.find_element_by_css_selector("span.img_border")
    images[i].screenshot(str(i) + ".png")

# 저장할 폴더 따로 만들기