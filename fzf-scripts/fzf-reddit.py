#!/usr/bin/env python
import subprocess
import requests
import tempfile
import html
import os
import datetime

SUBS = """r/archlinux
r/bash
r/commandline
r/emacs
r/freesoftware
r/linux
r/linux4noobs
r/linuxmasterrace
r/linuxquestions
r/suckless
r/Ubuntu
r/unixporn
r/vim"""

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
def fzf(data):
    file = tempfile.TemporaryFile().name
    with open(file, "w", encoding="utf-8") as f:
        f.write(data)
    choice = subprocess.getoutput(f"fzf --reverse < {file}")
    os.remove(file)
    return choice

def titles(sub):
    data = requests.get(f"https://reddit.com/{sub}.json",headers=HEADERS).json()
    names = []
    for i, name in enumerate(data["data"]["children"]):
        names.append(f"{i}. {html.unescape(name['data']['title'])}")
    return dict({"names": names, "data": data})

def content(data, post):
    data = data["data"]["children"][int(post.split(".")[0])]["data"]
    if data["selftext_html"] != None:
        text = data["url"]+"\n"+html.unescape(data['selftext'])
    else:
        text = data["url"]
                                              
    print(f"""Title: {data['title']}
Author: {data['author_fullname']}
Posted: {datetime.datetime.fromtimestamp(data['created_utc'])}

{text}""")

def main():
    sub = fzf(SUBS)
    stuff = titles(sub)
    post = fzf('\n'.join(stuff["names"]))
    data = stuff["data"]
    content(data, post)
    
if __name__ == "__main__":
    main()
