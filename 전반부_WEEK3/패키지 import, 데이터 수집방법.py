import requests
from bs4 import BeautifulSoup

raw = requests.get("Url", headers = {"User-Agent":"Mozilla/5.0"})
html = BeautifulSoup(raw.text, 'html.parser')