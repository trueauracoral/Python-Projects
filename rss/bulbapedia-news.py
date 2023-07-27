#!/usr/bin/env python

# Script for bulbapedia RSS in rssguard
# Post processing:
# https://bulbagarden.net
import requests
import re
import json
import sys
from datetime import datetime
from bs4 import BeautifulSoup

sys.stdin.reconfigure(encoding="utf-8")

input_data = sys.stdin.read()

soup = BeautifulSoup(input_data, "html.parser")
articles = soup.find("div", class_="news-article-list")
articles = articles.find_all("article", {"class": "news-article-card"})

items = []
for article in articles:
    date = article.find("div", {"class": "news-article-card-date"}).text
    date = datetime.strptime(date, "%b%d").isoformat()
    title = article.find("h2", {"class": "news-article-card-title"}).text
    thumbnail = article.find("a", {"class": "news-article-card-thumbnail"})
    url = thumbnail.get("href")
    image = thumbnail.find("img").get("src")
    description = article.find("div", {"class": "news-article-card-excerpt news-content"}).text
    author = article.find("li", {"class": "news-meta-item author"}).find("a").text.replace("\n", "")
    html = f"""
<img src='{image}'>
<p>{description}</p>
"""
    item = {
        "author": {"name": author},
        "title": title,
        "id": url,
        "content_html": html,
        "url": url,
        "date_published": date
    }
    items.append(item)
json_feed = {
  "title": "Pokemon News",
  "items": items
}
print(json.dumps(json_feed))
