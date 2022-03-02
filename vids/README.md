# <img src="logo.png" alt = "vids logo" width = "85" height = "45" /> vids

# Dependencies
In order to run this script you need:
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Requests](https://en.wikipedia.org/wiki/Requests_(software))

## Other Programs
Recommended:
- [mpv](https://github.com/mpv-player/mpv)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [youtube-dl](https://github.com/ytdl-org/youtube-dl)

The script takes a search term as input and returns a list of URLs of which one can be selected and opened in a program in your system's $PATH. [mpv](https://github.com/mpv-player/mpv) with [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [youtube-dl](https://github.com/ytdl-org/youtube-dl) are recommend because [mpv](https://github.com/mpv-player/mpv) is minimal, not a browser and works well on lower end hardware. If you don't have or want [mpv](https://github.com/mpv-player/mpv), this script can be easily modified to open links in a browser or other program.

# Install
In order to install this script you need to install both the config file and python script. You can easily do this with these two curl commands.
```bash
curl -o vids.py https://codeberg.org/zortazert/Python-Projects/raw/branch/main/vids/vids.py
curl -o vids.conf https://codeberg.org/zortazert/Python-Projects/raw/branch/main/vids/vids.conf
```

# Configurable Variables
This script comes with a config file. *Make sure the config file is in the same directory as the script!* The config file is called [vids.conf](vids.conf) in here you can find a lot of settings.
``` ini
[CONFIG]
librarian_instance = https://lbry.mutahar.rocks/
invidious_instance = https://invidio.xamh.de/
piped_instance = https://piped.kavin.rocks/
pipedapi_instance = https://pipedapi.kavin.rocks/
command = mpv
[THUMBNAILS]
; If you don't want thumbnails leave this as is which is set to 0
; In the event that you do want to see thumbnails set this to 1
open_thumbs = 0
image_viewer = mspaint
; This is one of the windows temp directory locations.
; For *nix operating systems it's usally located in /tmp/
temp_dir = C:\\tmp\\thumbnail
```

# Usage
``` bash
# You will be prompted to input a search term
python vids.py <option>

# You can also append the search term to the command
python vids.py <option> "search"
```

# Options
## LBRY network
`-l` for lighthouse API (searching) & librarian api (comments)

Learn more about: [LBRY](https://en.wikipedia.org/wiki/LBRY)

## PeerTube
`-pt` for sepiasearch API (searching) & PeerTube instance's API (comments) 

Learn more about: [PeerTube](https://en.wikipedia.org/wiki/PeerTube)

## Invidious: a YouTube proxy
`-i` for Invidious instance's API (searching & comments)

Learn more about: [Invidious](https://invidious.io/)

## Piped: a YouTube proxy
`-p` for Piped instance's API (searching & comments)

Learn more about: [Piped](https://github.com/TeamPiped/Piped#piped)

# Help is Appreciated!

I am not a great programmer, yet. Please write bug reports, suggestions for the inclusion of new video platforms/APIs, and code improvements!

Because many of this script's users are running *nix operating systems while I am developing it for Microsoft Windows, I'll do my best to make sure everything functions on both systems. Please file reports or make contributions.

# Contact me

- Email: zortazert@matthewevan.xyz
- Matrix: @zortazert:tchncs.de
