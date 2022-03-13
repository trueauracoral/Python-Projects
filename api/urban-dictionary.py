import requests
import json
import sys

bold = "\033[01m"
norm = "\033[00m"
query = ""
try:
    query = sys.argv[1:]
except:
    while not query:
        query = input("Searching for: ")

api = f"https://api.urbandictionary.com/v0/define?term={query}"
data = requests.get(api)
json_stuff = json.loads(data.text)
for i, result in enumerate(json_stuff["list"]):
    print(bold+"Word: "+norm+result["word"]+"\n"+bold+"Definition: "+norm+result["definition"].replace("\n","").replace("[","").replace("]","")+"\n" +bold+"Example: "+norm+result["example"].replace("\n","").replace("[","").replace("]","")+"\n---")
    if i == 1:
        break
