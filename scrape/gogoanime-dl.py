#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys
import re
import mimetypes
import time
import argparse
requests.packages.urllib3.disable_warnings()

def get_arguments():
 
    parser = argparse.ArgumentParser(description='IMDB trailer downloader')
 
    parser.add_argument('link', type=str, metavar='URL', help='IMDB link')
    #parser.add_argument('-r', '--random', action="store_true", default=False, help='Copy the link to the pasted file')
 
    args = parser.parse_args()
 
    return args

url = "https://ww4.gogoanimes.org/watch/pokemon-2019-harukanaru-aoi-sora-episode-1"

def fetch(url):
    request = requests.get(url)
    if request.status_code != 200:
        sys.exit(f"Could not get {url}")
    else:
        return request.text

def mp4upload(url):
    data = fetch(url)

    soup = BeautifulSoup(data, "html.parser")
    title = soup.find("div", {"class": "title_name"}).h2.text[:-1]
    print(title)
    iframe = soup.find("iframe")['src']

    data = fetch(iframe)

    soup = BeautifulSoup(data, "html.parser")
    for li in soup.find_all("li"):
        video = li.get("data-video")
        if not video.startswith("https://"):
            continue
        elif "mp4upload.com" in video:
            url = video
        #print(video)

    vid_id = url.split(".html")[0].split("embed-")[1].split("/")[-1]

    headers = {'referer': "https://mp4upload.com"}
    data = {
        'op': 'download2',
        'id': vid_id,
        'rand': '',
        'referer': 'https://mp4upload.com/',
        'method_free': '',
        'method_premium': ''
    }
    request = requests.post(url, headers=headers, data=data, stream=True, verify=False)
    return {"title": title, "response": request}

def download(response, title):
    extension = mimetypes.guess_all_extensions(response.headers['Content-Type'], strict=False)[0]
    invalid = '<>:"/\|?*'
    for char in invalid:
        title = title.replace(char, '')
    filename = f'{title}{extension}'
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
        data = mp4upload(args.link)
        download(data["response"], data["title"])

if __name__ == "__main__":
    main()