# Y-combinator news
#1~3 페이지 데이터 수집하기
import requests
from bs4 import BeautifulSoup

for i in range(1, 4) :
    raw = requests.get("https://news.ycombinator.com/news?p="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("tr.athing")

    for ar in articles :
        ranking = ar.select_one("span.rank").text
        title = ar.select_one("a.storylink").text

        print(ranking, title)