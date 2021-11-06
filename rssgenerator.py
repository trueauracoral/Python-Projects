# For command line args
import sys
# For running commands in shell with subprocess.Popen or subprocess.run
import subprocess
        
# VARIABLES
browser = 'c:\\users\\stanl\\appData\\local\\bravesoftware\\brave-browser\\application\\brave.exe'
clipboard = 'clip'
        
to_text = True

print(
'''
                 
|===============================|
|         RSS Generator         |
|   Type help for more info     |
|===============================|
'''
)

while True:
    command = input() # the : will be the presented function
    to_text = False

    if command == "help":
        print(
'''
Enter a freedom respecting social media: 
mastodon - Twitter alternative
teddit - Reddit viewer
librarian - LBRY viewer

Now enter a link you want the RSS of and it will open in your
browser.
'''
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
        
# Copy to clipboard
subprocess.run(clipboard, universal_newlines=True, input=new)

