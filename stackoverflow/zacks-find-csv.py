import requests
import sys

URL = "https://www.zacks.com/earnings/earnings-calendar"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Goanna/6.0 Firefox/102.0 PaleMoon/32.0.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "qzip, deflate, br",
}

r = requests.get(URL, headers=headers)
if not r.ok:
    sys.exit("Could not request url")

print(r.text)
