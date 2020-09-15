'''
## 복습문제 김윤서
import requests
from bs4 import BeautifulSoup

for i in range(1, 152, 50):
    raw = requests.get("https://www.melon.com/search/song/index.htm?q=%EC%82%AC%EB%9E%91&section=song&searchGnbYn=Y&kkoSpl=Y&kkoDpType=&ipath=srch_form#params%5Bq%5D=%25EC%2582%25AC%25EB%259E%2591&params%5Bsort%5D=hit&params%5Bsection%5D=song&params%5BsectionId%5D=&params%5BgenreDir%5D=&po=pageObj&startIndex="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    song = html.select("div.songTypeOne tbody tr")

    for sng in song:
        singer = sng.select_one("div#artistName span.checkEllipsisSongdefaultList").text.strip()
        title = sng.select_one("a.fc_gray").text.strip()
        print("{",singer,"-", title, "}")


#컨테이너: div.songTypeOne tbody tr
#가수: div.wrapArtistName   #모범답안: div#artistName span.checkEllipsisSongdefaultList
#제목: a.fc_gray


## 복습문제 박지연
import requests
from bs4 import BeautifulSoup

for i in range(1, 3):
    raw = requests.get("https://music.naver.com/chart/musicianLeague.nhn?duration=DAILY&page="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    music = html.select("tr._tracklist_move")

    for mus in music:
        ranking = mus.select_one("span.num").text.strip()
        title = mus.select_one("td.tb_name span.tit").text.strip()
        artist = mus.select_one("td.tb_artist span.tit").text.strip()
        print(ranking, "/", title, "/", artist)
#컨테이너:tr._tracklist_move
#순위: span.num
#곡명: td.tb_name span.tit
#아티스트: td.tb_artist span.tit


## 복습문제 성혜원

import requests
from bs4 import BeautifulSoup

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
for day in days:
    raw = requests.get("https://comic.naver.com/webtoon/weekdayList.nhn?week="+day, headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    webtoon = html.select("div.list_area li")

    for toon in webtoon:
        title = toon.select_one("ul.img_list dl>dt>a").text.strip()
        writer = toon.select_one("dd.desc > a").text.strip()
        print(title, "/", writer)

#컨테이너: div.list_area li
#제목: ul.img_list dl>dt>a
#작가이름: div.list_area dd.desc > a



## 복습문제 윤희준

import requests
from bs4 import BeautifulSoup

for i in range(1, 11):
    raw = requests.get("https://www.caltech.edu/about/news?p="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    article = html.select("div.article-teaser__info")

    for artcl in article:
        date = artcl.select_one("span.article-teaser__published-date__date").text.strip()
        title = artcl.select_one("div.article-teaser__title").text.strip()
        print(date, "/", title)

#컨테이너:div.article-teaser__info
#기사날짜:span.article-teaser__published-date__date
#제목: div.article-teaser__title

'''
## 복습문제 이미경

import requests
from bs4 import BeautifulSoup

for i in range(1, 52, 50):
    raw = requests.get("https://www.melon.com/new/index.htm#params%5BareaFlg%5D=I&po=pageObj&startIndex="+str(i), headers = {"User-Agent":"Mozilla/5.0"})
    html = BeautifulSoup(raw.text, 'html.parser')

    musics = html.select("div.wrap_song_info")

    for music in musics:
        title = music.select_one("div.ellipsis.rank01 span a").text.strip()
        singer = music.select_one("div.ellipsis.rank02 span a").text.strip()
        print(title, "/", singer)
#컨테이너: div.wrap_song_info
#제목: div.ellipsis.rank01
#가수: div.ellipsis.rank02
