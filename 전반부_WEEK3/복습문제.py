import requests
from bs4 import BeautifulSoup
for i in range(0, 41,10) :
    raw = requests.get("http://www.ewha.ac.kr/ewha/news/movie.do?mode=list&&articleLimit=10&article.offset="+str(i), headers={"User-Agent": "Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    promovideo = html.select("div.b-box02")

    for pr in promovideo :
        title = pr.select_one("a.b-title").text.strip()
        summary = pr.select_one("div.b-text-box").text.strip()
        date = pr.select_one("li.b-date").text.strip()
        view = pr.select_one("li.b-hit").text.strip()
        print(title)
        print(summary)
        print(date, view)
        print("="*50)

