import sqlite3
import subprocess
import os
import platform

browser = "qutebrowser"
fzf = "C:\\SGZ_Pro\\z-Apps_Drivers\\fzf-0.30.0-windows_amd64\\fzf.exe --reverse < FILE"

if platform.system() == "Windows":
    appdata = os.getenv('APPDATA')
    bookmarks_file = f"{appdata}\\qutebrowser\\config\\bookmarks\\urls"
    history_file = f"{appdata}\\qutebrowser\\data\\\history.sqlite"
else:
    bookmarks_file = "~/.config/qutebrowser/config/bokmarks/urls"
    history_file = "~/.local/share/qutebrowser/history.sqlite"

with open(bookmarks_file) as f:
    bookmarks_file = f.read()
with open("bookman.txt","w") as f:
    f.write(bookmarks_file)
    f.write("\n-------")

con = sqlite3.connect(history_file)
cur = con.cursor()

#cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
cur.execute("SELECT url,title FROM History;")
with open("bookman.txt","a") as f:
    for url in reversed(cur.fetchall()):
        if url[1] == "":
            f.write(url[0].encode('utf-8').decode('ascii','ignore')+"\n")
        elif url[1] == url[0]:
            f.write(url[1].encode('utf-8').decode('ascii','ignore')+"\n")
        else:
            f.write(url[1].encode('utf-8').decode('ascii','ignore')+" - "+url[0].encode('utf-8').decode('ascii','ignore')+"\n")

choice = subprocess.getoutput(fzf.replace("FILE","bookman.txt"))
if choice is not "":
    subprocess.Popen(f"{browser} {choice}")
os.remove("bookman.txt")