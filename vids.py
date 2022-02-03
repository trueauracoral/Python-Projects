# Script for searching FOSS video platforms
import requests
import json
import os
import sys

print('''
/-------------------------------\\
|             vids              |
\\-------------------------------/
''')

command = "vieb "
bold = "\033[01m"
norm = "\033[00m"
bright_cyan = "\033[46m"
colora = "\033[45m"
colorb = "\033[44m"
try:
    if sys.argv[1] == "-i":
        invidious_instance = "https://invidio.xamh.de"
        query = input("Searching for: ")
        query = str(query)
        size = str(19)
        invidious_search = invidious_instance + "/api/v1/search?q=" + query
        wol_api = "https://scrap.madiator.com/api/get-lbry-video?url="

        data = requests.get(invidious_search)
        json_stuff = json.loads(data.text)
        for i, vid in enumerate(json_stuff):
            print(i, colora+vid["title"]+norm+"\n"+colorb+vid["author"]+norm+"\n"+bright_cyan+vid["videoId"]+norm)

        c = 100000
        while not c >= 0 or not c <= 19:
            c = input('Number from 1-' + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000
        # wol-api check
        lbry_check = requests.get(wol_api + json_stuff[c]["videoId"])
        lbry_check = json.loads(lbry_check.text)
        librarian_instance = "https://lbry.ix.tc/"

        if lbry_check["lbryurl"] == None:
            selected_url = invidious_instance + '/watch?v=' + json_stuff[c]["videoId"]
        else:
            selected_url = librarian_instance + lbry_check["lbryurl"]
            selected_url = selected_url.replace("#", ":")

        # Do stuff with it.
        os.system(command + selected_url)
        quit()
    elif sys.argv[1] == "-p":
        query = input("Searching for: ")
        query = str(query)
        size = str(19)
        search = "https://sepiasearch.org/api/v1/search/videos?search=" + query
        # Any command that you can run on your system with the url link. Possily use xdg-open for GNU/Linux systems

        data = requests.get(search)
        json_stuff = json.loads(data.text)
        for i, vid in enumerate(json_stuff["data"]):
            print(i, colora+vid["name"]+norm+"\n"+colorb+vid["channel"]["displayName"]+norm+"\n"+bright_cyan+vid["url"]+norm)

        # Choose a result
        c = 100000
        while not c >= 0 or not c <= 19:
            c = input('Number from 1-' + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000

        selected_url = json_stuff["data"][c]["url"]

        # Do stuff with it.
        os.system(command + selected_url)
        quit()
    elif sys.argv[1] == "-l":
        query = input("Searching for: ")
        query = str(query)
        size = str(30)
        search = 'https://lighthouse.lbry.com/search?s=' + query + '&include=channel,title&size=' + size
        lbry = "https://lbry.ix.tc/"

        data = requests.get(search)
        json_stuff = json.loads(data.text)

        # Results
        for i, x in enumerate(json_stuff):
            pre = "lbry://"
            if x["channel"]:
                pre += x["channel"] + "/"
            url = pre + x["name"]
            print(i, bright_cyan+url+norm)

        # Choose a result
        c = 100000
        while not c >= 0 or not c <= 29:
            c = input('Number from 1-' + size + " of the URL you want to open: ")
            try:
                    c = int(c)
            except:
                    c = 100000
        selected_url = json_stuff[c]

        # Do stuff with it.
        url = str(lbry + selected_url["channel"] + "/" + selected_url["name"])
        os.system(command + url)
        quit()
except:
    print('''
Command:
python vids.py <arg>
-l for lighthouse (LBRY network)
-p for sepia (Peertube)
-i for invidious (YouTube) 
NOTE: All youtube links will be checked with the Watch on LBRY API. If
the video is available on the lbry network, the youtube search result
will be opened in librarian.
''')
