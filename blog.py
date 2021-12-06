# I need to get time instead of asking manuelly for it.
from time import gmtime, strftime

# Inputs
Title = input("Title: ")
Link = input("Link: ")
Date = str(strftime("%a, %d %b %Y %X"))
#htmlfile = input("HTML file: ")
rssfile = "rss.xml"

# cdata ~> Description ~> Reads in rss reader I hope :-)
# I need to figure out how to get data from <p> in html file
# htmlfile = str("<![CDATA[ "+open(htmlfile).read().replace('\n', ' ')+" ]]>")

# Delete channel and rss tags A very wonky and odd solution to the
# issue of this text being early in the file is to litterally add
# spaces to the end of the tags so it's very specific in what it's
# looking for.
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
    f.write("\n<![CDATA[ You can consume this content in any app you like! ]]>")
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
f.close()
