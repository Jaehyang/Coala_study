#네이버tv 1~100위
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

container = html.select("div.cds")
for cont in container:
    title = cont.select_one("dt.title")
    chn = cont.select_one("dd.chn")
    hit = cont.select_one("span.hit")
    like = cont.select_one("span.like")
    print("제목:"+title.text.strip())
    print("채널명:"+chn.text.strip())
    print(hit.text.strip())
    print(like.text.strip())
    print("="*50)