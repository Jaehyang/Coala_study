## 네이버 급상승검색어
from selenium import webdriver
import time

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.naver.com/")
time.sleep(2)   # 시간 지연

#급상승 검색어 클릭
open_button = driver.find_element_by_css_selector("a.link_keyword")
open_button.click()

for i in range(1, 6):
    slider_box = driver.find_elements_by_css_selector("div.slider_box")
    for s in slider_box:
        slider_range = s.find_element_by_css_selector("a.range")
        slider_range.click()

    age = driver.find_element_by_css_selector("ul.list_age li:nth-of-type(2)")
    age.click()
    time.sleep(0.5)

button = driver.find_element_by_css_selector("button#NM_RTK_VIEW_set_btn")
button.click()
