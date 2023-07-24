#!/usr/bin/env python
import requests
import re
import urllib.parse
import datetime

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1', "Content-Type": "text/html;charset=UTF-8"}

def scrape():
    data = requests.get("https://www.pokemon.com/us/pokemon-news", headers=HEADERS).text
    #with open("index.html", "w") as f:
        #f.write(data)

    dates = re.findall('<p class="date">(.*?)</p>', data)
    titles = re.findall("<h3>(.*?)</h3>", data)[2:]
    descriptions = re.findall('<p>|<p class="hidden-mobile">(.*?)</p>', data)
    descriptions = [x for x in descriptions if x]
    linkers = re.findall(f'<a href="(.*?)">', data)
    links = []
    images = re.findall(f'<img src="/static-assets(.*?)"',data)[2:]
    for link in linkers:
        if 'rel="" ' in link:
            pass
        elif "?article" in link:
            pass
        elif link.startswith(("/us/pokemon-news/","/us/strategy/")):
            links.append(link)
    links = links[2:]

    for (desc, title, date, link, image) in zip(descriptions, titles, dates, links, images):
        print(f"""<item>
    <title>{title}</title>
    <link>{"https://pokemon.com/"+link}</link>
    <pubdate>{datetime.datetime.strptime(date, '%B %d, %Y').strftime('%a, %d %b %Y')}</pubdate>
    <description><![CDATA[<img src="https://pokemon.com/static-assets/{image}" alt="{title}">
{desc}]]></description>
</item>""")

def api():
    data = requests.get("https://www.pokemon.com/api/1/us/news/get-news.json").json()
    for article in data:
        print(f"""<item>
    <title>{article['title']}</title>
    <link>{"https://pokemon.com"+article['url']}</link>
    <pubdate>{datetime.datetime.strptime(article['date'], '%B %d, %Y').strftime('%a, %d %b %Y')}</pubdate>
    <description><![CDATA[<img src="https://pokemon.com{article['image']}" alt="{article['alt']}">
{article['shortDescription']}]]></description>
</item>""")

if __name__ == "__main__":
    print('''<rss version="2.0">
<channel>
<title>Pokemon News</title>
<link>https://www.pokemon.com/us/pokemon-news/</link>
<description>RSS for Pokemon News articles</description>
''')

    api()

    print("""
</channel>
</rss>""")
