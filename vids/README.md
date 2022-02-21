# <img src="logo.png" alt = "vids logo" width = "45" height = "45" /> vids

# Dependencies
In order to run this script you need:
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [Python Requests](https://en.wikipedia.org/wiki/Requests_(software))

## Other Programs
Recommended:
- [mpv](https://github.com/mpv-player/mpv)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [youtube-dl](https://github.com/ytdl-org/youtube-dl)

The script takes a search term as input and returns a list of URLs of which one can be selected and opened in a program in your system's $PATH. [mpv](https://github.com/mpv-player/mpv) with [yt-dlp](https://github.com/yt-dlp/yt-dlp) or [youtube-dl](https://github.com/ytdl-org/youtube-dl) are recommend because [mpv](https://github.com/mpv-player/mpv) is minimal, not a browser and works well on lower end hardware. If you don't have or want [mpv](https://github.com/mpv-player/mpv), this script can be easily modified to open links in a browser or other program.

# Configurable Variables
There are several variables at the top of the script for adjusting its behavior.
- `command` = "Browser/video player (include space at the end)"
- `librarian_instance` = "Librarian instance"
- `invidious_instance` = "Invidious instance"
- `piped_instance` = "Piped instance"
- `pipedapi_instance` = "Piped API instance"

## Thumbnails (WIP)
This script will eventually display the thumbnail of each video link but this feature is still under development so it is set to False by default.
- `open_thumbs` = False
- `image_viewer` = "mspaint "
- `temp_dir` = "C:\\Users\\zoomer\\AppData\\Local\\Temp\\thumbnail"

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

Learn more about: [[https://invidious.io/][Invidious]]

# Piped: a YouTube proxy
`-p` for Piped instance's API (searching & comments)

Learn more about: [Piped](https://github.com/TeamPiped/Piped#piped)

# Help is Appreciated!
I am not a great programmer, yet. Please write bug reports, suggestions for the inclusion of new video platforms/APIs, and code improvements!

Because many of this script's users are running *nix operating systems while I am developing it for Microsoft Windows, I'll do my best to make sure everything functions on both systems. Please file reports or make contributions.

# TODO List:
- [x] Make a logo
- [ ] Make a proper config file using configparser
- [ ] Add thumbnail support
- [ ] Save a history of watched videos
