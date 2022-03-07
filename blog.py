# I need to get time instead of asking manuelly for it.
from time import gmtime, strftime
# copy for all platforms
import pyperclip
import os

# RSS GENERATION!
# Inputs
Title = input("Title: ")
Link = input("Link: ")
Date = str(strftime("%a, %d %b %Y %X"))
rssfile = 'rss.xml'

# rss file manipulation
with open(rssfile) as r:
  text = r.read().replace("\n</channel>\n</rss>", " ")
with open(rssfile, "w") as w:
  w.write(text)

# Add stuff
with open(rssfile, 'a') as f:
    f.write("\n<item>")
    f.write("\n<title>"+Title+"</title>")
    f.write("\n<link>"+Link+"</link>")
    f.write("\n<guid>"+Link+"</guid>")
    f.write("\n<pubDate>"+Date+"</pubDate>")
    f.write("\n<description>")
    f.write("\n<![CDATA[ <p>Consume this in any software you like!</p> ]]>")
    f.write("\n</description>")
    f.write("\n</item>")
    f.write("\n")
    f.write("\n</channel>")
    f.write("\n</rss>")

# Print file so I can glance and check for errors. Also copy the file to clipboard
f = open('rss.xml', 'r')
content = f.read()
print(content)
pyperclip.copy(content)
f.close()
