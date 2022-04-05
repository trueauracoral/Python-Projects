import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

query = ""
try:
    query = sys.argv[1]
    print(query)
except:
    while not query:
        query = input("Searching for: ")

search = f"https://knowyourmeme.com/search?q={query}"
search_result = requests.get(search, headers=headers)
search_data = str(search_result.content)
if "No results" in search_data:
    print("Nothing found :(")
    quit()
links = re.findall('<a href="/memes/.+?">',search_data)
for i, link in enumerate(links[15:]):
    url = "https://knowyourmeme.com" + link.replace("<a href=\"", "").replace("\">", "").replace("\" rel=\"nofollow","")
    if "trending" in url:
        break
    print(i, url)

while True:
    try:
        c = int(input(f"Which meme from 0-{i}: "))
    except ValueError:
        continue
    else:
        break

selected = "https://knowyourmeme.com"+links[c+15].replace("<a href=\"", "").replace("\">", "").replace("\" rel=\"nofollow","")

result = requests.get(selected, headers=headers)
data = str(result.content)

paragraph = re.findall('<p>(.+?)</p>',data)
cleaner = re.compile('<.*?>')
about = re.sub(cleaner, '', paragraph[2])
print("\nAbout: " + about.replace("\\'","'"))
origin = re.sub(cleaner, '', paragraph[3])
print("\nOrigin: " + origin.replace("\\'","'"))
spread = re.sub(cleaner, '', paragraph[4])
