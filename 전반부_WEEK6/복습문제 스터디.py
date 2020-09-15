## 김윤서
# 파파고 번역
'''
from selenium import webdriver
import time

translate = input("번역할 내용 입력: ")
lang = input("번역할 언어: (1)영어 (2)일본어 (3)중국어(간체) ")

driver = webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com/")
time.sleep(0.5)

input_translate = driver.find_element_by_css_selector("textarea#txtSource")
input_translate.send_keys(translate)
language_Change = driver.find_element_by_css_selector("button#ddTargetLanguage2Button")
language_Change.click()

if lang == 1:
    eng = driver.find_element_by_css_selector("div.dropdown_menu___XsI_h li: nth - of - type(2) > *")
    eng[3].click()

    # div.dropdown_menu___XsI_h li: nth - of - type(2)

elif lang == 2:
    jap = driver.find_element_by_css_selector("div.dropdown_menu___XsI_h li:nth-of-type(3) > *")
    jap[3].click()

 # div.dropdown_menu___XsI_h li:nth-of-type(3)

elif lang == 3:
    chin = driver.find_element_by_css_selector("div.dropdown_menu___XsI_h li:nth-of-type(4) > *")
    chin[3].click()
 # div.dropdown_menu___XsI_h li:nth-of-type(4)
else:
    print("잘못 누르셨습니다.")

button = driver.find_element_by_css_selector("button#btnTranslate")
button.click()
'''

## 김윤서(파파고) 답:
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://papago.naver.com/")
sent = input("번역할 내용 입력 : ")
lan = int(input("1. 영어 2. 일본어 3. 중국어 : "))

driver.find_element_by_css_selector("textarea#txtSource").send_keys(sent)
driver.find_elements_by_css_selector("span.btn_dropdown_arr___2xcBb")[1].click()
time.sleep(0.5)
year_select = driver.find_elements_by_css_selector("ul.dropdown_menu_inner___29_zc")[1]
for option in year_select.find_elements_by_tag_name('span'):
    if lan == 1:
        if option.text == "영어":
            option.click()
            break
    elif lan == 2:
        if option.text == "일본어":
            option.click()
            break
    elif lan == 3:
        if option.text == "중국어(간체)":
            option.click()
            break
    else:
        print("잘못입력")

'''


## 박지연
# 네이버 증권>국내증시>업종별 시세(https://finance.naver.com/sise/sise_group.nhn?type=upjong)에 접속하여 현재 업종별 시세 정보를 출력하여라.
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")

driver.get("https://finance.naver.com/sise/sise_group.nhn?type=upjong")
name = driver.find_elements_by_css_selector("tr>td>a")
fluctuation = driver.find_elements_by_css_selector("span.tah")

print("< 국내증시 업종별 시세 정보 >")
print("="*50)

for i in range(len(name)-5):
    print("##### 업종명 #####")
    print(name[i].text+"\n")
    print("##### 전일대비 #####")
    print(fluctuation[i].text)
    print("="*50)

driver.close()

### 다시 하기 
'''
# 업종명:
# 전일대비:



## 성혜원
#
'''
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://v4.map.naver.com/")

driver.find_elements_by_css_selector("button.btn_close")[1].click() # 네이버 지도 업데이트 후 안내메시지 끄기

map = driver.find_element_by_css_selector("a.spm_nfw")
map.click()

start = driver.find_elements_by_css_selector("div.pf_enter > div > *")
start[1].send_keys("이화여자대학교")

arrive = driver.find_elements_by_css_selector("div.pf_enter > div> *")
arrive[4].send_keys("청계천")

button = driver.find_element_by_css_selector("a.spm_pfa_startfind")
button.click()
'''
# 답
from selenium import webdriver
import time

driver=webdriver.Chrome(":/chromedriver.exe")

driver.get("https://v4.map.naver.com/")

#팝업창 닫기
close_box=driver.find_element_by_css_selector("div.popup_content button.btn_close")
close_box.click()

find_load=driver.find_elements_by_css_selector("li a.spm")
find_load[1].send_keys("\n")

time.sleep(1)

input=driver.find_elements_by_css_selector("input.input_act")

#출발지
input[1].send_keys("이화여자대학교")
input[1].send_keys("\n")
time.sleep(2)

#도착지
input[2].send_keys("청계천")
input[2].send_keys("\n")
time.sleep(2)

start=driver.find_elements_by_css_selector("div.pf_act a.spm")
start[2].click()
time.sleep(2)

path=driver.find_elements_by_css_selector("div.path_num span.spm")
for i in range(len(path)):
    print("<"+path[i].text+">\n")

    detail_path=driver.find_elements_by_css_selector("div.fw_path_traffic")
    for j in range(len(detail_path)):
        print(detail_path[j].text)

    print("="*50)



## 윤희준
'''
from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver")
driver.get("https://cyber.ewha.ac.kr/")

login = driver.find_element_by_css_selector("a.btn-sso")
login.click()

id = driver.find_element_by_css_selector("input#login_id")
id.send_keys("1882002")
pw = driver.find_element_by_css_selector("input#usr_pwd")
pw.send_keys("ko023221**")

button = driver.find_element_by_css_selector("button.btn-login")
button.click()
'''

## 이미경
'''
from selenium import webdriver
import time
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.koreabaseball.com/Schedule/Schedule.aspx")

#1. 드롭다운 메뉴에서 년, 월을 선택하기
# 2. 데이터 수집하기 (수집 항목 : 날짜, 시간, 경기 팀 2개, 스코어 2개, 구장, 비고(취소와 같은 특이사항이 적혀있습니다.)
# 3. 엑셀로 저장하기 (첫 행에 헤더 추가, 예시 아래)
# + 취소된 경기 같은 경우 점수 칸이 비어있고, 사유가 있습니다! 처리 해주기
# + 드롭다운 메뉴 선택은 배우지 않았습니다!! 아래 코드를 참고해주세요

# year_select = driver.find_element_by_css_selector(#드롭다운 메뉴 선택자)
# for option in year_select.find_elements_by_tag_name(#드롭다운 내용 들어있는 선택자):
#  if option.text == str(#선택할 년도):
#  option.click()
#  break

# 날짜: td.day
# 시간: td.time
# 경기팀 2개: td.play > span
# 스코어 2개 : span.lose    span.win
# 구장: table#tblSchedule td:nth-of-type(8)
# 비고: table#tblSchedule td:nth-of-type(9)
'''