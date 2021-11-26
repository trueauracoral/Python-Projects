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

# Delete channel and rss tags
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
