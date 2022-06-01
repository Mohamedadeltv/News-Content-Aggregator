from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup as BSoup, BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://egyptianstreets.com/category/news-politics-and-society/")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')
toi_headings = toi_soup.findAll("div", {"class": "widget-full-list-text left relative"})
toi_headings = toi_headings[2:]
toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

# Getting news from Hindustan times


ht_r = requests.get("https://www.egypttoday.com/Section/News/1")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "BOrderBoxSection"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)


def index3(req):
    return render(req,'news/index3.html')
def index(req):
    return render(req, 'news/index.html', {'toi_news': toi_news, 'ht_news': ht_news})


toi_r2 = requests.get("https://egyptianstreets.com/category/arts-culture/")
toi_soup2 = BeautifulSoup(toi_r2.content, 'html5lib')
toi_headings2 = toi_soup2.findAll("div", {"class": "widget-full-list-text left relative"})
toi_headings2 = toi_headings2[2:]
toi_news2 = []

for th2 in toi_headings2:
    toi_news2.append(th2.text)

ht_r2 = requests.get("https://www.egypttoday.com/Section/Arts-Culture/4")
ht_soup2 = BeautifulSoup(ht_r2.content, 'html5lib')
ht_headings2 = ht_soup2.findAll("div", {"class": "BOrderBoxSection"})
ht_headings2 = ht_headings2[2:]
ht_news2 = []

for hth2 in ht_headings2:
    ht_news2.append(hth2.text)


def index2(req):
    return render(req, 'news/index2.html', {'toi_news2': toi_news2, 'ht_news2': ht_news2})
