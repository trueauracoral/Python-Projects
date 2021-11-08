# Import all of tkinter GUI stuff
from tkinter import *
import subprocess

# Important variable
root = Tk()

# Name of window
root.title("RSSgenerator")

# Window size
root.geometry('650x650')

# Color
background_color = '#1A1919'
root.configure(bg=background_color)

# Title properties
title = Label(root, text="----- \n RSS Generator \n ----- ",
              bg=background_color,
              fg='#ffffff',
              font='20')

# Place title on screen
title.pack()

# Help info
help_ = Label(root, text = "Instructions: \n Enter a freedom respecting social media: \n mastodon - Twitter alternative \n teddit - Reddit viewer \n librarian - LBRY viewer \n \n Now enter a link you want the RSS of and it will open in your browser. \n ----- ",
              bg = background_color,
              fg='#ffffff',
              font='20')

# Place help info on screen
help_.pack()

# MASTODON
feild_mastodon = Entry(root, width=50)
feild_mastodon.pack()
feild_mastodon.insert(0, "Put a mastodon url:")

def click_mastodon():
    new = feild_mastodon.get() + ".rss"
    myLabel = Label(root, text=feild_mastodon.get() + ".rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    subprocess.run('clip', universal_newlines=True, input=new)

button_mastodon = Button(root, text="Enter", command=click_mastodon)
button_mastodon.pack()

# LIBRARIAN
feild_librarian = Entry(root, width=50)
feild_librarian.pack()
feild_librarian.insert(0, "Put a librarian url:")

def click_librarian():
    new = feild_librarian.get() + "/rss"
    myLabel = Label(root, text=feild_librarian.get() + "/rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    subprocess.run('clip', universal_newlines=True, input=new)

button_librarian = Button(root, text="Enter", command=click_librarian)
button_librarian.pack()

# Teddit
feild_teddit = Entry(root, width=50)
feild_teddit.pack()
feild_teddit.insert(0, "Put a teddit url:")

def click_teddit():
    new = feild_teddit.get() + "?api&type=rss"
    myLabel = Label(root, text=feild_teddit.get() + "?api&type=rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    subprocess.run('clip', universal_newlines=True, input=new)

button_teddit = Button(root, text="Enter", command=click_teddit)
button_teddit.pack()

# Run stuff
root.mainloop()
