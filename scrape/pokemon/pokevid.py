#!/usr/bin/env python
import re
import os

# Downloader
downloader = "yt-dlp"
# Folder to download to.
folder = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\"

# GET THE LINKS!
# 1. Go to https://watch.pokemon.tv, select a series and do inspect element. Find the main div block, right click, press "Edit as HTML" and copy.
# 2. Paste here into the source variable making sure it starts with ''' and ends with '''. Then search to make sure player?id is in it. If there are no results, then you probably have the wrong html.

#  Pokemon Sun & Moon https://watch.pokemon.com/en-us/#/ source code with player?id links. Could expire one day :(
source = '''
player?id=bc0317729f8b492daf704e962de5cf1c&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=d5af4c207c714a1bb206d434132f46dc&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=4851cd4f66f04e6f8992787b66bc0054&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=407a98634c104c82baf6fce69fa60d33&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=921b816bf40d4c95b21e244ad873abbb&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=aaec428402264fdda8e016a23ee0c9fb&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=643a4826d3a74a12ad0864770e4b7dc6&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=9d15d58fb89541cd9e46c408c8f2d4a2&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=2d1d9343459448e1be822b1342626b38&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=249c318718904b34b94623e6578ed20d&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=a1f76881036748d48ef1b12364112ef1&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=72e5e8a2afc242b59d8b893f398707d4&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=05028afb5bf445de8ea5accb466205e0&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=3d61bc8e5dd0441fb95e37f91d7fb6e3&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=3cbb0025c4c7488591317a2f58af82a3&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=cf5d1e86b8d6417b946c7e7e4e94dd0d&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=f0cc7f35329d4bb9b40afb27696b7854&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=42398d67a93c4b12bafa0d7a57490cbe&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=4e2471bbd4874ef5abe4d6c12c15dd08&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=19047391d8d54636b0dd2dd80730e78d&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=c8caf3c0b85440fd871751cae88eafc4&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=ad3853e753684c4bb32dac456ca24138&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=4c4757e483bb4894bfc28ee1acdec3ec&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=8a17e3a65bbf4c4ca5f59a16d532bb12&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=08c1a37c3112444388929f58043e400d&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=bcc8cbc794b34cfb89a472148d83ea45&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=4e4d205844a94e91aed11daac9f99ce4&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=ab3401d5cf2a405d95877a200aa92e18&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=b86c14b0edeb498181b9579050cd257c&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=48aad85c01f444cda64bdb0929416925&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=ff7108302321428f8ef1cbf763aa975e&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=0c15eb7a64a94a5882211715c151646a&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=f4b36b07e3c848ecb79e863658b0f4d7&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=918ccb5d3fab41fa86942c3fdfa33cb2&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=b7af684617e84132a43220c4773850c4&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=9cbe69da5a544a9fa3e5e7d3e2008ebd&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=d5adba865bcb49fc8fe4e6e5aaa6f506&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=63b10424d49d4e3db41b3173a1ed7cb0&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=b3c5e26ade5249dbbe2a75f8ebfacbc2&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=9444571a487e4a9d9d5931c0a38de046&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=50f5dad8df9041d0a9820014d1cb2a27&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=bec163bb692e4afaba9100dd1cbbd4b3&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=0158314a1e754158886c2d6d424e8fe7&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=d056255d15a34e2e99cd5e7982f3cfe5&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=4cdb86a1e6a14d23a0b82dd286d36606&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=89a72a7ba27a415d862aa3aa0c3dbcd2&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=55cd64fff25b48f3ae47e5982daa903f&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
player?id=f570f5b2f9ea44019fcbddd882d6e77e&amp;channelId=pokemon-the-series-sun-moon-ultra-adventures&amp;cameFromHome=false
'''
player_id = re.findall('player\?id=.{74}',source)
for link in player_id:
    print("https://watch.pokemon.com/en-us/#/" + link.replace("&amp;","&"))
    os.system(f"cd {folder} && {downloader} https://watch.pokemon.com/en-us/#/{link.replace('&amp;','&')}")
