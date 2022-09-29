#!/usr/bin/env python
import requests
import re
import json
from urllib.parse import urljoin, urlparse
import sys

def get_link(link):
    # Clean out ?ref_=nv_sr_srsg_0 nonsense if it's there
    link = urljoin(link, urlparse(link).path)
    # Found form over here: https://regex101.com/library/uO6fZ6
    pattern = re.compile("^(?:http:\/\/|https:\/\/)?(?:www\.)?(?:imdb.com\/title\/)?(tt[0-9]*)(.+?)")
    if not re.fullmatch(pattern, link):
        sys.exit("Invalid Link")
    request = requests.get(link)
    #with open("index.html", "w", encoding="utf-8") as f:
    #    f.write(request.text)
    if request.status_code == 200:
        # This is a json data goldmine I found when looking for a
        # trailer link... Could be used for a lot of other things.
        data = json.loads(re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', request.text)[0])
        print(data)
        try:
            trailer_link = data["props"]["pageProps"]["aboveTheFoldData"]["primaryVideos"]["edges"][0]["node"]["playbackURLs"][0]["url"]
        except:
            sys.exit("Something went wrong... Couldn't find the trailer.")
        print(trailer_link)
    else:
        sys.exit(f"Could not connect to {link}")
get_link("https://www.imdb.com/title/tt0168366/?ref_=fn_al_tt_1")
