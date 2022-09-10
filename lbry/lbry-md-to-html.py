#!/usr/bin/env python
import requests
import sys
import os

url = "lbry://@Nasikla:5/HSMMPS:a"
def resolve(url):
    json = {
        "jsonrpc": "2.0",
        "method": "resolve",
        "params": {
            "urls": [
                url
            ],
            "include_purchase_receipt": True,
            "include_is_my_output": True
        },
        "id": 1625272172800
    }

    data = requests.post("https://api.na-backend.odysee.com/api/v1/proxy?m=resolve", json=json)
    return data

def get(url):
    #OLD WAY
    #claim = resolve["claim_id"]
    #name = resolve["name"]
    ## I do not know what is the name of this..
    #hashcut = resolve["value"]["source"]["sd_hash"][:6]
    ##https://player.odycdn.com/api/v4/streams/free/HSMMPS/ac721fb7b4628e43e5f6b824334b77aba4f3fa4b/9e9c17
    #text = requests.get(f"https://player.odycdn.com/api/v4/streams/free/{name}/{claim}/{hashcut}").text
    json = {
        "jsonrpc":"2.0",
        "method":"get",
        "params": {
            "uri": url,
            "save_file": False
        },
        "id":1625272174700
    }
    data = requests.post("https://api.na-backend.odysee.com/api/v1/proxy?m=resolve", json=json).json()
    return data["result"]["streaming_url"]

def main():
    resolve = resolve(url).json()["result"][url]
    if resolve["value"]["source"]["media_type"] == "text/markdown":
        file = resolve["value"]["source"]["name"]
        # This is not perfect
        export = file.split(".")[0]+".html"
        with open(file, "w", encoding="utf-8") as f:
            f.write(requests.get(get(url)).text)
  os.system(f'pandoc {file} -o {export}')
    else:
        sys.exit("This is not a markdown publication.")
if __name__ == "__main__":
    main()
