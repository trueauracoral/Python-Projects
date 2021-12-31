# Neccasary import to convert org to html
from orgpython import to_html
# I need to get time instead of asking manuelly for it.
from time import gmtime, strftime
# copy for all platforms
import pyperclip

# Inputs
Title = input("Title: ")
Link = input("Link: ")
Date = str(strftime("%a, %d %b %Y %X"))
rssfile = "rss.xml"

# Get the org file
# neworgfile = open(orgfile, 'r').read()

# print(to_html(neworgfile, toc=False, offset=0, highlight=True))

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
    # f.write("\n<item>\n<title>"+Title+"</title>\n<link>"+Link+"</link>\n<guid>"+Link+"</guid>\n<pubDate>"+Date+"</pubDate>\n<description>\n"+htmlfile+"\n</description>\n</item>\n\n</channel>\n</rss>")

# Print file so I can glance and check for errors.
f = open('rss.xml', 'r')
content = f.read()
print(content)
pyperclip.copy(content)
f.close()
