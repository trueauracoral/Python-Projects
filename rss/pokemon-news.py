#!/usr/bin/env python
import requests
import re
import urllib.parse

WEBSITE = "https://www.pokemon.com"
DIR = "/us/pokemon-news/"
HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1', "Content-Type": "text/html;charset=UTF-8"}

def main():
    data = requests.get("https://www.pokemon.com/us/pokemon-news", headers=HEADERS).text

    print('''<rss version="2.0">
<channel>
<title>Pokemon News</title>
<link>https://www.pokemon.com/us/pokemon-news/</link>
<description>RSS for Pokemon News articles</description>
''')
    dates = re.findall('<p class="date">(.*?)</p>', data)
    titles = re.findall("<h3>(.*?)</h3>", data)
    descriptions = re.findall('<p>|<p class="hidden-mobile">(.*?)</p>', data)
    descriptions = [x for x in descriptions if x]
    combined = urllib.parse.urljoin(WEBSITE, DIR)
    links = re.findall(f'<a href="{DIR}(.*?)"', data)
    for (desc, title, date, link) in zip(descriptions, titles, dates, links):
        print(f"""<item>
    <title>{title}</title>
    <link>{combined+link}</link>
    <description><![CDATA[{desc}]]></description>
</item>""")

    print("""
</channel>
</rss>""")
if __name__ == "__main__":
    main()
