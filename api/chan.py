#!/usr/bin/env python
import requests
import argparse
import html
import os
import tempfile
import re
import sys

viewer = "imcat"

def parse_arguments():
    parser = argparse.ArgumentParser(description='Terminal 4chan client')
    parser.add_argument('-b', '--board', type=str, metavar='BOARD', help='Select a board to view e.g. "g"')
    parser.add_argument('-t', '--thread', type=str, metavar='BOARD/THREAD', help='Select a thread to view e.g. "g"')
    parser.add_argument('-p', '--page', type=int, metavar='NUMBER', help='Go to a certain page number in board.')
    parser.add_argument('-l', '--list', action="store_true", default=False, help='List boards')
    return parser.parse_args()

def content(stuff):
    com = html.unescape(stuff).replace("<br>","\n")
    cleaner = re.compile('<.*?>')
    com = re.sub(cleaner, '', com)
    return com

def list_boards():
    boards = []
    for board in requests.get("https://a.4cdn.org/boards.json").json()["boards"]:
        boards.append(board["board"])
    return boards

def board_error(board):
    args = parse_arguments()
    if board not in list_boards():
        print("ERROR: Can't find this board do -l/--list for a list of boards")
        sys.exit(1)

def title(stuff):
    title = f"{stuff['name']} {stuff['now']} No.{stuff['no']}"
    if "sub" in stuff:
        title = f"{html.unescape(stuff['sub'])} | {title}"
    return title

def image(stuff, board):
    if stuff["filename"] != "":
        file = os.path.join(tempfile.gettempdir(),stuff["filename"]+stuff["ext"])
        url = f"https://i.4cdn.org/{board}/{stuff['tim']}{stuff['ext']}"
        with open(file,"wb") as f:
            f.write(requests.get(url).content)
        os.system(f'{viewer} "{file}"')
        print(url)

def main():
    args = parse_arguments()
    if args.list:
        for board in requests.get("https://a.4cdn.org/boards.json").json()["boards"]:
            print(f'{board["board"]} - {board["title"]}')
            print(html.unescape(board["meta_description"]))

    elif args.board:
        board_error(args.board)
        data = requests.get(f"https://a.4cdn.org/{args.board}/catalog.json").json()
        if args.page:
            if args.page >= 0 and args.page <= len(data):
                num = args.page
            else:
                print("ERROR: Too big page number, printing out the first page")
        else:
            num = 0

        for i, thread in enumerate(data[num]["threads"]):
            print("---")
            print(title(thread))
            if "com" in thread:
                print(content(thread['com']))

            image(thread, args.board)

            if "last_replies" in thread:
                for reply in thread['last_replies']:
                    if "name" in reply:
                        print(f"\n    {reply['name']} {reply['now']} No.{reply['no']}")
                    if "com" in reply:
                        for thing in content(reply['com']).splitlines():
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
