#!/usr/bin/env python
import requests
import os
import argparse
import json
import sys

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

def parse_arguments():
    parser = argparse.ArgumentParser(description='pass.py')
    parser.add_argument('-r', '--region', type=str, metavar='REGION', help='Select your region. Default: us')
    parser.add_argument('-s', '--series', action="store_true", default=False, help='Select a serie to download.')
    parser.add_argument('-c', '--captions', action="store_true", default=False, help='Add Soft Subtitles/Captions to the video.')
    args = parser.parse_args()
 
    return args

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

    with open("C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\anime\\us.json", "r", encoding="utf-8") as f:
        data = json.loads(f.read())
    #r = requests.get(f"https://raw.githubusercontent.com/seiya-dev/pokemon-tv/master/watch/data/{REGION}.json")
    #if r.status_code != 200:
    #    sys.exit("Uh, oh. Could not get data")
    #data = r.json()

    # Series - Seasons of the pokemon anime
    # Stuns - "playlists" of episodes from the anime
    # Movies - From the pokemon anime
    # Specials - Spinoff series of the pokemon anime
    # Junior - Pokemon for babies nap time

    if args.series:
        data = [(channel) for channel in data if channel["category"] == "Specials"]
        for channel in data:
            print(channel["channel_id"])
    count = 0
    for i, channel in enumerate(data):
        count += 1
        print(f'({i+1}) {channel["channel_name"]}')
    print("(q) quit")
    choice = input("> ")
    if type(choice) == str and choice.lower() == "q":
        sys.exit()
    try:
        choice = int(choice)
    except:
        sys.exit(f"ERROR: Enter an integer between 1 and {count}")

    folder = os.path.join(os.getcwd(), data[choice-1]["channel_id_ext"])
    if not os.path.exists(folder):
        os.mkdir(folder)
    if choice in list(range(1, count+1)):
        sel = data[choice-1]["media"]
        amount = len(sel)
        for episode in sel:
            filename = f"{episode['episode']} - {episode['title']}.mp4"
            print(f"Downloading episode {episode['episode']} out of {amount}")
            #os.system(f"cd {folder} && yt-dlp {episode['stream_url']} -o \"{filename}\"")
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
    else:
        sys.exit(f"ERROR: Enter an integer between 1 and {count}")

if __name__ == "__main__":
    main()
