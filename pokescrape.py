import re
import os

# Downloader
downloader = "yt-dlp"
# Folder to download to.
folder = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\"

# GET THE LINKS INSTRUCTIONS
# 1. Go to https://watch.pokemon.tv and click inspect element. Find the main div block, right click and press "Edit as HTML" finally hit control c.
# 2. Paste here and search and make sure you have player?id links. If you don't you got the wrong part of the html.
# 3. You could clean it up like I did so it will take less space.

# Pokemon Journey's watch.pokemon.com links. Could expire one day :(
source = '''player?id=1e711b68496f473ab403d506dc7161f1&amp;channelId=pokemon-journeys-the-series
player?id=4b10e9e02da94d8fae80534dae86ee68&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=6e3306ff96034b388d30c5b62a255abb&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=2e12b8a3cd544be3815b83b3b1d7b846&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=6bc77ed7a2a6444181ee22c4bb69688c&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=461649c491c047e5bd3fc401132def7f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=4484c61cbe2c492fac9bbfa3818695b9&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=70b492f7c71c40ee80f504a79aeefec2&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=fffc366443be462da60ea497787636ec&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=deddc4344f9d4d35b18e16f2f3d028bd&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
player?id=e41185bef1204278bf9470334b307c91&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=e2e200ca2bf94cd99dae8f756663ea9f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=2314e00b3844411fb49147b8b5b73e56&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=b7e816904b2044bda8a6dd6124411f0d&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=19c07bfb72154f9688ce28241cd3c5e3&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=06cf75907b7a4e2a8a6a811494596895&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=ed04a7d41d5745acbe5ecd4dd867a264&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=35629ec700b74ecabe34edca4d9673aa&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=0b1b1b85792a4542acd29180baec6f42&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=3aa6f50c7f5841078e286af3c6879dab&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=0ce03387d7a44d128f3bb422120d4e7f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=1e711b68496f473ab403d506dc7161f1&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=8bc1e099676a4f71887359266a5855a4&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=96f954184f984a3faa4d62a757b1ffa4&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=89a6a9b4f2c5494d915cc0f0e0a2cd7b&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=d3b777fd8e234accbc66bb1043843d1b&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=deb16e15625f488cae58d07bb54f879c&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=be9346275c30480d9b713176886dd626&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=90427289e68541258f006b737c597ec4&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=154a9d70325e4d58b183f3b0da3a87d4&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=cafc5a49e00248fc8efdf83bcbc0d750&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=1e86393c26574340ba75456763e4c59d&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=81360e8cbc8e4aeb8fa613b7e185f19f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=c8b8b04596304bb885131ea0f3d02332&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=2e2f25705edf4889b577c08fcf0f2a0e&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=a2cf1aeb11ba4ca39b3b551be5ecf46f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=43589458f5f94a57957b6cc0c785ad62&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=15e0a5fb117b45709e608e3b66dfc932&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=be98430b1d2d4e4cb8f91d9dab1be94f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=5cf03da5cc1d4d5aa3e9a6fc5cf52033&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=3b20d8fe058942258f2585558d99331d&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=c93c34a30526428fa0c19326dfb42fef&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=740cc5f8b6f74cb6b832561c9af16f33&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=c88f4583844244b6b452e00560a4287f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=1a22d8b6e35947e6a45a0f5c773835fd&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=8cac20b73a0e47a4be44a83718067209&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=e944a8c746b44f33ab94e39b1892872f&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=8a01a63676f04cfa8bf3c8022a0f7709&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false
/player?id=13a1d3ae0d9748b386da3b362e01736c&amp;channelId=pokemon-journeys-the-series&amp;cameFromHome=false'''

player_id = re.findall('player\?id=.{74}',source)
for link in player_id:
    print("https://watch.pokemon.com/en-us/#/" + link.replace("&amp;","&"))
    os.system(f"cd {folder} && {downloader} https://watch.pokemon.com/en-us/#/{link.replace('&amp;','&')}")
