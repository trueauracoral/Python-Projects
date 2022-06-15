#!/usr/bin/env python
# This is a plugin for converting lbc to usd
# (c) TrueAuraCoral 2021 - under GNU GPLv3 or any later version.

# Make sure you pip install this
import requests
# Get how much lbc
lbc = input("How much LBC? ")

# Print it out
print(requests.get("https://rate.sx/" + lbc + "LBC").text.rstrip())
