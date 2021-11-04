#####################################################################
#                                                                   #
# DESCRIPTION:                                                      #
# This is a file for changing odysee links into a chosen link in the#
# variables.                                                        #
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
# For running commands in shell with subprocess.Popen
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
        link = input("Odysee link: ")

# Librarian does not accept the LBRY way of using '#' for the claim id
link = link.replace("#", ":")

# If you want to use a different instance or browser
instance = "librarian.bcow.xyz"
browser = 'c:\\users\\stanl\\appData\\local\\bravesoftware\\brave-browser\\application\\brave.exe'

# Only replace once
new = link.replace("odysee.com", instance, 1)

# Copy to clipboard
subprocess.run('clip', universal_newlines=True, input=new)

subprocess.Popen([browser, new])
