#!/usr/bin/env python
import requests
import argparse
import html
import os
import tempfile
from datetime import datetime, timezone
import time
import re
import sys
import urllib.parse
import random

VIEWER = "imcat"
INSTANCE = "https://chan.getgle.org/"

def parse_arguments():
    parser = argparse.ArgumentParser(description='Terminal fchannel client')
    parser.add_argument('-b', '--board', type=str, metavar='BOARD', help='Select a board to view e.g. "g"')
    parser.add_argument('-t', '--thread', type=str, metavar='BOARD/THREAD', help='Select a thread to view e.g. "g"')
    parser.add_argument('-p', '--page', type=int, metavar='NUMBER', help='Go to a certain page number in board.')
    parser.add_argument('-l', '--list', action="store_true", default=False, help='List boards')
    parser.add_argument('-li', '--list-instances', action="store_true", default=False, help='List boards')
    return parser.parse_args()

def list_instances():
    data = requests.get("https://fchannel.org/instance-index.html").text
    links = re.findall("<a href=\".+?\">", data)
    working = []
    for link in links:
        link = link.replace("<a href=","").replace('"',"").replace(">","")
        if not link.endswith(".onion"):
            working.append(link)
    return working

def content(stuff):
    com = html.unescape(stuff).replace("<br>","\n")
    cleaner = re.compile('<.*?>')
    com = re.sub(cleaner, '', com)
    return com

def list_boards():
    data = requests.get("https://chan.getgle.org/following").json()
    items = []
    for item in data["items"]:
        items.append(item["id"].split("/")[-1])
    return '\n'.join(items)

def board_error(board):
    args = parse_arguments()
    if board not in list_boards():
        print("ERROR: Can't find this board do -l/--list for a list of boards")
        sys.exit(1)

def title(stuff):
    date = datetime.strptime(stuff['published'], "%Y-%m-%dT%H:%M:%S.%fZ")
    date = date.replace(tzinfo=timezone.utc).astimezone(tz=None)
    date = date.strftime("%m/%d/%y(%a)%H:%M:%S")
    title = f"{date} No. {stuff['id'].split('/')[-1]}"
    if "attributedTo" in stuff:
        title = f"{stuff['attributedTo']} {title}"
    else:
        title = f"Anonymous {title}"
    if "name" in stuff:
        title = f"{stuff['name']} {title}"
    return title

def image(stuff):
    if stuff["name"] != "":
        file = os.path.join(tempfile.gettempdir(),stuff["name"])
        with open(file,"wb") as f:
            f.write(requests.get(stuff["href"]).content)
        os.system(f'{VIEWER} "{file}"')
        print(stuff["href"])

def main():
    args = parse_arguments()
    if args.list:
        print(list_boards())

    elif args.list_instances:
        print(list_instances())
    elif args.board:
        board_error(args.board)
        url = urllib.parse.urljoin(INSTANCE, args.board+"/outbox")
        data = requests.get(url).json()
        for i, thread in enumerate(data["orderedItems"]):
            print(title(thread))
            print(thread["content"])

            image(thread["attachment"][0])

            if 'orderedItems' in thread['replies']:
                for reply in thread['replies']['orderedItems']:
                    print("\n    "+title(reply))
                    for thing in reply['content'].splitlines():
                        print("     "+thing)
            if i == 0:
                input("Press ENTER for next post:")
            else:
                input(":")

    if args.thread:
        instances = '\n'.join(list_instances())
        result = urllib.parse.urlparse(args.thread)
        isit = all([result.scheme, result.netloc])
        if isit == False:
            print("This is not a valid url.")
            sys.exit(1)
        data = requests.get(args.thread, headers={"Accept": "application/ld+json"})
        status = data.status_code
        url = urllib.parse.urlparse(args.thread)
        url = url.scheme+"://"+url.netloc
        url = url[:-1] if url[-1] == '/' else url
        if url not in list_instances():
            print(f"""Couldn't get this thread try to get a thread from one of these instances
{instances}""")
            sys.exit(1)
        data = data.json()["orderedItems"][0]

        print(title(data))

        print(data['content'])
        print(image(data["attachment"][0]))
        for i, reply in enumerate(data["replies"]["orderedItems"]):
            print(f"\n    {title(reply)}")
            for thing in content(reply['content']).splitlines():
                print("     "+thing)

if __name__ == '__main__':
    main()
