## 페이지 변경하며 데이터 수집하기
# 네이버 뉴스 데이터 수집에서는 여러 페이지에서 데이터를 수집하기 위해 URL 요청값을 사용함.
# 하지만 네이버 지도와 같은 동적페이지에서는 URL이 변하지 않기 때문에 요청값 규칙을 이용할 수 없음.
# 그렇기 때문에 직접 검색결과 아래에 있는 페이지 버튼을 클릭하며 데이터를 수집해줘야 함.

from selenium import webdriver
import time

##1. 웹드라이버 켜기
driver = webdriver.Chrome("./chromedriver")

##2. 네이버 지도 접속하기 (url창에 입력)
driver.get("https://v4.map.naver.com/")
# 네이버 지도 업데이트 후 안내메시지 끄기
driver.find_elements_by_css_selector("button.btn_close")[1].click()

##3. 검색창에 검색어 입력하기 // 검색창: input#search-input
search_box = driver.find_element_by_css_selector("input#search-input")
search_box.send_keys("오골계")

##4. 검색버튼 누르기 // 검색버튼: button.spm
search_button = driver.find_element_by_css_selector("button.spm")
search_button.click()

##5. 검색 결과 확인하기(반복문)
for n in range(1, 20):            # 여기서 임시변수 n은 현재 페이지를 의미
    time.sleep(1)                 # 지연시간 주기
    # 컨테이너: dl.lsnx_det
    stores = driver.find_elements_by_css_selector("dl.lsnx_det")

    for s in stores:
        name = s.find_element_by_css_selector("dt > a").text
        addr = s.find_element_by_css_selector("dd.addr").text

        # 전화번호가 없는 경우 에러처리
        try :                         # selenium에서 전화번호(dd.tel)을 찾을 수 없기 때문에 no such element(그런 데이터 없어!) 에러 발생
            tel = s.find_element_by_css_selector("dd.tel").text
        except:
            tel = "전화번호 없음"

        # 가게 이름: dt > a
        # 가게 주소: dd.addr
        # 전화번호: dd.tel

        print(name, '/', addr, '/', tel)

    # 페이지 버튼의 룰을 찾아야하는데 페이지 버튼의 코드는 <a>와 <strong>이 섞여 있기 때문에 쉽게 룰을 찾을 수 없음.
    # selenium의 find_elements_by_css_selector()함수를 사용하면 모든 버튼을 리스트 형태로 저장할 수 있음.
    page_bar = driver.find_elements_by_css_selector('div.paginate > *')          # div.paginate 아래에 있는 모든 태그를 선택해주세요!

    # 다음 페이지가 없는 경우 에러처리
    try:
        # 현재 페이지(n)가 5의 배수가 아닌 경우 n%5+1 페이지 버튼 클릭
        if n % 5 != 0:
            page_bar[n%5+1].click()
        # 현재 페이지(n)가 5의 배수인 경우 다음페이지 버튼을 클릭
        else:
            page_bar[6].click()
    except:             # 페이지가 선택되지 않은 경우
        print("수집완료")
        break

## 문제: "수집완료" 안뜸 -> 데이터가 반복되어 수집됨.
