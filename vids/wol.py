# Script for searching FOSS video platforms
import requests
import json
import os
import sys

print('''
/-------------------------------\\
|             wol api            |
\\-------------------------------/
''')

# Any command that you can run on your system with the url link. Possily use xdg-open for GNU/Linux systems
command = "vieb "
bold="\033[01m"
norm ="\033[00m"
bright_cyan ="\033[46m"
colora ="\033[45m"
colorb ="\033[44m"
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
