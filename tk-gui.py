# Import all of tkinter GUI stuff
from tkinter import *

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

# LIBRARIAN
feild_librarian = Entry(root, width=50)
feild_librarian.pack()
feild_librarian.insert(0, "Put a url:")

def click_librarian():
    myLabel = Label(root, text=feild_librarian.get() + "/rss")
    myLabel.pack()

button_librarian = Button(root, text="Enter", command=click_librarian)
button_librarian.pack()

# Teddit
feild_teddit = Entry(root, width=50)
feild_teddit.pack()
feild_teddit.insert(0, "Put a url:")

def click_teddit():
    myLabel = Label(root, text=feild_teddit.get() + "?api&type=rss")
    myLabel.pack()

button_teddit = Button(root, text="Enter", command=click_teddit)
button_teddit.pack()

# Run stuff
root.mainloop()
