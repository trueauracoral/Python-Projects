#!/usr/bin/env python
import requests
import os
import argparse
import json
import sys
import subprocess

REGIONS = {
    'us': 'United States',
    'uk': 'UK',
    'fr': 'France',
    'it': 'Italia',
    'de': 'Deutschland',
    'es': 'España',
    'el': 'América Latina',
    'br': 'Brasil',
    'ru': 'Россия',
    'dk': 'Danmark',
    'nl': 'Nederland',
    'fi': 'Suomi',
    'no': 'Norge',
    'se': 'Sverige',
}
REGION = "us" #default
PLAYER = "mpv"
DOWNLOADER = "yt-dlp"
def parse_arguments():
    parser = argparse.ArgumentParser(description='pass.py')
    parser.add_argument('-r', '--region', type=str, metavar='REGION', help='Select your region. Default: us')
    parser.add_argument('-s', '--series', action="store_true", default=False, help='Select a serie to download.')
    parser.add_argument('-P', '--stuns', action="store_true", default=False, help='Select a stun/playlist to download.')
    parser.add_argument('-m', '--movies', action="store_true", default=False, help='Select a movie to download.')
    parser.add_argument('-S', '--specials', action="store_true", default=False, help='Select a special spin off to download.')
    parser.add_argument('-j', '--junior', action="store_true", default=False, help='Select a babies nap time to download.')
    parser.add_argument('-p', '--player', action="store_true", default=False, help='Use the PLAYER variable to play episode')
    parser.add_argument('-c', '--captions', action="store_true", default=False, help='Add Soft Subtitles/Captions to the video.')
    parser.add_argument('-e', '--episode', action="store_true", default=False, help='In the selected channel (Not movies), select an episode to download or play with -p')
    #parser.add_argument('-f', '--fzf', action="store_true", default=False, help='Select with fzf')
    args = parser.parse_args()
 
    return args

def filter(data, key):
    return [(channel) for channel in data if channel["category"] == key]

def prompt(data, key=False, episode=False, fzf=False):
    count = 0
    if episode == True:
        for i, episode in enumerate(data[key]["media"]):
            count += 1
            print(f'({i+1}) {episode["title"]}')
    else:
        for i, channel, in enumerate(data):
            count += 1
            print(f'({i+1}) {channel["channel_name"]}')
    print("(q) quit")
    choice = input("> ")
    if type(choice) == str and choice.lower() == "q":
        sys.exit()
    try:
        choice = int(choice) - 1
    except:
        sys.exit(f"ERROR: Enter an integer between 1 and {count}")
    return choice

def play():
    subprocess.Popen([PLAYER, episode['stream_url']])
    sys.exit("Opened player")
    
def main():
    args = parse_arguments()
    global REGION
    if args.region:
        try:
            REGIONS[args.region]
            REGION = args.region
        except:
            print("Available Regions:")
            for key, value in REGIONS.items():
                print(f"{key}: {value}")
            sys.exit(f"Could not find {args.region}")

    r = requests.get(f"https://raw.githubusercontent.com/seiya-dev/pokemon-tv/master/watch/data/{REGION}.json")
    if r.status_code != 200:
        sys.exit("Uh, oh. Could not get data")
    data = r.json()

    # Series - Seasons of the pokemon anime
    # Stuns - "playlists" of episodes from the anime
    # Movies - From the pokemon anime
    # Specials - Spinoff series of the pokemon anime
    # Junior - Pokemon for babies nap time

    if args.series:
        data = filter(data, "Series")
    elif args.stuns:
        data = filter(data, "Stuns")
    elif args.movies:
        data = filter(data, "Movies")
    elif args.specials:
        data = filter(data, "Specials")
    elif args.junior:
        data = filter(data, "Junior")
    else:
        sys.exit("Read the help (-h/--help), must select either a series, playlist/stun, movie, special, junior to download.")

    choice = prompt(data)
    sel = data[choice]["media"]
    if args.episode:
        information = sel[prompt(data, choice, episode=True)]
        if args.player:
            play(information['stream_url'])
        else:
            os.system(f"{DOWNLOADER} {information['stream_url']} -o \"S{information['season'].zfill(2)}E{information['episode'].zfill(2)}.%(ext)s\"")
        sys.exit("finished")
            
    if data[choice-1]["category"] == "Movies":
        filename = f"{data[choice]['media'][0]['title']}.%(ext)s"
    else:
        filename = ""
    amount = len(sel)
    count = 0
    for episode in sel:
        if args.player:
            play(episode['stream_url'])
        count += 1
        if filename == "":
            filename = f"{count} - {episode['title']}.mp4"
            folder = os.path.join(os.getcwd(), data[choice-1]["channel_id_ext"])
            if not os.path.exists(folder):
                os.mkdir(folder)
            print(f"Downloading episode {count} out of {amount}")
        os.system(f"cd {folder} && {DOWNLOADER} {episode['stream_url']} -o \"{filename}\"")
        if args.captions:
            if REGION != "us":
                sys.exit("ERROR: Sorry, only captions for the us are supported.")
            for file in os.listdir(folder):
                if file.startswith(episode['episode']):
                    newfile = file
            full = os.path.join(folder, newfile)
            capfull = os.path.join(folder, 'cap'+newfile)
            enfull = str(os.path.join(folder, "en.vtt"))
            print("Downloading Captions...")
            captions = requests.get(episode["captions"])
            with open(enfull, 'wb') as f:
                f.write(captions.content)
            os.rename(full, capfull)
            os.system(f"ffmpeg -i \"{capfull}\" -i {enfull} -c copy -c:s mov_text -metadata:s:s:0 language=eng \"{full}\"")
            os.remove(enfull)
            os.remove(capfull)

if __name__ == "__main__":
    main()
