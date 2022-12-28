#!/usr/bin/env python

from flask import Flask, render_template
import requests
import datetime
import re
import json

ERRROR_MESSAGE = 'Uh oh, could not connect to urban dictionary api'
DEFINE = "https://api.urbandictionary.com/v0/define?term="
RANDOM = "https://api.urbandictionary.com/v0/random"

def api(url, arg=None):
    if arg == None:
        data = requests.get(url)
    else:
        data = requests.get(f"{url}{arg}")
    
    if data.status_code == 200:
        data = data.json()["list"]
        text = ""
        for word in data:
            text += f'''
<div class="{word["defid"]}">
<h2>{word["word"]}</h2>
<p>{word["definition"]}</p>
<p>by {word["author"]} {word["written_on"]}</p>
</div>
'''
        return text
    else:
        return ERRROR_MESSAGE

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template('index.html', text=api(RANDOM))

@app.route('/us/pokemon-news/<url>')
def article(url):
    data = requests.get("https://www.pokemon.com/us/pokemon-news/"+url).text
    with open("index.html", "w") as f:
        f.write(data)
    find = json.loads(re.findall('<script type="application/ld\+json">((.|\n)*?)</script>', data)[0][0])["articleBody"]
    return find

if __name__ == '__main__':
    app.run(port=80)
