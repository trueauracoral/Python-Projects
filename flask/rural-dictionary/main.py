#!/usr/bin/env python

from flask import Flask, render_template
import requests
from datetime import datetime, timezone
import re
import json
import sys

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
        defid = [word["defid"] for word in data]
        word = [word["word"] for word in data]
        definition = [re.sub('\[([^\]]*)\]', '<a href="/define.php?term=\1>\1</a>">', word["definition"]) for word in data]
        author = [word["author"] for word in data]
        written_on = [datetime.strptime(word["written_on"], "%Y-%m-%dT%H:%M:%S.%f%z").strftime("%B %d, %Y") for word in data]
        return {"defid": defid, "word": word, "definition": definition, "author": author, "written_on": written_on}
    else:
        return f"couldn't get data from the API\n{data.status_code}"

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    data = api(RANDOM)
    return render_template('index.html', data=zip(data["defid"], data["word"], data["definition"], data["author"], data["written_on"]))

if __name__ == '__main__':
    app.run(port=80)
