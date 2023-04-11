#!/usr/bin/env python
import requests
import csv

games = [["Red", "Blue", "R/B"], ["Yellow"], ["Crystal"], ["Ruby", "Sapphire", "R/S"], ["FireRed", "LeafGreen"], ["Emerald"], ["Diamond", "Pearl", "D/P"], ["Platinum"], ["Black", "White", "B/W"], ["Black 2", "White 2", "B2/W2"], ["Omega Ruby", "Alpha Sapphire", "OR/AS"], ["Sun", "Moon", "S/M"], ["Ultra Sun", "Ultra Moon", "US/UM"], ["Sword", "Shield", "SW/SH"], ["Brilliant Diamond", "Shining Pearl", "BDSP"]]

types = ["Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting", "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice", "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"]

data = requests.get("https://vid.puffyan.us/api/v1/playlists/PLFdGupe1YxogHKI230igaoZEE1sGfGwJk").json()["videos"]

titles = [(channel["title"]) for channel in data]
print(titles)
for game in games:
    print(game)
