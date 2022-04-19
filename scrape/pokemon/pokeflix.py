import re
import os
import os.path
import requests

website = "https://www.pokeflix.tv"
downloader = "yt-dlp"
folder = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\black-white\\"

videos = '''
01 - In the Shadow of Zekrom!
/video/14-in-the-shadow-of-zekrom
/static/thumbnails/14-black-white/2.png
02 - Enter Iris and Axew!
/video/14-enter-iris-and-axew
/static/thumbnails/14-black-white/3.png
03 - A Sandile Gusher of Change!
/video/14-a-sandile-gusher-of-change
/static/thumbnails/14-black-white/4.png
04 - The Battle Club and Tepig's Choice!
/video/14-the-battle-club-and-tepigs-choice
/static/thumbnails/14-black-white/5.png
05 - Triple Leaders, Team Threats!
/video/14-triple-leaders-team-threats
/static/thumbnails/14-black-white/6.png
06 - Dreams by the Yard Full!
/video/14-dreams-by-the-yard-full
/static/thumbnails/14-black-white/7.png
07 - Snivy Plays Hard to Catch!
/video/14-snivy-plays-hard-to-catch
/static/thumbnails/14-black-white/8.png
08 - Saving Darmanitan From the Bell!
/video/14-saving-darmanitan-from-the-bell
/static/thumbnails/14-black-white/9.png
09 - The Bloom Is on Axew!
/video/14-the-bloom-is-on-axew
/static/thumbnails/14-black-white/10.png
10 - A Rival Battle for Club Champ!
/video/14-a-rival-battle-for-club-champ
/static/thumbnails/14-black-white/11.png
11 - A Home for Dwebble!
/video/14-a-home-for-dwebble
/static/thumbnails/14-black-white/12.png
12 - Here Comes the Trubbish Squad!
/video/14-here-comes-the-trubbish-squad
/static/thumbnails/14-black-white/13.png
13 - Minccino-Neat and Tidy!
/video/14-minccino-neat-and-tidy
/static/thumbnails/14-black-white/14.png
14 - A Night in the Nacrene City Museum!
/video/14-a-night-in-the-nacrene-city-museum
/static/thumbnails/14-black-white/15.png
15 - The Battle According to Lenora!
/video/14-the-battle-according-to-lenora
/static/thumbnails/14-black-white/16.png
16 - Rematch at the Nacrene Gym!
/video/14-rematch-at-the-nacrene-gym
/static/thumbnails/14-black-white/17.png
17 - Scraggy-Hatched to Be Wild!
/video/14-scraggy-hatched-to-be-wild
/static/thumbnails/14-black-white/18.png
18 - Sewaddle and Burgh in Pinwheel Forest!
/video/14-sewaddle-and-burgh-in-pinwheel-forest
/static/thumbnails/14-black-white/19.png
19 - A Connoisseur's Revenge!
/video/14-a-connoisseurs-revenge
/static/thumbnails/14-black-white/20.png
20 - Dancing With the Ducklett Trio!
/video/14-dancing-with-the-ducklett-trio
/static/thumbnails/14-black-white/21.png
21 - The Lost World of Gothitelle!
/video/14-the-lost-world-of-gothitelle
/static/thumbnails/14-black-white/22.png
22 - A Venipede Stampede!
/video/14-a-venipede-stampede
/static/thumbnails/14-black-white/23.png
23 - Battling For The Love of Bug-Types!
/video/14-battling-for-the-love-of-bug-types
/static/thumbnails/14-black-white/24.png
24 - Emolga the Irresistible!
/video/14-emolga-the-irresistible
/static/thumbnails/14-black-white/25.png
25 - Emolga and the New Volt Switch!
/video/14-emolga-and-the-new-volt-switch
/static/thumbnails/14-black-white/26.png
26 - Scare at the Litwick Mansion!
/video/14-scare-at-the-litwick-mansion
/static/thumbnails/14-black-white/27.png
27 - The Dragon Master's Path!
/video/14-the-dragon-masters-path
/static/thumbnails/14-black-white/28.png
28 - Oshawott's Lost Scalchop!
/video/14-oshawotts-lost-scalchop
/static/thumbnails/14-black-white/29.png
29 - Cottonee in Love!
/video/14-cottonee-in-love
/static/thumbnails/14-black-white/30.png
30 - A UFO for Elgyem!
/video/14-a-ufo-for-elgyem
/static/thumbnails/14-black-white/31.png
31 - Ash and Trip's Third Battle!
/video/14-ash-and-trips-third-battle
/static/thumbnails/14-black-white/32.png
32 - Facing Fear with Eyes Wide Open!
/video/14-facing-fear-with-eyes-wide-open
/static/thumbnails/14-black-white/33.png
33 - Iris and Excadrill Against the Dragon Buster!
/video/14-iris-and-excadrill-against-the-dragon-buster
/static/thumbnails/14-black-white/34.png
34 - Gotta Catch A Roggenrola!
/video/14-gotta-catch-a-roggenrola
/static/thumbnails/14-black-white/35.png
35 - Where Did You Go, Audino?
/video/14-where-did-you-go-audino
/static/thumbnails/14-black-white/36.png
36 - Archeops In The Modern World!
/video/14-archeops-in-the-modern-world
/static/thumbnails/14-black-white/37.png
37 - A Fishing Connoisseur in a Fishy Competition!
/video/14-a-fishing-connoisseur-in-a-fishy-competition
/static/thumbnails/14-black-white/38.png
38 - Movie Time! Zorua in "The Legend of the Pokemon Knight"!
/video/14-movie-time-zorua-in-the-legend-of-the-pokemon-knight
/static/thumbnails/14-black-white/39.png
39 - Reunion Battles In Nimbasa!
/video/14-reunion-battles-in-nimbasa
/static/thumbnails/14-black-white/40.png
40 - Cilan Versus Trip, Ash Versus Georgia!
/video/14-cilan-versus-trip-ash-versus-georgia
/static/thumbnails/14-black-white/41.png
41 - The Club Battle Hearts of Fury: Emolga Versus Sawk!
/video/14-the-club-battle-hearts-of-fury-emolga-versus-sawk
/static/thumbnails/14-black-white/42.png
42 - Club Battle Finale: A Hero's Outcome!
/video/14-club-battle-finale-a-heros-outcome
/static/thumbnails/14-black-white/43.png
43 - Meowth's Scrafty Tactics!
/video/14-meowths-scrafty-tactics
/static/thumbnails/14-black-white/44.png
44 - Purrloin: Sweet or Sneaky?
/video/14-purrloin-sweet-or-sneaky
/static/thumbnails/14-black-white/45.png
45 - Beheeyem, Duosion, and the Dream Thief!
/video/14-beheeyem-duosion-and-the-dream-thief
/static/thumbnails/14-black-white/46.png
46 - The Beartic Mountain Feud!
/video/14-the-beartic-mountain-feud
/static/thumbnails/14-black-white/47.png
47 - Crisis From the Underground Up!
/video/14-crisis-from-the-underground-up
/static/thumbnails/14-black-white/48.png
48 - Battle for the Underground!</h4>
/video/14-battle-for-the-underground'''

videos = videos.splitlines()

yesno = input("Try to get thumbnails (N/y): ")
if yesno == "yes" or yesno == "Y" or yesno == "y":
    get_thumb = True
else:
    get_thumb = False
if get_thumb == True:
    if os.path.exists(folder+"thumbnails"):
        pass
    else:
        os.mkdir(folder+"thumbnails")

for video in videos:
    if get_thumb == True:
        if video.startswith("/static"):
            thumbnail_data = requests.get(website+video)
            name = folder+"thumbnails\\"+video.split("/")[4]
            with open(name,"wb") as f:
                f.write(thumbnail_data.content)
            print("GETTING THUMBNAILS")
    elif video.startswith("/video"):
        os.system(f"cd {folder} && {downloader} {website+video}")
    else:
        print(video)
    
# Only usefule for RAW HTML.
#data = re.findall('<a href="(.+?)">',videos)
#for link in data:
#    link = link.replace("\" class=\"btn btn-default","")
#    print("https://www.pokeflix.tv" + link)
#    os.system(f"cd {folder} && {downloader} https://www.pokeflix.tv{link}")
