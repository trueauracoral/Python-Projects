#!/usr/bin/env python

from flask import Flask
import requests
import datetime
import re
import json

error_message = 'Uh oh, could not connect to urban dictionary api'

def api():
    data = requests.get("https://www.pokemon.com/api/1/us/news/get-news.json")
    if data.status_code == 200:
        return data.json()
    else:
        return error_message
#    for article in data:
#        print(f"""<item>
#    <title>{article['title']}</title>
#    <link>{"https://pokemon.com"+article['url']}</link>
#    <pubdate>{datetime.datetime.strptime(article['date'], '%B %d, %Y').strftime('%a, %d %b %Y')}</pubdate>
#    <description><![CDATA[<img src="https://pokemon.com{article['image']}" alt="{article['alt']}">
#{article['shortDescription']}]]></description>
#</item>""")


app = Flask(__name__)

@app.route('/')
def home():
    data = api()
    if data == error_message:
        return error_message
    text = ""
    for article in data:
        text = text + f"""
<div class='{article['id']}'>
<p>{article['date']}</p>
<h1><a href='{article['url']}'>{article['title']}</a></h1>
<img src='https://pokemon.com{article['image']}' alt='{article['alt']}'>

<p>{article['shortDescription']}</p>
</div>
<hr>
"""
    return text

@app.route('/us/pokemon-news/<url>')
def article(url):
    data = requests.get("https://www.pokemon.com/us/pokemon-news/"+url).text
    with open("index.html", "w") as f:
        f.write(data)
    find = json.loads(re.findall('<script type="application/ld\+json">((.|\n)*?)</script>', data)[0][0])["articleBody"]
    return find

if __name__ == '__main__':
    app.run(port=80)
