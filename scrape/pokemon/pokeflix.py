import re
import os

# Downloader
downloader = "yt-dlp"
# Folder to download to.
folder = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\black-white\\"

videos = '''
<div class="container">
		<center>
			<div id="vortexBanner" onclick="window.open('https://www.pokemon-vortex.com/?ref=pokeflix','mywindow');" style="cursor: pointer;"></div>
					</center>
		<div class="page-header">
        	<h2>Black &amp; White</h2>
        </div>
        <div class="row">
			<div class="col-sm-6 col-md-4" style="height: 260px;">
                <div class="thumbnail" style="height: 260px;">
                    <img src="/static/thumbnails/14-black-white/1.png" alt="thumbnail">
                    <div class="caption">
                        <h4>01 - In the Shadow of Zekrom!</h4>
                        <p class="desc">960,335 Views</p>
                        <p><a href="/video/14-in-the-shadow-of-zekrom" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 260px;">
                <div class="thumbnail" style="height: 260px;">
                    <img src="/static/thumbnails/14-black-white/2.png" alt="thumbnail">
                    <div class="caption">
                        <h4>02 - Enter Iris and Axew!</h4>
                        <p class="desc">1,051,810 Views</p>
                        <p><a href="/video/14-enter-iris-and-axew" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 260px;">
                <div class="thumbnail" style="height: 260px;">
                    <img src="/static/thumbnails/14-black-white/3.png" alt="thumbnail">
                    <div class="caption">
                        <h4>03 - A Sandile Gusher of Change!</h4>
                        <p class="desc">797,502 Views</p>
                        <p><a href="/video/14-a-sandile-gusher-of-change" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/4.png" alt="thumbnail">
                    <div class="caption">
                        <h4>04 - The Battle Club and Tepig's Choice!</h4>
                        <p class="desc">838,100 Views</p>
                        <p><a href="/video/14-the-battle-club-and-tepigs-choice" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/5.png" alt="thumbnail">
                    <div class="caption">
                        <h4>05 - Triple Leaders, Team Threats!</h4>
                        <p class="desc">857,996 Views</p>
                        <p><a href="/video/14-triple-leaders-team-threats" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/6.png" alt="thumbnail">
                    <div class="caption">
                        <h4>06 - Dreams by the Yard Full!</h4>
                        <p class="desc">856,860 Views</p>
                        <p><a href="/video/14-dreams-by-the-yard-full" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/7.png" alt="thumbnail">
                    <div class="caption">
                        <h4>07 - Snivy Plays Hard to Catch!</h4>
                        <p class="desc">694,185 Views</p>
                        <p><a href="/video/14-snivy-plays-hard-to-catch" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/8.png" alt="thumbnail">
                    <div class="caption">
                        <h4>08 - Saving Darmanitan From the Bell!</h4>
                        <p class="desc">523,323 Views</p>
                        <p><a href="/video/14-saving-darmanitan-from-the-bell" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/9.png" alt="thumbnail">
                    <div class="caption">
                        <h4>09 - The Bloom Is on Axew!</h4>
                        <p class="desc">515,213 Views</p>
                        <p><a href="/video/14-the-bloom-is-on-axew" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/10.png" alt="thumbnail">
                    <div class="caption">
                        <h4>10 - A Rival Battle for Club Champ!</h4>
                        <p class="desc">664,108 Views</p>
                        <p><a href="/video/14-a-rival-battle-for-club-champ" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/11.png" alt="thumbnail">
                    <div class="caption">
                        <h4>11 - A Home for Dwebble!</h4>
                        <p class="desc">482,864 Views</p>
                        <p><a href="/video/14-a-home-for-dwebble" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/12.png" alt="thumbnail">
                    <div class="caption">
                        <h4>12 - Here Comes the Trubbish Squad!</h4>
                        <p class="desc">490,885 Views</p>
                        <p><a href="/video/14-here-comes-the-trubbish-squad" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/13.png" alt="thumbnail">
                    <div class="caption">
                        <h4>13 - Minccino-Neat and Tidy!</h4>
                        <p class="desc">549,147 Views</p>
                        <p><a href="/video/14-minccino-neat-and-tidy" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/14.png" alt="thumbnail">
                    <div class="caption">
                        <h4>14 - A Night in the Nacrene City Museum!</h4>
                        <p class="desc">455,511 Views</p>
                        <p><a href="/video/14-a-night-in-the-nacrene-city-museum" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/15.png" alt="thumbnail">
                    <div class="caption">
                        <h4>15 - The Battle According to Lenora!</h4>
                        <p class="desc">461,888 Views</p>
                        <p><a href="/video/14-the-battle-according-to-lenora" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/16.png" alt="thumbnail">
                    <div class="caption">
                        <h4>16 - Rematch at the Nacrene Gym!</h4>
                        <p class="desc">493,204 Views</p>
                        <p><a href="/video/14-rematch-at-the-nacrene-gym" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/17.png" alt="thumbnail">
                    <div class="caption">
                        <h4>17 - Scraggy-Hatched to Be Wild!</h4>
                        <p class="desc">531,014 Views</p>
                        <p><a href="/video/14-scraggy-hatched-to-be-wild" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/18.png" alt="thumbnail">
                    <div class="caption">
                        <h4>18 - Sewaddle and Burgh in Pinwheel Forest!</h4>
                        <p class="desc">466,796 Views</p>
                        <p><a href="/video/14-sewaddle-and-burgh-in-pinwheel-forest" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/19.png" alt="thumbnail">
                    <div class="caption">
                        <h4>19 - A Connoisseur's Revenge!</h4>
                        <p class="desc">539,413 Views</p>
                        <p><a href="/video/14-a-connoisseurs-revenge" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/20.png" alt="thumbnail">
                    <div class="caption">
                        <h4>20 - Dancing With the Ducklett Trio!</h4>
                        <p class="desc">498,935 Views</p>
                        <p><a href="/video/14-dancing-with-the-ducklett-trio" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/21.png" alt="thumbnail">
                    <div class="caption">
                        <h4>21 - The Lost World of Gothitelle!</h4>
                        <p class="desc">401,046 Views</p>
                        <p><a href="/video/14-the-lost-world-of-gothitelle" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/22.png" alt="thumbnail">
                    <div class="caption">
                        <h4>22 - A Venipede Stampede!</h4>
                        <p class="desc">446,383 Views</p>
                        <p><a href="/video/14-a-venipede-stampede" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/23.png" alt="thumbnail">
                    <div class="caption">
                        <h4>23 - Battling For The Love of Bug-Types!</h4>
                        <p class="desc">551,078 Views</p>
                        <p><a href="/video/14-battling-for-the-love-of-bug-types" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/24.png" alt="thumbnail">
                    <div class="caption">
                        <h4>24 - Emolga the Irresistible!</h4>
                        <p class="desc">543,933 Views</p>
                        <p><a href="/video/14-emolga-the-irresistible" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/25.png" alt="thumbnail">
                    <div class="caption">
                        <h4>25 - Emolga and the New Volt Switch!</h4>
                        <p class="desc">540,187 Views</p>
                        <p><a href="/video/14-emolga-and-the-new-volt-switch" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/26.png" alt="thumbnail">
                    <div class="caption">
                        <h4>26 - Scare at the Litwick Mansion!</h4>
                        <p class="desc">455,489 Views</p>
                        <p><a href="/video/14-scare-at-the-litwick-mansion" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/27.png" alt="thumbnail">
                    <div class="caption">
                        <h4>27 - The Dragon Master's Path!</h4>
                        <p class="desc">447,727 Views</p>
                        <p><a href="/video/14-the-dragon-masters-path" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 260px;">
                <div class="thumbnail" style="height: 260px;">
                    <img src="/static/thumbnails/14-black-white/28.png" alt="thumbnail">
                    <div class="caption">
                        <h4>28 - Oshawott's Lost Scalchop!</h4>
                        <p class="desc">429,742 Views</p>
                        <p><a href="/video/14-oshawotts-lost-scalchop" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 260px;">
                <div class="thumbnail" style="height: 260px;">
                    <img src="/static/thumbnails/14-black-white/29.png" alt="thumbnail">
                    <div class="caption">
                        <h4>29 - Cottonee in Love!</h4>
                        <p class="desc">351,745 Views</p>
                        <p><a href="/video/14-cottonee-in-love" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 260px;">
                <div class="thumbnail" style="height: 260px;">
                    <img src="/static/thumbnails/14-black-white/30.png" alt="thumbnail">
                    <div class="caption">
                        <h4>30 - A UFO for Elgyem!</h4>
                        <p class="desc">320,485 Views</p>
                        <p><a href="/video/14-a-ufo-for-elgyem" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/31.png" alt="thumbnail">
                    <div class="caption">
                        <h4>31 - Ash and Trip's Third Battle!</h4>
                        <p class="desc">450,547 Views</p>
                        <p><a href="/video/14-ash-and-trips-third-battle" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/32.png" alt="thumbnail">
                    <div class="caption">
                        <h4>32 - Facing Fear with Eyes Wide Open!</h4>
                        <p class="desc">506,237 Views</p>
                        <p><a href="/video/14-facing-fear-with-eyes-wide-open" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/33.png" alt="thumbnail">
                    <div class="caption">
                        <h4>33 - Iris and Excadrill Against the Dragon Buster!</h4>
                        <p class="desc">482,893 Views</p>
                        <p><a href="/video/14-iris-and-excadrill-against-the-dragon-buster" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/34.png" alt="thumbnail">
                    <div class="caption">
                        <h4>34 - Gotta Catch A Roggenrola!</h4>
                        <p class="desc">427,326 Views</p>
                        <p><a href="/video/14-gotta-catch-a-roggenrola" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/35.png" alt="thumbnail">
                    <div class="caption">
                        <h4>35 - Where Did You Go, Audino?</h4>
                        <p class="desc">398,992 Views</p>
                        <p><a href="/video/14-where-did-you-go-audino" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/36.png" alt="thumbnail">
                    <div class="caption">
                        <h4>36 - Archeops In The Modern World!</h4>
                        <p class="desc">402,517 Views</p>
                        <p><a href="/video/14-archeops-in-the-modern-world" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/37.png" alt="thumbnail">
                    <div class="caption">
                        <h4>37 - A Fishing Connoisseur in a Fishy Competition!</h4>
                        <p class="desc">415,723 Views</p>
                        <p><a href="/video/14-a-fishing-connoisseur-in-a-fishy-competition" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/38.png" alt="thumbnail">
                    <div class="caption">
                        <h4>38 - Movie Time! Zorua in "The Legend of the Pokémon Knight"!</h4>
                        <p class="desc">425,557 Views</p>
                        <p><a href="/video/14-movie-time-zorua-in-the-legend-of-the-pokemon-knight" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/39.png" alt="thumbnail">
                    <div class="caption">
                        <h4>39 - Reunion Battles In Nimbasa!</h4>
                        <p class="desc">611,238 Views</p>
                        <p><a href="/video/14-reunion-battles-in-nimbasa" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/40.png" alt="thumbnail">
                    <div class="caption">
                        <h4>40 - Cilan Versus Trip, Ash Versus Georgia!</h4>
                        <p class="desc">596,323 Views</p>
                        <p><a href="/video/14-cilan-versus-trip-ash-versus-georgia" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/41.png" alt="thumbnail">
                    <div class="caption">
                        <h4>41 - The Club Battle Hearts of Fury: Emolga Versus Sawk!</h4>
                        <p class="desc">626,762 Views</p>
                        <p><a href="/video/14-the-club-battle-hearts-of-fury-emolga-versus-sawk" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/42.png" alt="thumbnail">
                    <div class="caption">
                        <h4>42 - Club Battle Finale: A Hero's Outcome!</h4>
                        <p class="desc">547,941 Views</p>
                        <p><a href="/video/14-club-battle-finale-a-heros-outcome" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/43.png" alt="thumbnail">
                    <div class="caption">
                        <h4>43 - Meowth's Scrafty Tactics!</h4>
                        <p class="desc">440,287 Views</p>
                        <p><a href="/video/14-meowths-scrafty-tactics" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/44.png" alt="thumbnail">
                    <div class="caption">
                        <h4>44 - Purrloin: Sweet or Sneaky?</h4>
                        <p class="desc">401,914 Views</p>
                        <p><a href="/video/14-purrloin-sweet-or-sneaky" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/45.png" alt="thumbnail">
                    <div class="caption">
                        <h4>45 - Beheeyem, Duosion, and the Dream Thief!</h4>
                        <p class="desc">417,357 Views</p>
                        <p><a href="/video/14-beheeyem-duosion-and-the-dream-thief" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/46.png" alt="thumbnail">
                    <div class="caption">
                        <h4>46 - The Beartic Mountain Feud!</h4>
                        <p class="desc">371,199 Views</p>
                        <p><a href="/video/14-the-beartic-mountain-feud" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/47.png" alt="thumbnail">
                    <div class="caption">
                        <h4>47 - Crisis From the Underground Up!</h4>
                        <p class="desc">438,025 Views</p>
                        <p><a href="/video/14-crisis-from-the-underground-up" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div><div class="col-sm-6 col-md-4" style="height: 279px;">
                <div class="thumbnail" style="height: 279px;">
                    <img src="/static/thumbnails/14-black-white/48.png" alt="thumbnail">
                    <div class="caption">
                        <h4>48 - Battle for the Underground!</h4>
                        <p class="desc">482,830 Views</p>
                        <p><a href="/video/14-battle-for-the-underground" class="btn btn-default"><span class="ion-play"></span> WATCH NOW</a></p>
                    </div>
                </div>
            </div>		</div>
    </div>
'''
data = re.findall('<a href="(.+?)">',videos)

for link in data:
    link = link.replace("\" class=\"btn btn-default","")
    print("https://www.pokeflix.tv" + link)
    os.system(f"cd {folder} && {downloader} https://www.pokeflix.tv{link}")
