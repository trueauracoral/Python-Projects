#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def request(url, jsonify=False):
    r = requests.get(url)
    if not r.ok:
        sys.exit("Could not request url")

    if jsonify == False:
        return r.text
    elif jsonify == True:
        return r.json()

def main():
    data = request("https://pokemondb.net/pokedex/national")
    soup = BeautifulSoup(data, 'html.parser')
    generations = soup.find_all("div", {"class": "infocard-list infocard-list-pkmn-lg"})
    for i, generation in enumerate(generations):
        pokemons = generation.find_all("div", {"class": "infocard"})
        allof = []
        for pokemon in pokemons:
            types = pokemon.find_all("small")[1].text.split(" ")
            if len(types) == 3:
                types = [types[0], types[2]]
            else:
                types = [types[0]]
            allof += types;
        originals = [*set(allof)]
        numbers = []
        for original in originals:
            numbers.append(str(allof.count(original)))
        print(f"""Gen{i+1},{','.join(originals)}
{i+1},{','.join(numbers)}""")

if __name__ == "__main__":
    main()
