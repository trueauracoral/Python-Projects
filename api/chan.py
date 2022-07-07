#!/usr/bin/env python
import requests
import argparse
import html
import os
import tempfile
import re

viewer = "imcat"

def parse_arguments():
    parser = argparse.ArgumentParser(description='Terminal 4chan client')
    parser.add_argument('-b', '--board', type=str, metavar='BOARD', help='Select a board to view e.g. "g"')
    parser.add_argument('-p', '--page', type=int, metavar='NUMBER', help='Go to a certain page number in board.')
    parser.add_argument('-l', '--list', action="store_true", default=False, help='List boards')
    return parser.parse_args()

def main():
    args = parse_arguments()
    if args.list:
        for board in requests.get("https://a.4cdn.org/boards.json").json()["boards"]:
            print(f'{board["board"]} - {board["title"]}')
            print(html.unescape(board["meta_description"]))

    elif args.board:
        def content(stuff):
            com = html.unescape(stuff).replace("<br>","\n")
            cleaner = re.compile('<.*?>')
            com = re.sub(cleaner, '', com)
            return com

        data = requests.get(f"https://a.4cdn.org/{args.board}/catalog.json").json()
        if args.page:
            if args.page >= 0 and args.page <= len(data):
                num = args.page
            else:
                print("ERROR: Too big page number, printing out the first page")
        else:
            num = 0
        for thread in data[0]["threads"]:
            print("---")
            title = f"{thread['name']} {thread['now']} No.{thread['no']}"
            if "sub" in thread:
                title = f"{html.unescape(thread['sub'])} | {title}"
            print(title)
            print(content(thread['com']))

            if thread["filename"] != "":
                file = os.path.join(tempfile.gettempdir(),thread["filename"]+thread["ext"])
                url = f"https://i.4cdn.org/{args.board}/{thread['tim']}{thread['ext']}"
                with open(file,"wb") as f:
                    f.write(requests.get(url).content)
                os.system(f'{viewer} "{file}"')
                print(url)
            if "last_replies" in thread:
                for reply in thread['last_replies']:
                    if "name" in reply:
                        print(f"\n    {reply['name']} {reply['now']} No.{reply['no']}")
                    if "com" in reply:
                        for thing in content(reply['com']).splitlines():
                            print("     "+thing)

if __name__ == '__main__':
    main()
