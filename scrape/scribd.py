#!/usr/bin/env python
# FORK OF: https://github.com/vaginessa/Scribd-Downloader/
# Python 2 to Python 3 and making it work for my usecase
from bs4 import BeautifulSoup
import requests
import sys
import re
import os

response = requests.request(method='GET', url=sys.argv[1])
with open("index.html", "w", encoding="utf-8") as f:
    f.write(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
extraction = ''
train = 1

title = soup.find("div", {"class": "auto__app_page_body_metadata_original_title data_row original_title inline"}).get_text().split(":")[1].replace("&", "").replace("_","")

js_text = soup.find('script', type='text/javascript')
print(js_text)
for opening in js_text:
    for inner_opening in opening:
        urls = re.findall("contentUrl\: \"(.*?)\"", inner_opening)
        if not urls == '':
            for url in urls:
                replacement = url.replace('/pages/', '/images/').replace('jsonp', 'jpg')
                print(replacement)
                #print replacement
                print('Downloading page ' + str(train))
                #response = requests.get(replacement, stream=True)
                #with open(str(train) + '.jpg', 'wb') as out_file:
                #    out_file.write(response.content)
                train+=1
