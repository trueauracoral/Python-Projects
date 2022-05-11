import requests

move = input("Move: ").lower().replace(" ","-")
data = requests.get(f"https://pokeapi.co/api/v2/move/{move}")
if data.text == "Not Found":
    print("ERROR: Either, you inputed a misspelled/none existing move or the PokeApi data isn't working.")
    quit()
else:
    data = data.json()

try:
    print(f"""---
Type: {data["type"]["name"]}
Category: {data["damage_class"]["name"]}
Power: {data["power"]}
Accuracy: {data["accuracy"]}
PP: {data["pp"]}
Effect: {data["effect_entries"][0]["short_effect"]}""")
except:
    print("Error fetching data :(")
