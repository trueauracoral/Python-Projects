#!/usr/bin/env python
import subprocess
import os

browser = "vieb "
links = [
    "https://codeberg.org",
    "https://tube.tchncs.de",
    "https://lbry.ix.tc",
    "https://odysee.com",
    "https://mastodon.online",
    "https://zortazert.codeberg.page",
    "https://davidovski.xyz",
    "https://uveronunix.com",
    "https://denshi.org",
    "https://itzzen.net",
]

for i, link in enumerate(links):
    print(i, link)

# Choose a result
c = input("Choose a link: ")
c = int(c)
chosen = str(links[c])

os.system(browser + chosen)
quit()
