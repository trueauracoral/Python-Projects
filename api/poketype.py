#!/usr/bin/env python
import requests

type = input("Type: ").lower()
data = requests.get(f"https://pokeapi.co/api/v2/type/{type}")
if data.text == "Not Found":
    print("ERROR: Either, you inputed a misspelled/none existing type or the PokeApi data isn't working.")
    quit()
else:
    data = data.json()

print("Weak to:")
for ddf in data["damage_relations"]["double_damage_from"]:
    print("- "+ddf["name"]+" (Double Damage!)")
for hdf in data["damage_relations"]["half_damage_from"]:
    print("- "+hdf["name"]+" (Half Damage)")
for ndt in data["damage_relations"]["no_damage_to"]:
    print("- "+ndt["name"]+" (No Damage!)")

print("Strong to:")
for ddt in data["damage_relations"]["double_damage_to"]:
    print("- "+ddt["name"]+" (Double Damage!)")
for hdt in data["damage_relations"]["half_damage_to"]:
    print("- "+hdt["name"]+" (Half Damage)")
for ndf in data["damage_relations"]["no_damage_from"]:
    print("- "+ndf["name"]+" (No Damage!)")
