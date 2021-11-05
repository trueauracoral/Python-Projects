# Version 0 by TrueAuraCoral
# # File to create blogs but mostly just generate rss entries for me
#
# # Ask for input and stuff for the entries
# title = input("Title: ")
# link = input("Link: ")
# date = input("Pubdate: ")
#
# # Use a multiple print to print both variables that I asked for input and print text.
# # I chose to use "+" variabe "+" as seperators. I seem to like this.
# print("<--------------COPY COPY COPY-------------->")
#
# print("<item>\n<title>" + title + "</title>")
#
# print("<link>" + link + "</link>")
#
# print("<pubDate>" + date + "</pubDate>")
#
# print("</item>")

# Version 1 by Duckey
# Ask for input and stuff for the entries
# title = input("Title: ")
# link = input("Link: ")
# date = input("Pubdate: ")
# file = input("Paste to: ")
#
#
# file = open(file, "w")
# file.writelines("<item>\n<title>" + title + "</title>\n")
#
# file.writelines("<link>" + link + "</link>\n")
#
# file.writelines("<pubDate>" + date + "</pubDate>\n")
#
# file.writelines("</item>\n")

# Version 2 GalacticColourisation#5721
# dat = {"title": None, "link": None, "date": None, "file": None}
# for k, v in dat.items():
#     dat[k] = input(f"{k}: ")
#
# with open(dat["file"], "r+") as file:
#     contents = file.readlines()[:-2]  # remove last two lines
#     contents.append(f"<item>\n<title>{dat['title']}</title>\n")
#     contents.append(f"<pubDate>{dat['date']}</pubDate>\n")
#     contents.append("</item>\n")
#     contents.append("</channel>\n</rss>\n\n\n")
#     file.seek(0)
#     file.truncate()
#     file.write(''.join(contents))

# Version 3 GalacticColourisation#5721
import textwrap

dat = {"title": None, "link": None, "date": None, "file": None}
for k, v in dat.items():
    dat[k] = input(f"{k}: ")

with open(dat["file"], "r+") as file:
    contents = ''.join(file.readlines()[:-2])  # remove last two lines
    contents += textwrap.dedent(
        f"""
        <item>
        <title>{dat['title']}</title>
        <link>{dat['link']}</link>
        <pubDate>{dat['date']}</pubDate>
        </item>\n\n\n
        </channel>
        </rss>
        """
    )
    file.seek(0)
    file.truncate()
    file.write(contents)
