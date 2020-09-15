## stage1: 정적페이지와 동적페이지 구분 ##
## requests로 수집할 수 없는 페이지

import requests
from bs4 import BeautifulSoup
raw = requests.get("https://v4.map.naver.com/", headers = {"User-Agent": "Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')

# 컨테이너: dl.lsnx_det
stores = html.select("dl.lsnx_det")
print(stores)          # 데이터가 수집되지 않음
print(len(stores))     # 0이 나옴

# 네이버 지도 페이지는 우리가 지금까지 수집해온 페이지(네이버TV, 네이버뉴스, 네이버영화 등)와 다른 방식으로 구성된 페이지이기 때문
# 즉, 동적페이지이므로 requests로는 데이터 수집이 안됨.

# 정적(Static)페이지: 네이버 뉴스 검색결과처럼 URL에 따라 정해진 페이지를 불러오는 것
# 동적(dynamic)페이지: 네이버 지도처럼 URL에 관계없이 웹페이지 위에서 데이터를 불러오는 방법을 사용하는 것

# 가게 이름:
# 가게 주소:
# 전화번호:


# 셀레니움: 크롬, 사파리, 파이어폭스 등 웹브라우저를 자동으로 제어할 수 있는 파이썬 오픈소스 패키지 -> 웹페이지에서 접속해서 할 수 있는 거의 모든 일을 할 수 있음.
