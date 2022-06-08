import subprocess
import os

browser = "palemoon"
fzf = "C:\\SGZ_Pro\\z-Apps_Drivers\\fzf-0.30.0-windows_amd64\\fzf.exe --reverse < FILE"

engines = """
bing - https://www.bing.com/search?q=
brave - https://search.brave.com/search?q=
duckduckgo - https://duckduckgo.com/?q=
google - https://www.google.com/search?q=
qwant - https://www.qwant.com/?q=
swisscows - https://swisscows.com/web?query=
yandex - https://yandex.com/search/?text=
bbcnews - https://www.bbc.co.uk/search?q=
cnn - https://www.cnn.com/search?q=
googlenews - https://news.google.com/search?q=
wikipedia - https://en.wikipedia.org/w/index.php?search=
wiktionary - https://en.wiktionary.org/w/index.php?search=
reddit - https://www.reddit.com/search/?q=
odysee - https://odysee.com/$/search?q=
youtube - https://www.youtube.com/results?search_query=
amazon - https://www.amazon.com/s?k=
craigslist - https://www.craigslist.org/search/sss?query=
ebay - https://www.ebay.com/sch/i.html?&_nkw=
gumtree - https://www.gumtree.com/search?search_category=all&q=
archaur - https://aur.archlinux.org/packages/?O=0&K=
archpkg - https://archlinux.org/packages/?sort=&q=
archwiki - https://wiki.archlinux.org/index.php?search=
debianpkg - https://packages.debian.org/search?suite=default&section=all&arch=any&searchon=names&keywords=
github - https://github.com/search?q=
gitlab - https://gitlab.com/search?search=
sourceforge - https://sourceforge.net/directory/?q=
stackoverflow - https://stackoverflow.com/search?q=
"""

with open("search-engines.txt","w") as f:
    f.write(engines)

choice = subprocess.getoutput(fzf.replace("FILE","search-engines.txt")).split(" - ")[1]
search = input("Search: ").replace(" ","%20")
subprocess.Popen(f"{browser} {choice}{search}")
os.remove("search-engines.txt")
