## 셀레니옴 연습하기 - 네이버 지도 ##

from selenium import webdriver
import time       # 파이썬 프로그램에서 시간을 조정해주는 파이썬 내부 라이브러리 time: 시간과 관련된 여러가지 기능을 포함
                  # 네이버 지도 검색에서는 검색버튼을 누른 후, 검색결과를 확인하기까지 짧지만 데이터를 로딩하는 시간이 필요함.

##1. 웹드라이버 켜기 (ex 크롬)
driver = webdriver.Chrome("./chromedriver")      # ./: 현재 디렉토리에 있는 크롬 드라이버를 열어줘   -> 드라이버 변수를 만들기, 크롬을 켜
##2. 네이버 지도 접속하기 (url창에 입력)
driver.get("https://v4.map.naver.com/")          # 주소창에 해당하는 주소를 입력하여 URL에 접속하겠다는 의미. 헤더 필요없음.

# 네이버 지도 업데이트 후 안내메시지 끄기
driver.find_elements_by_css_selector("button.btn_close")[1].click()

##3. 검색창에 검색어 입력하기 // 검색창: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")          # cf. request에서는 select를 통해 데이터 가져옴.
search_box.send_keys("치킨")                                                    # send_keys: 텍스트를 입력할 수 있는 공간에 치킨이라는 키워드 전송
##4. 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()
# 1초의 지연시간 주기
time.sleep(1)
##5. 검색 결과 확인하기
# 컨테이너: dl.lsnx_det
#selenium을 활용한 데이터수집 방법 : select/select_one 함수를 find_element_by_css_selector / find_elements_by_css_selector로 바꿔주면 됨.
# c.f) stores = html.select("dl.lsnx_det")
stores = driver.find_elements_by_css_selector("dl.lsnx_det")               #element's' 복수형: 이 선택자에 해당하는 모든 요소를 리스트 형식으로 가져옴.

for s in stores:
    name = s.find_element_by_css_selector(" dt > a ").text                 #.text : 데이터가 아닌 요소 이므로 변환해줘야함.
    addr = s.find_element_by_css_selector(" dd.addr ").text
    tel = s.find_element_by_css_selector(" dd.tel ").text
    # 가게 이름: dl.lsnx_det dt > a
    # 가게 주소: dd.addr
    # 전화번호: dd.tel

    print(name, '/', addr, '/', tel)
