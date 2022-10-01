#!/usr/bin/env python
import requests
import re
import json
from urllib.parse import urljoin, urlparse
import sys
import time
import mimetypes

def get_data(imdb_link):
    # Clean out ?ref_=nv_sr_srsg_0 nonsense if it's there
    imdb_link = urljoin(imdb_link, urlparse(imdb_link).path)
    # Found form over here: https://regex101.com/library/uO6fZ6
    pattern = re.compile("^(?:http:\/\/|https:\/\/)?(?:www\.)?(?:imdb.com\/title\/)?(tt[0-9]*)(.+?)")
    if not re.fullmatch(pattern, imdb_link):
        sys.exit("Invalid imdb link")
    request = requests.get(imdb_link)
    #with open("index.html", "w", encoding="utf-8") as f:
    #    f.write(request.text)
    if request.status_code == 200:
        # This is a json data goldmine I found when looking for a
        # trailer imdb_link... Could be used for a lot of other things.
        data = json.loads(re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', request.text)[0])
        try:
            trailer_imdb_link = data["props"]["pageProps"]["aboveTheFoldData"]["primaryVideos"]["edges"][0]["node"]["playbackURLs"][0]["url"]
            title = data["props"]["pageProps"]["aboveTheFoldData"]["titleText"]["text"]
        except:
            sys.exit("Something went wrong... Couldn't find the trailer.")
        #print(data)
        return {"link": trailer_imdb_link, "title": title}
    else:
        sys.exit(f"Could not connect to {imdb_link}")

def download(link):
    data = get_data(link)
    response = requests.get(data["link"], stream= True)
    extension = mimetypes.guess_all_extensions(response.headers['Content-Type'], strict=False)[0]
    filename = data["title"]+extension
    print(filename)
    with open(filename, 'wb') as f:
        total = response.headers.get('content-length')
        megabytes = f"{round(float(total) / 1024, 2)}MiB"

        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                sys.stdout.write('\r[{}{}]'.format('#' * done, '.' * (50-done))+f" of {megabytes}")
                sys.stdout.flush()
    sys.stdout.write('\n')
 
download("https://www.imdb.com/title/tt0168366/?ref_=fn_al_tt_1")
