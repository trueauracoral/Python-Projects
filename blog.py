# File to create blogs but mostly just generate rss entries for me

# Ask for input and stuff for the entries
title = input("Title: ")
link = input("Link: ")
date = input("Pubdate: ")

# Use a multiple print to print both variables that I asked for input and print text.
# I chose to use "+" variabe "+" as seperators. I seem to like this.
print("<--------------COPY COPY COPY-------------->")

print("<item>\n<title>" + title + "</title>")

print("<link>" + link + "</link>")

print("<pubDate>" + date + "</pubDate>")

print("</item>")
