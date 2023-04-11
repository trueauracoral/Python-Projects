#!/usr/bin/env python
import re
import requests
import sys

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Goanna/6.0 Firefox/102.0 PaleMoon/32.0.1",
    'Host': "tapas.io",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "qzip, deflate, br",
}
def request(url, jsonify=False, headers=False):
    if headers == False:
        r = requests.get(url)
    else:
        r = requests.get(url, headers=headers)
    
    if not r.ok:
        sys.exit("Could not request url")

    if jsonify == False:
        return r.text
    elif jsonify == True:
        return r.json()

data = request("https://tapas.io/series/Theodd1sout/info", headers=headers)
id = re.findall("tapastic\:\/\/series\/(.*?)\/info", data)[1]
data = request("https://tapas.io/series/2791/episodes?page=1&sort=OLDEST&max_limit=99999999")
print(id)
