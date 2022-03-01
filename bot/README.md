# How to use FOSSBOT?

Fossbot is capable of doing many things but one of it's key features is to detect sent youtube, reddit or twitter links and send back a message link with a proxy site such as: invidious, teddit and nitter.

## Extra Commands:

- `fossbot-help` <br>
Print out this help message.
- `!fby` qeury <br>
Print out youtube search results as invidious links with title and channel information. Uses the invidious API
- `!fbp` qeury <br>
Print out peertube search results as peertube instance links with title and channel information. Uses the sepiasearch API
- `!fbl` query <br>
Print out LBRY search results as librarian links with title and channel information. Uses the lighthouse API
- `!fbc` query <br>
Print out in USD values of crypto currencies. Uses the rate.sx API.
- `!fbn` query <br>
Print out the amount of neow coins a user on neow has.
- `!fbw` query <br>
Print out wikipedia search result snippets of different articles including links to those articles.
- `!fbu` query <br>
Print out uncyclopedia search result snippets of different articles including links to those articles.
- `!fbu` query <br>
Print out uncyclopedia search result snippets of different articles including links to those articles.
- `!fbg` query <br>
Print out repo information of github and gitea projects.

# Host FOSSBOT

Here is what you will need to do host fossbot yourself:
- Create a matrix account and save the login credentials.
- Making sure you have python and pip installed run `pip install matrix_bot_api`
- Download the script by running this in your terminal `curl -o fossbot.py https://codeberg.org/zortazert/Python-Projects/raw/branch/main/bot/fossbot.py`
- Edit the script to change these values: <br>
```python
# Global variables
USERNAME = ""  # Bot's username
PASSWORD = ""  # Bot's password
SERVER = ""  # Matrix server URL
```
- Run the script, preferably on a server that runs constantly or just run the script on a computer you have access to on your own schedule.

Another option is to contact me links listed below for me to make the account **I** run fossbot on inside your server. It isn't guaranteed I will put him in your server. Also I run fossbot only during the CST daytime, not 24/7.

# Help is Appreciated!

I am not a great programmer, yet. Please write bug reports, suggestions for the inclusion of new ideas/commands, and code improvements!

# Contact me

- Email: zortazert@matthewevan.xyz
- Matrix: @zortazert:tchncs.de

# Watch FOSSBOT in action!

[![Video explination](https://tube.tchncs.de/lazy-static/previews/99b24a26-17f6-4abb-b914-0684514c9b8f.jpg)](https://tube.tchncs.de/w/tGPUDpuP3k5QZzJHyaDWn4)

Click on the image above to watch the video ^ or just click this peertube link. https://tube.tchncs.de/w/tGPUDpuP3k5QZzJHyaDWn4

Librarian: https://lbry.mutahar.rocks/@trueauracoral:a/fossbot:6

**NOTE:** This video shows a older version of fossbot with a bit less commands and different syntax to use the bot. This video is purely for showcasing the bot.
