## Selenium을 활용하여 네이버 로그인 페이지(https://nid.naver.com)와 페이스북(https://www.facebook.com)에 자동으로 로그인하는 프로그램을 만들어보기 ##
    # 로그인 절차에 대해 생각해봅니다.
    # 아이디/비밀번호를 입력하고 로그인버튼을 누를 수 있는 선택자를 찾습니다.
    # 코딩을 통해 자동 로그인 장치를 만들어봅니다.

# 페이스북 #
from selenium import webdriver
import time01029403

##1. 계정정보 입력하기
id = input("아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

##2. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

##3. 네이버 로그인 페이지 접속하기
driver.get("https://www.facebook.com")
time.sleep(0.5)   # 페이지 접속 후 시간 지연

##4. 아이디, 비밀번호 입력하기 // 아이디: input#email, 비밀번호: input#pass
input_id = driver.find_element_by_css_selector("input#email")
input_id.send_keys(id)
input_password = driver.find_element_by_css_selector("input#pass")
input_password.send_keys(password)

##5. 로그인 버튼 누르기 // 로그인 버튼: label#loginbutton
login = driver.find_element_by_css_selector("label#loginbutton")
login.click()
