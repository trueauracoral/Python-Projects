#!/usr/bin/env python
import subprocess
import os
import json
import multiprocessing
import argparse
import urllib.parse

LIBRARIAN_INSTANCE = "https://lbry.ix.tc/"
def get_arguments():
    parser = argparse.ArgumentParser(description='LBRY RSS generator')
    parser.add_argument('-o', '--odysee', action="store_true", default=False, help='Odysee RSS')
    parser.add_argument('-l', '--librarian', action="store_true", default=False, help='Librarian RSS')
    parser.add_argument('-m', '--melroy', action="store_true", default=False, help='Melroy RSS')
    return parser.parse_args()


def lbry_start():
    startnow = subprocess.Popen("lbrynet start", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

dot = "."
def get():
    data = subprocess.getoutput("lbrynet preference get")
    while True:
        if data == "Could not connect to daemon. Are you sure it's running?":
            dot += "."
            print(dot)
        else:
            data = subprocess.getoutput("lbrynet preference get")
            return json.loads(data)

def rss(start, end):
    data = get()
    channels = []
    for channel in data["shared"]["value"]["subscriptions"]:
        channel = channel.split("#")[0].replace("lbry://","",1)
        channels.append(urllib.parse.urljoin(start, channel+end))
    return '\n'.join(channels)


def main():
    args = get_arguments()
    if args.odysee:
        print(rss("https://odysee.com/$/rss/",""))
    if args.librarian:
        print(rss(LIBRARIAN_INSTANCE, "/rss"))
    if args.melroy:
        print(rss("https://lbryfeed.melroy.org/channel", ""))
if __name__ == '__main__':
    p1 = multiprocessing.Process(name='p1', target=lbry_start)
    p = multiprocessing.Process(name='p', target=get)
    p1.start()
    p.start()
    main()
