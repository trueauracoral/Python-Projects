#!/usr/bin/env python
# For command line args
import sys
# For running commands in shell with subprocess.Popen or subprocess.run
import subprocess
        
# VARIABLES
browser = 'c:\\users\\stanl\\appData\\local\\bravesoftware\\brave-browser\\application\\brave.exe'
clipboard = ["clip"]
norm="\033[00m"
ital="\033[03m"
bold="\033[01m"
red="\033[96m"
black="\033[90m"
red="\033[91m"
green="\033[92m"
yellow="\033[93m"
blue="\033[94m"
magenta="\033[95m"
cyan="\033[96m"
white="\033[97m"

print("\n|===============================|")
print(ital+"|         RSS Generator         |"+norm)
print(bold+"|   Type help for more info     |"+norm)
print("|===============================|")

while True:
    command = input(bold+":"+norm) # the : will be the presented function

    if command == "help":
        print(
bold+'''
Enter a freedom respecting social media: 
mastodon - Twitter alternative
teddit - Reddit viewer
librarian - LBRY viewer

Now enter a link you want the RSS of and it will open in your
browser.
Other commands:
quit - Quits the program or you can use control + c
help - brings up this screen
'''+norm
    )

    elif command == "mastodon":
        # Get the link
        link = input("Mastodon link: ")
        
        # Add rss to given link
        new = link + ".rss"

        # Run the browser variable with the new url arg.
        subprocess.Popen([browser, new])

    elif command == "librarian":
        # Get the link
        link = input("Librarian link: ")
        
        # Add rss to given link
        new = link + "/rss"

        # Run the browser variable with the new url arg.
        subprocess.Popen([browser, new])
        
    elif command == "teddit":
        # Get the link
        link = input("Teddit link: ")
        
        # Add rss to given link
        new = link + "?api&type=rss"

        # Run the browser variable with the new url arg.
        subprocess.Popen([browser, new])
        
    elif command == "quit":
        break

    elif command != "":
        print(bold+"Not a correct command :( type help ")
        
# Copy to clipboard
subprocess.run(clipboard, universal_newlines=True, input=new)

