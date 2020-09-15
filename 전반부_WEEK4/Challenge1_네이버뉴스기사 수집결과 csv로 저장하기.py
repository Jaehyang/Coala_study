import requests
from bs4 import BeautifulSoup

f = open("navernews.csv", "w")
f.write("제목, 언론사\n")        #헤더 넣어주기

page = 1
for page in range(1, 100, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&query=코알라&start="+str(page),
                       headers={"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: ul.type01 > li
    # 기사제목: a._sp_each_title
    # 언론사: span._sp_each_source
    articles = html.select("ul.type01 > li")
    for ar in articles:
        title = ar.select_one("a._sp_each_title").text
        source = ar.select_one("span._sp_each_source").text
        print(title, source)

        title = title.replace(",", "")        # 제목(title)과 언론사(source)에 ,가 포함되어있는 경우 데이터가 구분될 수 있으므로 ,를 삭제
        source = source.replace(",", "")

        f.write(title + "," + source + "\n")      # 제목(title)과 언론사(source)를 ,로 구분하여 써주기
f.close()
