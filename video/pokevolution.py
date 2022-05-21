import os
import requests

#data = requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000").json()
#for pokemon in data["results"]:
#    pokemon["name"]:

pokemon = "charmander"
data = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()
data = requests.get(data["evolution_chain"]["url"]).json()
def artinator(a):
    data2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{a}").json()
    artwork = data2["sprites"]["other"]["official-artwork"]["front_default"]
    with open(a+".png","wb") as f:
        f.write(requests.get(artwork).content)
if data["chain"]["evolves_to"] == []:
    artinator(pokemon)
    text = f"{pokemon.capitalize()} does not evolve"
    #second = ""
else:
    second = data["chain"]["evolves_to"][0]["species"]["name"]
    print(second)
    artinator(second)
    text = f"{pokemon.capitalize()} evolves into {second}"
    try:
        third = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
        artinator(third)
        print(third)
    except:
        third = ""
os.system(f'ffmpeg -y -i {pokemon}.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" edit-{pokemon}.png')
os.system(f"ffmpeg -y -i edit-{pokemon}.png -vf \"drawtext=text='{text}':fontcolor=black:fontsize=65:x=(w-text_w)/2:y=(h-text_h)/2:\" output.png")
with open("concat.txt","w") as f:
    f.write(f"""file 'output.png'
duration 10""")
if not second:
    os.system(f'ffmpeg -y -i {second}.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" edit-{second}.png')
    os.system(f"ffmpeg -y -i edit-{pokemon}.png -vf \"drawtext=text='{text}':fontcolor=black:fontsize=65:x=(w-text_w)/2:y=(h-text_h)/2:\" second.png")
    with open("concat.txt","a") as f:
        f.write(f"""file 'second.png'
duration 10""")
if not third:
    os.system(f'ffmpeg -y -i {third}.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" edit-{third}.png')
    os.system(f"ffmpeg -y -i edit-{pokemon}.png -vf \"drawtext=text='{text}':fontcolor=black:fontsize=65:x=(w-text_w)/2:y=(h-text_h)/2:\" third.png")
    with open("concat.txt","a") as f:
        f.write(f"""file 'third.png'
duration 10""")
os.system("ffmpeg -f concat -i concat.txt -c copy input.mp4")
os.system("mpv "+"output.png")
os.remove(pokemon+".png")
os.remove("edit-"+pokemon+".png")
