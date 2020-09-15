## 인스타그램에서 ootd 해시태그 검색결과(https://www.instagram.com/explore/tags/ootd/) 페이지에 접속해서 12개 포스트의 본문 내용을 수집하기 ##
# 인스타그램의 class/id는 자동 생성프로그램에 의해 랜덤하게 생성됩니다.

from selenium import webdriver
import time

##1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")
time.sleep(1)
##2. 인스타그램 ootd 해시태그 검색결과 페이지 접속하기
driver.get("https://www.instagram.com/explore/tags/ootd/")

id = "go990525@naver.com"
pw = "ko023221**"

##3. 인스타그램 로그인하기
# 로그인 버튼 누르기 div.eLAPa 인덱스1
login = driver.find_element_by_css_selector("div.eLAPa")
login.click()

# 아이디 label.f0n8F 인덱스1
input_id = driver.find_element_by_css_selector("form.HmktE div:nth-of-type(2) input")
input_id.send_keys(id)
# 비밀번호 label.f0n8F 인덱스2
input_pw = driver.find_element_by_css_selector("form.HmktE div:nth-of-type(3) input")
input_pw.send_keys(pw)
# 로그인 button.L3NKy
login_button = driver.find_element_by_css_selector("div.Igw0E button.L3NKy")
login_button.click()
time.sleep(2)

##4. 컨테이너(포스트) 12개 저장
instagram = driver.find_elements_by_css_selector("div.v1Nh3 a div.eLAPa")
instagram = instagram[:12]

##5. 포스트 본문 내용 수집하기 // 내용: div.C4VMK span 인덱스1
for insta in instagram:         # 컨테이너 반복하기
    # 포스트 클릭하기
    insta.click()

    # 시간 지연
    time.sleep(1)

    # 본문 선택 후 출력
    post = driver.find_element_by_css_selector("div.C4VMK span").text
    print(post)

    # 닫기 버튼 클릭
    but_close = driver.find_element_by_css_selector("div.Igw0E button.wpO6b path")
    but_close.click()



