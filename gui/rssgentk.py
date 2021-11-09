# Import all of tkinter GUI stuff
from tkinter import *
import subprocess

# Important variable
root = Tk()

# Name of window
root.title("RSSgenerator")

# Set the icon
root.iconbitmap('freedomerss.ico')

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

# Mastodon label
label_mastodon = Label(root, text = "Put a Mastodon url:",
                       bg = background_color,
                       fg = '#ffffff',
                       font='10')
# Place mastodon label on screen
label_mastodon.pack()

# MASTODON
feild_mastodon = Entry(root, width=50)
feild_mastodon.pack()

def click_mastodon():
    new = feild_mastodon.get() + ".rss"
    myLabel = Label(root, text=feild_mastodon.get() + ".rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(new)

button_mastodon = Button(root, text="Enter", command=click_mastodon)
button_mastodon.pack()

# Nitter label
label_nitter = Label(root, text = "Put a Nitter url:",
                       bg = background_color,
                       fg = '#ffffff',
                       font='10')
# Place nitter label on screen
label_nitter.pack()

# NITTER
feild_nitter = Entry(root, width=50)
feild_nitter.pack()

def click_nitter():
    new = feild_nitter.get() + "/rss"
    myLabel = Label(root, text=feild_nitter.get() + "/rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(new)

button_nitter = Button(root, text="Enter", command=click_nitter)
button_nitter.pack()

# Librarian label
label_librarian = Label(root, text = "Put a Librarian url:",
                       bg = background_color,
                       fg = '#ffffff',
                       font='10')
# Place librarian label on screen
label_librarian.pack()

# LIBRARIAN
feild_librarian = Entry(root, width=50)
feild_librarian.pack()

def click_librarian():
    new = feild_librarian.get() + "/rss"
    myLabel = Label(root, text=feild_librarian.get() + "/rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(new)

button_librarian = Button(root, text="Enter", command=click_librarian)
button_librarian.pack()

# Teddit label
label_teddit = Label(root, text = "Put a Teddit url:",
                       bg = background_color,
                       fg = '#ffffff',
                       font='10')
# Place teddit label on screen
label_teddit.pack()

# Teddit
feild_teddit = Entry(root, width=50)
feild_teddit.pack()

def click_teddit():
    new = feild_teddit.get() + "?api&type=rss"
    myLabel = Label(root, text=feild_teddit.get() + "?api&type=rss is copied!")
    myLabel.pack()

    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(new)

button_teddit = Button(root, text="Enter", command=click_teddit)
button_teddit.pack()

# Run stuff
root.mainloop()
