#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import sys
import re
import mimetypes
import time
import argparse
from urllib.parse import urlparse
import os
from http.cookiejar import LWPCookieJar
requests.packages.urllib3.disable_warnings()
import subprocess

# Needs to get changed every week or month or two
INSTANCE = "gogoanime.hu"
DOWNLOADER = "yt-dlp"
# Put in here mpv ok
PLAYER = "mpv"
COMMAND = ['fzf', '--reverse']
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; 5060 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"
}
def get_arguments():
 
    parser = argparse.ArgumentParser(description='GOGOanime downloader')
 
    parser.add_argument('-s', '--search', type=str, metavar='KEYWORD', help='Search Term')
    parser.add_argument('-n', '--filename', type=str, metavar='FILENAME', help='File Naming Convention')
    parser.add_argument('-p', '--player', action="store_true", default=False, help='Play with player')
    parser.add_argument('link', nargs="?", type=str, metavar='URL', help='GOGO link')
 
    args = parser.parse_args()
 
    return args

def fetch(url):
    request = requests.get(url)
    if request.status_code != 200:
        sys.exit(f"Could not get {url}")
    else:
        return request.text

def search(keyword):
    search_url = f"https://{INSTANCE}/search.html?keyword={keyword}"
    data = fetch(search_url)

    soup = BeautifulSoup(data, "html.parser")
    # Grab all pages
    pages = soup.find("ul", {"class": "pagination-list"})
    if pages:
        # How to get href's
        # https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
        # How to make for loop to list
        # https://www.youtube.com/watch?v=kNTveFsQVHY
        pagination = [f"https://{INSTANCE}/{x['href']}" for x in pages.find_all(href=True)]
    else:
        pagination = [search_url]
    search_data = []
    for page in pagination:
        data = fetch(page)
        soup = BeautifulSoup(data, "html.parser")
        items = soup.find("ul", {"class": "items"}).find_all("div", {"class": "img"})
        for num, img_data in enumerate(items):
            metadata = img_data.find("a")
            title = metadata['title']
            link = metadata['href']
            image = metadata.find("img")['src']
            search_data.append({
                "name": f"{num+1}: {title}",
                "title": title,
                "link": f"https://{INSTANCE}{link}",
                "image": image,
                "alias": link.split("/")[-1]
            })
    return search_data

def episode_list(name):
    #pagaste: https://github.com/justfoolingaround/animdl/blob/master/animdl/core/codebase/providers/gogoanime/__init__.py
    page = fetch(f"https://{INSTANCE}/category/{name}")
    soup = BeautifulSoup(page, 'html.parser')
    id = soup.find("input", {"class": "movie_id"})['value'].zfill(2)

    gogoanime = fetch(f"https://ajax.gogo-load.com/ajax/load-list-episode?ep_start=0&ep_end=10000000&id={id}&default_ep=0&alias={name}")
    soup = BeautifulSoup(gogoanime, 'html.parser')
    episodes = soup.find_all("li")
    data = []
    for episode in episodes:
        number = int(episode.find('div', attrs={'class':'name'}).text.split(" ")[-1])
        link = f"https://{INSTANCE}"+episode.find('a')['href'][1:]
        data.append({
            "number": str(number),
            "link": link
        })
    return data

def fzf(data, key):
    titles = '\n'.join([x[key] for x in data])
    p = subprocess.run(COMMAND, input=titles, capture_output=True, text=True)
    if p.stdout == "":
        sys.exit("Please select something.")
    else:
        try:
            index = int(p.stdout) - 1
        except:
            index = int(p.stdout.split("\n")[0].split(":")[0]) - 1
        return data[index]

def scrape(url):
    print(url)
    data = fetch(url)

    soup = BeautifulSoup(data, "html.parser")
    # I wish I could get season number or something
    title = soup.find("div", {"class": "title_name"}).h2.text[:-1]
    episode = soup.find("input", {"class": "default_ep"})['value'].zfill(2)
    iframe = soup.find("iframe")['src']
    if urlparse(iframe).netloc == "ww.9anime2.com":
        return {"response": iframe, "title": title}
    print(iframe)
    data = fetch(iframe)

    links = soup.find("div", {"class": "anime_muti_link"}).find_all("a")
    for li in links:
        video = li['data-video']
        print(video)
        host = urlparse(video).netloc
        # For now yt-dlp has support for mp4upload
        if host == "www.mp4upload.com":
            request = video
            # This code is so dogwater I didn't even make it
            #url = video
            #vid_id = url.split(".html")[0].split("embed-")[1].split("/")[-1]
    
            #headers = {'referer': "https://mp4upload.com"}
            #data = {
            #    'op': 'download2',
            #    'id': vid_id,
            #    'rand': '',
            #    'referer': 'https://mp4upload.com/',
            #    'method_free': '',
            #    'method_premium': ''
            #}
            #request = requests.post(url, headers=headers, data=data, stream=True, verify=False)
        elif host == "fembed9hd.com":
            id = video.split("/")[-1]
            raw = requests.post("https://layarkacaxxi.icu/api/source/"+id).json()
            url = raw["data"][len(raw["data"]) - 1]["file"]
            session = requests.Session()
            session.headers["User-Agent"] = HEADERS["User-Agent"]
            session.cookies = LWPCookieJar()
            head = session.head(url)
            request = head.headers.get("Location", url)
    return {
        "title": title,
        "response": request,
        "episode": episode
    }

def download(response, title, play=False):
    invalid = '<>:"/\|?*'
    for char in invalid:
        title = title.replace(char, '')
    if type(response) == str:
        if play == True:
            os.system(f"{PLAYER} --title=\"{title}\" {response}")
        else:
            os.system(f"{DOWNLOADER} {response} -o \"{title}.%(ext)s\"")
        return
    extension = mimetypes.guess_all_extensions(response.headers['Content-Type'], strict=False)[0]
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
        data = scrape(args.link)
    elif args.search:
        selection = fzf(episode_list(fzf(search(args.search), "name")["alias"]), "number")
        data = scrape(selection["link"])
    if args.filename:
        title = args.filename % data
    else:
        title = data["title"]
    print(data)
    print(title)
    if args.player:
        download(data["response"], title, True)
    else:
        download(data["response"], title)

if __name__ == "__main__":
    main()
