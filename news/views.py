from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://www.thenationalnews.com/mena/egypt/")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.findAll("div", {"class": "flex flex_direction_column custom-simple-text"})
toi_headings = toi_headings[2:]
toi_news = []


for th in toi_headings:
    toi_news.append(th.text)

#Getting news from Hindustan times


ht_r = requests.get("https://www.egypttoday.com/Section/News/1")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "BOrderBoxSection"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index(req):
    return render(req, 'news/index.html', {'toi_news':toi_news, 'ht_news': ht_news})