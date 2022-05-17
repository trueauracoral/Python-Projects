import requests
import os
browser = "palemoon"

search = input("Pokemon: ").lower().replace(" ","-")
data = requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000").json()
for pokemon in data["results"]:
    if search in pokemon["name"]:
        search = pokemon["name"].split("-")[0]
        search2 = pokemon["name"]

data = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{search}/").json()
data2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{search}/").json()
types = []
for type in data2["types"]:
    types.append(type["type"]["name"])
types = ' | '.join(types)
artwork = data2["sprites"]["other"]["official-artwork"]["front_default"]
os.system(f"{browser} {artwork}")
chain = requests.get(data["evolution_chain"]["url"]).json()
for evolution in chain["chain"]["evolves_to"]:
    evolves_to = evolution["species"]["name"]
print(f"""From Generation: {data["generation"]["url"].split("/")[6]}
Evolves to: {evolves_to}
Type: {types}""")
