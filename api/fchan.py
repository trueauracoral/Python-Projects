#!/usr/bin/env python
import requests
import argparse
import html
import os
import tempfile
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
    return parser.parse_args()

def get_random_instance():
    data = requests.get("https://fchannel.org/instance-index.html").text
    links = re.findall("<a href=\".+?\">", data)
    working = []
    for link in links:
        link = link.replace("<a href=","").replace('"',"").replace(">","")
        if not link.endswith(".onion"):
            working.append(link)
    return random.choice(working)

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
    title = f"{stuff['published']} No. {stuff['id'].split('/')[-1]}"
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
        if "/" in args.thread:
            board = args.thread.split("/")[0]
            thread = args.thread.split("/")[1]
        else:
            print("ERROR: Needs to be BOARD/THREAD")
            sys.exit(1)
        board_error(board)
        data = requests.get(f"https://a.4cdn.org/{board}/thread/{thread}.json").json()['posts']

        print(title(data[0]))

        if "com" in data[0]:
            print(content(data[0]['com']))
        image(data[0], board)
        for i, reply in enumerate(data[1:6]):
            if "name" and "com" in reply:
                print(f"\n    {reply['name']} {reply['now']} No.{reply['no']}")
                for thing in content(reply['com']).splitlines():
                    print("     "+thing)

if __name__ == '__main__':
    main()
