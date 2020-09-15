## Selenium을 사용해서 파파고(https://papago.naver.com)에서 "seize the day"라는 문장을 입력, 번역결과를 출력하는 프로그램을 만들어보기 ##
# 파파고 번역 서비스 이용 절차 적어보기
# 지연시간이 필요한 부분 생각해보기
# 코딩을 통해 번역결과 출력하기
# 입력도구(input, textarea)를 찾아 .send_keys를 사용하기

from selenium import webdriver
import time

##1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

##2. 파파고 페이지 접속하기 (url창에 입력)
driver.get("https://papago.naver.com/")
time.sleep(0.5)   # 페이지 접속 후 시간 지연

##3. 입력창에 검색어 입력하기 // 번역창: textarea#txtSource
input_box = driver.find_element_by_css_selector("textarea#txtSource")
input_box.send_keys("seize the day")

##4. 번역하기 버튼 누르기 // 번역하기 버튼: button.btn_text___3-laJ
button = driver.find_element_by_css_selector("button.btn_text___3-laJ")
button.click()
time.sleep(1)    # 버튼 클릭 후 시간 지연

##5. 번역 결과 확인하기
result = driver.find_element_by_css_selector("div#txtTarget").text
print(result)

# 크롬창 닫기
# driver.close()