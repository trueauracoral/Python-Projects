# File that is for the future where odysee is not free software. This file
# replaces odysee.com with a librarian instance. Librarian is a alternative to
# odysee.com.  How it works: Basically, it takes a argument of a url, parses
# it, replaces with desired instance of librarian and then opens it with my
# brave.

# For getting command line args
import sys
# For running system commands. NOTE: Never use os.system for running system commands, just use subprocess.Popen([code])
import subprocess

# Get the URL arg
link = sys.argv[1]

# This is the instance I want to replace
instance = "librarian.bcow.xyz"

# Use .replace to replace with the variable above
new = link.replace("odysee.com", instance)

# Use subprocess.Popen to run my browser with the argument of the variable
# "new"
subprocess.Popen(['c:\\users\\stanl\\appData\\local\\bravesoftware\\brave-browser\\application\\brave.exe', new])
