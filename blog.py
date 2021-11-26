# Inputs
Title = input("Title: ")
Link = input("Link: ")
Date = input("Date: ")
htmlfile = input("HTML file: ")
rssfile = "rss.xml"

# cdata ~> Description ~> Reads in rss reader I hope :-)
htmlfile = str("<![CDATA[ "+open(htmlfile).read().replace('\n', ' ')+" ]]>")

# Add stuff
with open(rssfile, 'a') as f:
    f.write("\n<item>\n<title>"+Title+"</title>\n<link>"+Link+"</link>\n<pubDate>"+Date+"</pubDate>\n<description>\n"+htmlfile+"\n</description>\n</item>\n")
