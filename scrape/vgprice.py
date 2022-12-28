#!/usr/bin/env python

# Game:         Revenue:
# Pokemon       296.98
# Yu-Gi-Oh!     27.53
# Yo-kai Watch	12.916
# Beyblade	    0.97
# Digimon	    0.24

import requests
import re

def digimon():
    digimon_games = requests.get("https://wikimon.net/api.php?action=query&formatversion=2&prop=revisions&rvprop=content&rvslots=*& titles=List_of_Video_Games&format=json").json()
    digimon_games = digimon_games["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
    #print(digimon_games)
    # good regek <i><a.*?href=".*?".*?>(.*?)</a></i>
    find = re.findall('\* \[\[(.*?)\]\]', digimon_games)
    games = []
    for game in find:
        if "|" in game:
            game = game.split("|")[1]
        elif "(Game)" in game:
            game = ' '.join(game.split(" ")[:-1])
        elif ":" in game:
            game = game.replace(":", "%3A")
        games.append(game)
    return games

def beyblade():
    beyblade_games = requests.get("https://bw.vern.cc/beyblade/wiki/Category:Video_Games").text
    find = re.findall('<li><a.*?href=".*?".*?>(.*?)</a></li>', beyblade_games)[:-1]
    games = []
    for game in find:
        compiled = re.compile(re.escape(" (video game)"), re.IGNORECASE)
        res = compiled.sub("", game)
        res = res.replace(" (game)", "")
        res = res.replace(" (Switch game)", "")
        games.append(res)
    return games

def pricecalc(find):
    price = 0
    for game in find:
        print(game)
        data = requests.get(f"https://www.vgchartz.com/games/games.php?name={game}&keyword=&console=&region=All&developer=&publisher=&  goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=50&order=Sales&showtotalsales=0&showtotalsales=1&   showpublisher=0&showvgchartzscore=0&shownasales=0&showdeveloper=0&showcriticscore=0&showpalsales=0&showreleasedate=0&showuserscore=0&  showjapansales=0&showlastupdate=0&showothersales=0&showshipped=0").text
        try:
            results = re.findall('<th colspan="3" align="left" style="color:white;">Results: (.+?)</th>', data)[0]
            if results == "(0)":
                print("Could not find price :(")
            else:
                prices = re.findall('<td align="center">(.+?)</td>', data)[0]
                if "m" in prices:
                    price += float(prices.split("m")[0])
                    print(prices)
                    print(price)
        except:
            print("uh oh")
    print(price)

def yu_gi_oh():
    data = requests.get("https://www.vgchartz.com/games/games.php?name=yu-gi-oh&keyword=&console=&region=All&developer=&publisher=&goty_year=&genre=&boxart=Both&banner=Both&ownership=Both&showmultiplat=No&results=200&order=Sales&showtotalsales=0&showtotalsales=1&showpublisher=0&showvgchartzscore=0&shownasales=0&showdeveloper=0&showcriticscore=0&showpalsales=0&showreleasedate=0&showuserscore=0&showjapansales=0&showlastupdate=0&showothersales=0&showshipped=0").text
    prices = re.findall('<td align="center">(.+?)</td>', data)
    price = 0
    for game in prices:
        if "m" in game:
            price += float(game.split("m")[0])
            print(game)
            print(price)
    print(price)
yu_gi_oh()