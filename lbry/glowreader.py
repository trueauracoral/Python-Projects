import subprocess

# Change this to the location of your glow program
glow = "glow.exe"

# Get the link
link = input("Link: ")

# Just in case it's a lbry:// link
link = link.replace('lbry:/', 'https://lbry2.vanwanet.com/speech')

# Run in shell
subprocess.Popen([glow, link])
