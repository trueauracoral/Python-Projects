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

subprocess.Popen([browser, new])