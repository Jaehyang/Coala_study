#1. 성혜원 답(네이버 지도 이화여대 -> 청계천)
'''
from selenium import webdriver
import time

driver=webdriver.Chrome("./chromedriver")

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
'''

#2. 이미경 답(야구)
from selenium import webdriver
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(['년','월','날짜','시간','팀1','팀2','점수1','점수2','장소','사유'])

# 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

# 야구 경기 사이트 접속하기
driver.get("https://www.koreabaseball.com/Schedule/Schedule.aspx")

# 일정 검색 버튼 누르기


year_select = driver.find_element_by_css_selector("select#ddlYear")
for option in year_select.find_elements_by_tag_name('option'):
    if option.text == "2020": #년도 입력
        option.click()
        break


month_select = driver.find_element_by_css_selector("select#ddlMonth")
for option in month_select.find_elements_by_tag_name('option'):
    if option.text == "05": #월 입력
        option.click()
        break

    # 검색 결과 수집하기

    ## 선택자 (컨테이너)
    ## 날짜, 시간, 경기 팀 2개, 점수, 구장
container = driver.find_elements_by_css_selector("tbody tr")


for c in container:
    try:
        date = c.find_element_by_css_selector("td.day").text
    except:
        pass

    try:
        time = c.find_element_by_css_selector("td.time b").text
    except:
        continue
    team1 = c.find_element_by_css_selector("td.play>span").text
    team2 = c.find_elements_by_css_selector("td.play>span")[1].text
    place = c.find_elements_by_css_selector("td")[-2].text
    try:
        score1 = c.find_elements_by_css_selector("td.play em span")[0].text
        score2 = c.find_elements_by_css_selector("td.play em span")[2].text
    except: #특정 사유로 경기 취소될 경우
        score1 = "-"
        score2 = "-"
        reason = c.find_elements_by_css_selector("td")[-1].text
        print("%s %s %s %s vs %s %s , %s %s" %(date, time, team1,score1,score2, team2, place, reason))
        sheet.append(["2020","05",date,time,team1,team2,score1,score2,place,reason])
        continue

    print("%s %s %s %s vs %s %s , %s" %(date, time, team1,score1,score2, team2, place))
    sheet.append(["2020","05",date,time,team1,team2,score1,score2,place])


wb.save('baseball.csv')