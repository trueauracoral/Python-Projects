#!/usr/bin/env python

from flask import Flask
import requests
import datetime
import re
import json

error_message = 'Uh oh, could not connect to pokemon tv api'

def api():
    data = requests.get("https://www.pokemon.com/api/pokemontv/v2/channels/us/")
    if data.status_code == 200:
        return data.json()
    else:
        return error_message

app = Flask(__name__)

@app.route('/')
def home():
    data = api()
    if data == error_message:
        return error_message
    text = "<div class='row' style='display:flex; flex-wrap: wrap; padding: 0 4px;'>\n"
    index = 0
    for i, channel in enumerate(data):
        stuff = [0, 5, 10, 15, 20, 25, 30]
        if (i in stuff) and (i != 30):
            index = index + 1
            print(i)
            text += "<div class='column' style='flex: 50%; padding: 0 4px;'>"
            for i in range(stuff[index]):
                text += f"""
<img style='margin-top: 8px; vertical-align: middle;' src='{channel['channel_images']['dashboard_image_1125_1500']}'>
"""
            text += "</div>"
    text += "</div>"
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
