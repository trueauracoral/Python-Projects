#!/usr/bin/env python
import requests

url = "lbry://@Nasikla:5/HSMMPS:a"
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

resolve = data.json()["result"][url]
claim = resolve["claim_id"]
name = resolve["name"]
# I do not know what is the name of this..
hashcut = resolve["value"]["source"]["sd_hash"][:6]
#https://player.odycdn.com/api/v4/streams/free/HSMMPS/ac721fb7b4628e43e5f6b824334b77aba4f3fa4b/9e9c17
text = requests.get(f"https://player.odycdn.com/api/v4/streams/free/{name}/{claim}/{hashcut}").text
print(text)
