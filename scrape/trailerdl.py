#!/usr/bin/env python

import requests
import re
import json
from urllib.parse import urljoin, urlparse
import sys
import mimetypes
import time
import argparse

def get_arguments():
 
    parser = argparse.ArgumentParser(description='IMDB trailer downloader')
 
    parser.add_argument('link', type=str, metavar='URL', help='IMDB link')
    #parser.add_argument('-r', '--random', action="store_true", default=False, help='Copy the link to the pasted file')
 
    args = parser.parse_args()
 
    return args

def get_data(imdb_link):
    # Clean out ?ref_=nv_sr_srsg_0 nonsense if it's there
    imdb_link = urljoin(imdb_link, urlparse(imdb_link).path)
    # Found form over here: https://regex101.com/library/uO6fZ6
    # somehow in the future I want to detect imdb id's and libremdb
    # links
    pattern = re.compile("^(?:http:\/\/|https:\/\/)?(?:www\.)?(?:imdb.com\/title\/)?(tt[0-9]*)(.+?)")
    if not re.fullmatch(pattern, imdb_link):
        sys.exit("Invalid imdb link")
    request = requests.get(imdb_link)
    #with open("index.html", "w", encoding="utf-8") as f:
    #    f.write(request.text)
    if request.status_code != 200:
        sys.exit(f"Could not connect to {imdb_link}")
    # This is a json data goldmine I found when looking for a
    # trailer imdb_link... Could be used for a lot of other things.
    data = json.loads(re.findall('<script id="__NEXT_DATA__" type="application/json">(.*?)</script>', request.text)[0])
    try:
        trailer_imdb_link = data["props"]["pageProps"]["aboveTheFoldData"]["primaryVideos"]["edges"][0]["node"]["playbackURLs"][0]["url"]
        title = data["props"]["pageProps"]["aboveTheFoldData"]["titleText"]["text"]
        imdb_id = data["query"]["tconst"]
    except Exception:
        sys.exit("Something went wrong... Couldn't find the trailer.")
    #print(data)
    return {"link": trailer_imdb_link, "title": title, "id": imdb_id}


def download(link):
    data = get_data(link)
    response = requests.get(data["link"], stream= True)
    extension = mimetypes.guess_all_extensions(response.headers['Content-Type'], strict=False)[0]
    title = data["title"]
    invalid = '<>:"/\|?*'
    for char in invalid:
        title = title.replace(char, '')
    filename = f'{title} [{data["id"]}]{extension}'
    print(f"[download] Destination: {filename}")
    with open(filename, 'wb') as f:
        total = int(response.headers.get('content-length'))
        megabytes = f"{round(float(total) / 1024, 1)}MiB"

        if total is None:
            f.write(response.content)
            return

        downloaded = 0
        st = time.time()
        for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
            downloaded += len(data)
            f.write(data)
            et = str(time.strftime("%H:%M:%S", time.gmtime(time.time() - st)))
            sys.stdout.write(f'\r[download] {round((downloaded / total) * 100)}% of {megabytes} in {et}')
            sys.stdout.flush()
    sys.stdout.write('\n')
 

def main():
    args = get_arguments()
    if args.link:
        download(args.link)

if __name__ == "__main__":
    main()
