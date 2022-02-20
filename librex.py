import requests
import json
import os
import sys

librex_instance = "https://search.davidovski.xyz/"
# put a space at the end for it to work
command = "palemoon "

# C O L E R S
bold = "\033[01m"
norm = "\033[00m"
bright_cyan = "\033[46m"
colora = "\033[45m"
colorb = "\033[44m"

try:
    query = sys.argv[2]
except:
    query = input("Searching for: ")
    query = str(query)
size = str(19)
librex_search = librex_instance + "api.php?q=" + query + "&p=1&img_search=false"

data = requests.get(librex_search)
json_stuff = json.loads(data.text)
for i, vid in enumerate(json_stuff):
    print(i, colora+vid["title"]+norm+"\n"+colorb+vid["url"]+norm)

c = 100000
while not c >= 0 or not c <= 19:
    c = input('Number from 1-' + size + " of the URL you want to open: ")
    try:
            c = int(c)
    except:
            c = 100000

selected_url = json_stuff[c]["url"]
os.system(command + selected_url)
quit()
