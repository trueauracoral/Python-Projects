import requests
import json

query = "abababababab"

data = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{query}").json()

try:
    print(f"""Searching the Dictionary for {query}
Defintion: {data[0]["meanings"][0]["definitions"][0]["definition"]}
""")
except:
    print("No defintions found.")
