#####################################################################
#                                                                   #
# DESCRIPTION:                                                      #
# This is a file for changing mastodon links to have .rss at the end#
#                                                                   #
# LISCENSE INFO (A dedicated liscense file is in the repo.):        #
#      ALL THE CODE IN THIS REPOSITORY INCLUDING THIS FILE IS       #
# (C) TrueAuraCoral and Other Contributors 2021.                    #
# YOU CAN USE THIS FILE AND ANY OTHER FILE IN THIS REPOSITORY UNDER #
# THE TERMS OF GNU GENERAL PUBLIC LICENSE VERSION 3 OR ANY LATER    #
# VERSION. TO FIND THE FULL TEXT OF THE LICENSE GO TO THE GNU.ORG   #
# WEBSITE AT ( https://www.gnu.org/licenses/gpl-3.0.html ).         #
#####################################################################

# For command line args
import sys
# For running commands in shell with subprocess.Popen or subprocess.run
import subprocess

# Initialize the link variable so the loop works
link = ""

# Get link as the first argument if we can
try:
    link = sys.argv[1]
except:
    # Or prompt for the link
    # If the users just presses enter it will prompt again
    while not link:
        link = input("Mastodon link: ")

# VARIABLES
browser = 'c:\\users\\stanl\\appData\\local\\bravesoftware\\brave-browser\\application\\brave.exe'
clipboard = 'clip'

# Add .rss to given link
new = link + ".rss"

# Copy to clipboard
subprocess.run(clipboard, universal_newlines=True, input=new)

# Run the browser variable with the new url arg.
subprocess.Popen([browser, new])
