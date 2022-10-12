#!/usr/bin/env python

import requests
import re 
import sys

def pokemondb():
    url = "https://pokemondb.net/scarlet-violet"
    request = requests.get(url)

    if request.status_code != 200:
        sys.exit("Could not connect.")

    oof_pokemons = re.findall('<a href="/pokedex/.+?">(.*?)</a>', request.text)
    pokemons = []
    for pokemon in oof_pokemons:
        if "\xe9" not in pokemon:
            print(pokemon)
            pokemons.append(pokemon)
    return pokemons

def serebii():
    url = "https://www.serebii.net/scarletviolet/pokemon.shtml"

    request = requests.get(url)

    if request.status_code != 200:
        print("Could not connect.")

    oof_pokemons = re.findall('<h2><a href="/pokemon/(.+?)><b>(.*?)</b></a></h2>', request.text)
    pokemons = []
    for pokemon in oof_pokemons:
        # tuples
        pokemon = pokemon[1]
        if pokemon != "???":
            print(pokemon)
            pokemons.append(pokemon)
    return pokemons

if __name__ == '__main__':
    pokemondb()
    #serebii()
