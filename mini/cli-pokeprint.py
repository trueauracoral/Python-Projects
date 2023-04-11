#!/usr/bin/env python
# A simpler version of Phoney Badger's pokemon-colorscripts tool:
# https://gitlab.com/phoneybadger/pokemon-colorscripts

import requests
import re
import os
import argparse
import random

# A place where you store pokemon sprites. You can get these sprites using the
# -g/--generate option.
dir = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\pokedex\\pixel"
# A program that you can find on github for terminal image printing. I
# found imcat because it works on windows but you can use whatever you
# want like ueberzug and whatever else.
cli_image_printer = "imcat"


def get_arguments():

    parser = argparse.ArgumentParser(description='CLI Pokeprint')

    parser.add_argument('-g', '--generate', type=str, metavar='DIR', help='Download all of the pokemon sprites to a specified directory.')
    parser.add_argument('-n', '--name', type=str, metavar='NAME', help='Select pokemon based on it\'s name.')
    parser.add_argument('-l', '--list', action="store_true", default=False, help='Copy the link to the pasted file')
    parser.add_argument('--no-title', action="store_true", default=False, help='Copy the link to the pasted file')
    parser.add_argument('-r', '--random', action="store_true", default=False, help='Copy the link to the pasted file')

    args = parser.parse_args()

    return args


def main():

    args = get_arguments()

    if args.generate:

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}

        database = "https://pokemondb.net/pokedex/all"
        request = requests.get(database, headers=headers)
        data = request.text
        print(data)
        images = re.findall('<img class=\"img-fixed icon-pkmn\" src=\"(.*?)\"', data)
        print(images)

        if os.path.isdir(args.generate) == False:
            os.mkdir(args.generate)

        for i, image in enumerate(images):
            url = image
            print(url)
            name = url.split("/")[-1].split(".png")[0]
            if "\\" in name:
                name = name.split("\\")[0]
            print(name)

            thumbnail_data = requests.get(url)
            png = name + ".png"
            cwd = os.getcwd()

            print(os.path.join(cwd, args.generate, png))

            with open(os.path.join(cwd, args.generate, png), 'wb') as f:
                f.write(thumbnail_data.content)

    elif args.list:
        for file in os.listdir(dir):
            print(file.replace(".png", ""))

    elif args.name:

        matches = []

        for file in os.listdir(dir):
            if file.startswith(args.name):
                matches.append(file)

        if matches != []:
            if not args.no_title:
                print(matches[0].replace(".png", ""))
            os.system(f'{cli_image_printer} "{os.path.join(dir,matches[0])}"')
        else:
            print(f"ERROR: Could not find {args.name}. This could be because of a spelling mistake. Or it was not saved on your computer.")

    elif args.random:

        pokemon = os.listdir(dir)[random.randint(0, len(os.listdir(dir)))]

        if not args.no_title:
            print(pokemon.replace(".png", ""))

        os.system(f'{cli_image_printer} "{os.path.join(dir,pokemon)}"')


if __name__ == '__main__':
    main()
