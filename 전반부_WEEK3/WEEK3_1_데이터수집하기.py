'''
import requests         # 패키지 사용할때 색깔 변함. 활성화
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r/")      # get은 requests안의 함수
#print(raw)            # <Response [200]>: 데이터 잘 가지고 왔음    <Response [404]>: 페이지 잘못 가져왔을때 에러
#print(raw.text)       #홈페이지의 소스코드 버전으로 보고 싶을때
#print(raw.elapsed)    #데이터 요청시 소요시간
html = BeautifulSoup(raw.text, 'html.parser')
#print(html)
#get함수를 통해 가져온 소스코드는 단순한 문자열에 불과함. HTML파싱을 해줘야 소스코드로 인식하므로, 소스코드를 태그별로 구분하고 선택자를 활용하여 원하는 데이터를 찾을 수 있음.

## 네이버티비 인기영상 1~3위
# 1~3위 컨테이너: div.inner
# 제목: dt.title
# 채널명: dd.chn
# 재생수: span.hit
# 좋아요수: span.like

# 데이터 수집 단계: 1) 컨테이너 수집 2) 영상별 데이터 수집 3) 수집반복

#1. 컨테이너 수집
container = html.select("div.inner")
# print(container)        # 리스트 안으로 저장됨.
# print(container[0])

#2. 영상 데이터 수집(첫번째 영상)
title = container[0].select_one("dt.title")      #select: indexing 필요,  select_one : 한 컨테이너 안에 제목은 하나밖에 없으므로 하나만 가져와.
# print(title)   #텍스트만 원해도 태그까지 포함돼서 나옴.
#print(title.text)   #텍스트 데이터만 나옴.

chn = container[0].select_one("dd.chn")
hit = container[0].select_one("span.hit")
like = container[0].select_one("span.like")
print(title.text.strip())   #strip()은 공백은 제거하는 함수
print(chn.text.strip())
print(hit.text.strip())
print(like.text.strip())

#3. 반복하기 
#for문 사용해주기

'''



# 정리하면,

import requests
from bs4 import BeautifulSoup

raw = requests.get("https://tv.naver.com/r/")
html = BeautifulSoup(raw.text, 'html.parser')

container = html.select("div.inner")

for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")

    print(title.text.strip())
    print(chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)