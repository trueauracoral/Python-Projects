#!/usr/bin/env python
# This is supposed to help automate the process of adding software to
# FreeAlternatives

# GETTING DATA FROM:
# - alternativeto
# - github
# - wikipedia

# WHAT WE NEED:
# - names
# - comment
# - links
#   - git (if possible)
#   - wikipedia (if possible)
#   - documentation (if possible)
#   - icon
# - license
# - platforms
# - interface
# - languages
# - networks read (if possible)
# - networks write (if possible)
# - formats read (if possible)
# - formats write (if possible)
# - genaric name
import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

software = "gnu_emacs"
wikipedia_api_url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&rvsection=0&titles={software}&format=json"
data = requests.get(wikipedia_api_url).json()


# https://en.wikipedia.org/?curid=18933234
for page in data["query"]["pages"]:
    print(page)
#id = data["query"]["pages"]["
