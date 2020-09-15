#다음 뉴스기사 수집하기
# 1~3페이지

# 컨테이너: ul#clusterResultUL li
# 제목:a.f_link_b
# 기사 요약: p.f_eb.desc

import requests
from bs4 import BeautifulSoup

for i in range(1,4) :
    raw = requests.get("https://search.daum.net/search?w=news&q=%EC%BD%94%EC%95%8C%EB%9D%BC&DA=PGD&spacing=0&p="+str(i))
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("ul#clusterResultUL li")     #모범답안: div.wrap_cont

    for ar in articles:
        title = ar.select_one("a.f_link_b").text
        summary = ar.select_one("p.f_eb.desc").text
        print(title, "\n", summary)
        print("=" * 100)
