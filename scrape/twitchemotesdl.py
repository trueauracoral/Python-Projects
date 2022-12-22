#!/usr/bin/env python
import requests
import re
import sys
import mimetypes
import argparse 
def get_arguments():
    parser = argparse.ArgumentParser(description='IMDB trailer downloader')
    parser.add_argument('-c', '--channel', type=str, metavar='CHANNEL', help='Twitch channel with emotes')
    parser.add_argument('-g', '--general', action="store_true", default=False, help='Get general emotes')
    args = parser.parse_args()
    return args

def check(r):
    if r.status_code not in [200, 302]:
        sys.exit("Could not connect")

def scrape(r, imgRegex, titleRegex, titleRegex2='<br \/>(.*?)[\s]<\/center>'):
    findimg = re.findall(imgRegex, r)[1:]
    findtitle = re.findall(titleRegex, r)
    findtitle2 = re.findall(titleRegex2, r)
    findtitle = findtitle + findtitle2
    for i, result in enumerate(findimg):
        result = result.replace("2.0", "3.0").replace("1.0", "3.0")
        response = requests.get(result)
        try:
            ext = mimetypes.guess_all_extensions(response.headers["content-type"], strict=False)[0]
        except:
            ext = ".png"
        filename = findtitle[i].replace(":", "_").replace("/", "_").replace("\\", "_").replace("|", "_")+ext
        print(f"Downloading {filename}")
        with open(filename, 'wb') as f:
            f.write(response.content)

def main():
    args = get_arguments()
    if args.channel:
        headers = {
            "Host": "twitchemotes.com",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/   537.   36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://twitchemotes.com/channels/75508096",
            "Origin": "https://twitchemotes.com",
            "Connection": "keep-alive"
        }
        location = requests.post("https://twitchemotes.com/search/channel", allow_redirects=False, headers=headers, data={"query": args.channel, "source": "nav-bar"})
        check(location)
        location = location.headers["Location"]

        data = requests.get(f"https://twitchemotes.com{location}")
        check(data)
        scrape(data.text, '<img src="(.+?)"', '<br \/>(.*?)<\/center>')
    elif args.general:
        data = requests.get("https://twitchemotes.com")
        check(data)
        scrape(data.text, '<img src="(.+?)"', '</a>(.+?)</center>', "")

if __name__ == '__main__':
    main()