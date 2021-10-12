# Copyright (c) 2021 TrueAuraCoral
# You can copy this file under the GNU GPL version 3 or any later version

# This will ask the user for a file, a word they want to replace and the replacement word.

# Ask for file.
file = input("File: ")

# Read the file. Also makes sure the file exists.
with open(file) as f:
    text = f.read()

# Asks for a word
word = input("What word do you wish to replace? ")

# Asks for a replacement
replace = input("Replacement: ")

# Prints the replace words with print and adds a enter
print('\n', text.replace(word, replace))
