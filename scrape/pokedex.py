import requests
import re
import sys
import random

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

query = ""
try:
    query = sys.argv[1]
except:
    while not query:
        query = input("Searching for: ")

search = f"https://pokemondb.net/pokedex/{query}"
search_result = requests.get(search, headers=headers)
search_data = str(search_result.content)
pokedex = re.findall('<td class="cell-med-text">(.+?)</td>',search_data)
try:
    print(links[random.randint(0,len(links))])
except:
    print("ERROR: Either you mispelled or this pokemon doesn't exist")
