import os, os.path
import requests
import mimetypes

# Evolution image and a background image. For both it needs to be
# either an HTTPS URL or a file on your computer. Also needs to be a
# PNG file.

# This is an image to represent the pokemon evolving.
evolveimage = "https://spee.ch/@TrueAuraCoralPublishesImages:5/PokeevolutionEvolveSign:8"
# This is an image the pokemon will be overlayed on
backgroundimage = "https://spee.ch/@TrueAuraCoralPublishesImages:5/PokeevolutionBackgroundSign:a"
# Audio file to go over the video to make it less boring. Need to have
# one on your computer
audio = "C:\\SGZ_Pro\\Hobbys\\Media\\music\\lukrembo - butter (royalty free vlog music) [Ua7Qfc1xu90].mp3"

# Various pokemon you want to have a evolution video out of. These are
# all the starters in pokemon. This placeholder going to get oudated
# because scarlet and violet
pokemons = ["bulbasaur","charmander","squirtle","chikorita","cyndaquil","totodile","treecko","torchic","mudkip","turtwig","chimchar","piplup","snivy","tepig","oshawott","chespin","fennekin","froakie","rowlet","litten","popplio","grookey","scorbunny","sobble"]
#pokemons = ["bulbasaur","charmander"]

if evolveimage.startswith("https://"):
    with open("evolveimage.png","wb") as f:
        f.write(requests.get(evolveimage).content)
    evolveimage = "evolveimage.png"
if backgroundimage.startswith("https://"):
    with open("backgroundimage.png","wb") as f:
        f.write(requests.get(backgroundimage).content)
    backgroundimage = "backgroundimage.png"

os.system(f"ffmpeg -y -loop 1 -i {evolveimage} -c:v libx264 -t 10 -pix_fmt yuv420p -vf scale=1920:1080 evolveimage.mp4")
def artinator(a):
    data2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{a}").json()
    artwork = data2["sprites"]["other"]["official-artwork"]["front_default"]
    with open(a+".png","wb") as f:
        f.write(requests.get(artwork).content)

def makeevolutionvideo(pokemon):
    data = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}").json()
    data = requests.get(data["evolution_chain"]["url"]).json()
    artinator(pokemon)
    if data["chain"]["evolves_to"] == []:
        text = f"{pokemon.capitalize()} does not evolve"
        second = ""
        third = ""
    else:
        second = data["chain"]["evolves_to"][0]["species"]["name"]
        print(second)
        artinator(second)
        text = f"{pokemon.capitalize()} evolves into {second.capitalize()}"
        try:
            third = data["chain"]["evolves_to"][0]["evolves_to"][0]["species"]["name"]
            artinator(third)
            text3 = f"{second.capitalize()} evolves into {third.capitalize()}"
        except:
            third = ""
    # os.system(f'ffmpeg -y -i {pokemon}.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" edit-{pokemon}.png')
    os.system(f'ffmpeg -y -i {backgroundimage} -i {pokemon}.png -filter_complex "[1]scale=950:950[b];[0][b] overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" edit-{pokemon}.png')
    os.system(f"ffmpeg -y -loop 1 -i edit-{pokemon}.png -c:v libx264 -t 10 -pix_fmt yuv420p -vf scale=1920:1080 {pokemon}.mp4")
    os.system(f"ffmpeg -y -i evolveimage.mp4 -vf \"drawtext=text='{text}':fontcolor=white:bordercolor=black:borderw=5:fontsize=65:x=(w-text_w)/2:y=(h-text_h)/2:\" evolveimage-{pokemon}.mp4")
    with open("concat.txt","w") as f:
        f.write(f"""file '{pokemon}.mp4'
file 'evolveimage-{pokemon}.mp4'""")
    if second == "":
        pass
    else:
        text2 = f"{second.capitalize()} evolves into {third.capitalize()}"
        # os.system(f'ffmpeg -y -i {second}.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" edit-{second}.png')
        os.system(f'ffmpeg -y -i {backgroundimage} -i {second}.png -filter_complex "[1]scale=950:950[b];[0][b] overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" edit-{second}.png')
        os.system(f"ffmpeg -y -loop 1 -i edit-{second}.png -c:v libx264 -t 10 -pix_fmt yuv420p -vf scale=1920:1080 {second}.mp4")
        os.system(f"ffmpeg -y -i evolveimage.mp4 -vf \"drawtext=text='{text2}':fontcolor=white:bordercolor=black:borderw=5:fontsize=65:x=(w-text_w)/2:y=(h-text_h)/2:\" evolveimage-{second}.mp4")
        with open("concat.txt","a") as f:
            f.write(f"""
file '{second}.mp4'
file 'evolveimage-{second}.mp4'""")
    if third == "":
        pass
    else:
        # os.system(f'ffmpeg -y -i {third}.png -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:-1:-1" edit-{third}.png')
        os.system(f'ffmpeg -y -i {backgroundimage} -i {third}.png -filter_complex "[1]scale=950:950[b];[0][b] overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2:shortest=1" edit-{third}.png')
        os.system(f"ffmpeg -y -loop 1 -i edit-{third}.png -c:v libx264 -t 10 -pix_fmt yuv420p -vf scale=1920:1080 {third}.mp4")
        #os.system(f"ffmpeg -y -i edit-{third}.mp4 -vf \"drawtext=text='{text3}':fontcolor=white:bordercolor=black:borderw=5:fontsize=65:x=(w-text_w)/2:y=(h-text_h)/2:\" {third}.mp4")
        with open("concat.txt","a") as f:
            f.write(f"""
file '{third}.mp4'""")
    os.system(f"ffmpeg -y -f concat -i concat.txt -c copy vid-{pokemon}.mp4")
    for file in os.listdir():
        if file == "backgroundimage.png":
            pass
        elif file == "evolveimage.png":
            pass
        elif file.endswith(".png"):
            os.remove(file)
    os.remove(pokemon+".mp4")
    os.remove("evolveimage-"+pokemon+".mp4")
    os.remove(second+".mp4")
    os.remove("evolveimage-"+second+".mp4")
    os.remove(third+".mp4")

for thing in pokemons:
    makeevolutionvideo(thing)
    print(f"Made video for {thing.capitalize()}.")
    with open("concat2.txt","a") as f:
        f.write(f"\nfile 'vid-{thing}'")

os.system(f"ffmpeg -y -f concat -i concat2.txt -c copy input.mp4")
#os.remove("backgroundimage.png")
#os.remove("evolveimage.png")
#os.remove("evolveimage.mp4")
#for thing in pokemons:
#    os.remove("vid-"+thing+".mp4")

#os.system(f'ffmpeg -y -i input.mp4 -i "{audio}" -filter_complex \" [1:0] apad \" -shortest vid-{pokemon}.mp4')
#data = requests.get("https://pokeapi.co/api/v2/pokemon?limit=2000").json()
#for pokemon in data["results"]:
#    pokemon["name"]:
