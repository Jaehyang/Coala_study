## 구글지도(https://www.google.com/maps/)에 카페를 검색해서 검색된 카페들의 이름, 평점, 주소 데이터를 수집하기 ##
# 구글의 경우 지연시간을 길게 줘야함 (평균 5 ~ 10초)

#1. 구글 지도 페이지에 접속한다.
#2. 입력창에 키워드(카페)를 입력한다.
#3. 검색버튼을 누른다.
#4. --- 지연 ---
#5. 검색 결과를 확인한다.
#6. 다음페이지를 누른다.
#7. 4, 5번을 반복한다.
#8. 다음페이지가 없으면 반복을 종료한다.

from selenium import webdriver
import time

##1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

##2. 구글 지도 접속하기 (url창에 입력)
driver.get("https://www.google.com/maps/")

##3. 검색창에 검색어 입력하기 // 검색창: input#searchboxinput
search_box = driver.find_element_by_css_selector("input#searchboxinput")
search_box.send_keys("치킨")

##4. 검색버튼 누르기 // 검색버튼: button#searchbox-searchbutton
search_button = driver.find_element_by_css_selector("button#searchbox-searchbutton")
search_button.click()

##5. 검색 결과 확인하기(반복문)
# 컨테이너: div.section-result-content
# 이름: h3.section-result-title > span
# 평점: span.cards-rating-score (try-except 쓰기)
# 주소: span.section-result-location
# 다음페이지: span.n7lv7yjyC35__button-next-icon

print("<카페 검색결과>")
for i in range(999):
    time.sleep(5)
    cafe = driver.find_elements_by_css_selector("div.section-result-content")

    for c in cafe:
        name = c.find_element_by_css_selector("h3.section-result-title > span").text
        try:
            score = c.find_element_by_css_selector("span.cards-rating-score").text
        except:
            score = "평점 없음"
        addrs = c.find_element_by_css_selector("span.section-result-location").text
        print(name, '/', score, '/', addrs)
    try:
        nextpage = driver.find_element_by_css_selector('button#n7lv7yjyC35__section-pagination-button-next')
        nextpage.click()
    except:
        print("데이터 수집 완료.")
        break