import requests
import re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1'}
image_viewer = "palemoon"
dir = "C:\\SGZ_Pro\\Hobbys\\Media\\pokemon\\"

moves="""
Pound
Normal
Physical
35
40
100%
I
Karate Chop
Fighting
Physical
25
50
100%
I
Double Slap
Normal
Physical
10
15
85%
I
Comet Punch
Normal
Physical
15
18
85%
I
Mega Punch
Normal
Physical
20
80
85%
I
Pay Day
Normal
Physical
20
40
100%
I
Ice Punch
Ice
Physical
15
75
100%
I
Thunder Punch
Electric
Physical
15
75
100%
I
<td><a href="/wiki/Scratch_(move)" title="Scratch (move)">Scratch</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>11
</td>
<td><a href="/wiki/Vise_Grip_(move)" title="Vise Grip (move)">Vise Grip</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>55
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>12
</td>
<td><a href="/wiki/Guillotine_(move)" title="Guillotine (move)">Guillotine</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td><span class="explain" title="Success is calculated using a custom formula.">30%</span>
</td>
<td>I
</td></tr>
<tr>
<td>13
</td>
<td><a href="/wiki/Razor_Wind_(move)" title="Razor Wind (move)">Razor Wind</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%<span class="explain" title="75% in Generations I-II">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>14
</td>
<td><a href="/wiki/Swords_Dance_(move)" title="Swords Dance (move)">Swords Dance</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20<span class="explain" title="30 in Generations I-V">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>15
</td>
<td><a href="/wiki/Cut_(move)" title="Cut (move)">Cut</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>50
</td>
<td>95%
</td>
<td>I
</td></tr>
<tr>
<td>16
</td>
<td><a href="/wiki/Gust_(move)" title="Gust (move)">Gust</a><span class="explain" title="Normal-type move in Generation I">*</span>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>35
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>17
</td>
<td><a href="/wiki/Wing_Attack_(move)" title="Wing Attack (move)">Wing Attack</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>60<span class="explain" title="35 in Generation I">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>18
</td>
<td><a href="/wiki/Whirlwind_(move)" title="Whirlwind (move)">Whirlwind</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—<span class="explain" title="85% in Generation I, 100% in Generations II-V">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>19
</td>
<td><a href="/wiki/Fly_(move)" title="Fly (move)">Fly</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90<span class="explain" title="70 in Generations I-III">*</span>
</td>
<td>95%
</td>
<td>I
</td></tr>
<tr>
<td>20
</td>
<td><a href="/wiki/Bind_(move)" title="Bind (move)">Bind</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>15
</td>
<td>85%<span class="explain" title="75% in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>21
</td>
<td><a href="/wiki/Slam_(move)" title="Slam (move)">Slam</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>80
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>22
</td>
<td><a href="/wiki/Vine_Whip_(move)" title="Vine Whip (move)">Vine Whip</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25<span class="explain" title="10 in Generations I-III, 15 in Generations IV-V">*</span>
</td>
<td>45<span class="explain" title="35 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>23
</td>
<td><a href="/wiki/Stomp_(move)" title="Stomp (move)">Stomp</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>24
</td>
<td><a href="/wiki/Double_Kick_(move)" title="Double Kick (move)">Double Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>30
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>25
</td>
<td><a href="/wiki/Mega_Kick_(move)" title="Mega Kick (move)">Mega Kick</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>26
</td>
<td><a href="/wiki/Jump_Kick_(move)" title="Jump Kick (move)">Jump Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="25 in Generations I-IV">*</span>
</td>
<td>100<span class="explain" title="70 in Generations I-III, 85 in Generation IV">*</span>
</td>
<td>95%
</td>
<td>I
</td></tr>
<tr>
<td>27
</td>
<td><a href="/wiki/Rolling_Kick_(move)" title="Rolling Kick (move)">Rolling Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>28
</td>
<td><a href="/wiki/Sand_Attack_(move)" title="Sand Attack (move)">Sand Attack</a><span class="explain" title="Normal-type move in Generation I">*</span>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>29
</td>
<td><a href="/wiki/Headbutt_(move)" title="Headbutt (move)">Headbutt</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>70
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>30
</td>
<td><a href="/wiki/Horn_Attack_(move)" title="Horn Attack (move)">Horn Attack</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>65
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>31
</td>
<td><a href="/wiki/Fury_Attack_(move)" title="Fury Attack (move)">Fury Attack</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>15
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>32
</td>
<td><a href="/wiki/Horn_Drill_(move)" title="Horn Drill (move)">Horn Drill</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td><span class="explain" title="Success is calculated using a custom formula.">30%</span>
</td>
<td>I
</td></tr>
<tr>
<td>33
</td>
<td><a href="/wiki/Tackle_(move)" title="Tackle (move)">Tackle</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>40<span class="explain" title="35 in Generations I-IV, 50 in Generations V-VI">*</span>
</td>
<td>100%<span class="explain" title="95% in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>34
</td>
<td><a href="/wiki/Body_Slam_(move)" title="Body Slam (move)">Body Slam</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>85
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>35
</td>
<td><a href="/wiki/Wrap_(move)" title="Wrap (move)">Wrap</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>15
</td>
<td>90%<span class="explain" title="85 in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>36
</td>
<td><a href="/wiki/Take_Down_(move)" title="Take Down (move)">Take Down</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>90
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>37
</td>
<td><a href="/wiki/Thrash_(move)" title="Thrash (move)">Thrash</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="20 in Generations I-IV">*</span>
</td>
<td>120<span class="explain" title="90 in Generations I-IV">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>38
</td>
<td><a href="/wiki/Double-Edge_(move)" title="Double-Edge (move)">Double-Edge</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>120<span class="explain" title="100 in Generation I">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>39
</td>
<td><a href="/wiki/Tail_Whip_(move)" title="Tail Whip (move)">Tail Whip</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>40
</td>
<td><a href="/wiki/Poison_Sting_(move)" title="Poison Sting (move)">Poison Sting</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>15
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>41
</td>
<td><a href="/wiki/Twineedle_(move)" title="Twineedle (move)">Twineedle</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>25
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>42
</td>
<td><a href="/wiki/Pin_Missile_(move)" title="Pin Missile (move)">Pin Missile</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>25<span class="explain" title="14 in Generations I-V">*</span>
</td>
<td>95%<span class="explain" title="85% in Generations I-V">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>43
</td>
<td><a href="/wiki/Leer_(move)" title="Leer (move)">Leer</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>44
</td>
<td><a href="/wiki/Bite_(move)" title="Bite (move)">Bite</a><span class="explain" title="Normal-type move in Generation I">*</span>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>60
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>45
</td>
<td><a href="/wiki/Growl_(move)" title="Growl (move)">Growl</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>46
</td>
<td><a href="/wiki/Roar_(move)" title="Roar (move)">Roar</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generations I-V">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>47
</td>
<td><a href="/wiki/Sing_(move)" title="Sing (move)">Sing</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>55%
</td>
<td>I
</td></tr>
<tr>
<td>48
</td>
<td><a href="/wiki/Supersonic_(move)" title="Supersonic (move)">Supersonic</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>55%
</td>
<td>I
</td></tr>
<tr>
<td>49
</td>
<td><a href="/wiki/Sonic_Boom_(move)" title="Sonic Boom (move)">Sonic Boom</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>—<span class="explain" title="Always deals 20 HP damage">*</span>
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>50
</td>
<td><a href="/wiki/Disable_(move)" title="Disable (move)">Disable</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%<span class="explain" title="55% in Generations I-III, 80% in Generation IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>51
</td>
<td><a href="/wiki/Acid_(move)" title="Acid (move)">Acid</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>52
</td>
<td><a href="/wiki/Ember_(move)" title="Ember (move)">Ember</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>25
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>53
</td>
<td><a href="/wiki/Flamethrower_(move)" title="Flamethrower (move)">Flamethrower</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>90<span class="explain" title="95 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>54
</td>
<td><a href="/wiki/Mist_(move)" title="Mist (move)">Mist</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>55
</td>
<td><a href="/wiki/Water_Gun_(move)" title="Water Gun (move)">Water Gun</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>25
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>56
</td>
<td><a href="/wiki/Hydro_Pump_(move)" title="Hydro Pump (move)">Hydro Pump</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>110<span class="explain" title="120 in Generations I-V">*</span>
</td>
<td>80%
</td>
<td>I
</td></tr>
<tr>
<td>57
</td>
<td><a href="/wiki/Surf_(move)" title="Surf (move)">Surf</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>90<span class="explain" title="95 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>58
</td>
<td><a href="/wiki/Ice_Beam_(move)" title="Ice Beam (move)">Ice Beam</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90<span class="explain" title="95 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>59
</td>
<td><a href="/wiki/Blizzard_(move)" title="Blizzard (move)">Blizzard</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>110<span class="explain" title="120 in Generations I-V">*</span>
</td>
<td>70%<span class="explain" title="90% in Generation I">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>60
</td>
<td><a href="/wiki/Psybeam_(move)" title="Psybeam (move)">Psybeam</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>61
</td>
<td><a href="/wiki/Bubble_Beam_(move)" title="Bubble Beam (move)">Bubble Beam</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>62
</td>
<td><a href="/wiki/Aurora_Beam_(move)" title="Aurora Beam (move)">Aurora Beam</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>63
</td>
<td><a href="/wiki/Hyper_Beam_(move)" title="Hyper Beam (move)">Hyper Beam</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>64
</td>
<td><a href="/wiki/Peck_(move)" title="Peck (move)">Peck</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>35
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>65
</td>
<td><a href="/wiki/Drill_Peck_(move)" title="Drill Peck (move)">Drill Peck</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>80
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>66
</td>
<td><a href="/wiki/Submission_(move)" title="Submission (move)">Submission</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20<span class="explain" title="25 in Generations I-V">*</span>
</td>
<td>80
</td>
<td>80%
</td>
<td>I
</td></tr>
<tr>
<td>67
</td>
<td><a href="/wiki/Low_Kick_(move)" title="Low Kick (move)">Low Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>—<span class="explain" title="50 in Generations I-II">*</span>
</td>
<td>100%<span class="explain" title="90% in Generations I-II">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>68
</td>
<td><a href="/wiki/Counter_(move)" title="Counter (move)">Counter</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>69
</td>
<td><a href="/wiki/Seismic_Toss_(move)" title="Seismic Toss (move)">Seismic Toss</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>70
</td>
<td><a href="/wiki/Strength_(move)" title="Strength (move)">Strength</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>71
</td>
<td><a href="/wiki/Absorb_(move)" title="Absorb (move)">Absorb</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>25<span class="explain" title="20 in Generations I-III, 15 in LGPE">*</span>
</td>
<td>20<span class="explain" title="40 in LGPE">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>72
</td>
<td><a href="/wiki/Mega_Drain_(move)" title="Mega Drain (move)">Mega Drain</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15<span class="explain" title="10 in Generations I-III and LGPE">*</span>
</td>
<td>40<span class="explain" title="75 in LGPE">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>73
</td>
<td><a href="/wiki/Leech_Seed_(move)" title="Leech Seed (move)">Leech Seed</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>74
</td>
<td><a href="/wiki/Growth_(move)" title="Growth (move)">Growth</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20<span class="explain" title="40 in Generations I-V">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>75
</td>
<td><a href="/wiki/Razor_Leaf_(move)" title="Razor Leaf (move)">Razor Leaf</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>55
</td>
<td>95%
</td>
<td>I
</td></tr>
<tr>
<td>76
</td>
<td><a href="/wiki/Solar_Beam_(move)" title="Solar Beam (move)">Solar Beam</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>120<span class="explain" title="200 in LGPE">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>77
</td>
<td><a href="/wiki/Poison_Powder_(move)" title="Poison Powder (move)">Poison Powder</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>35
</td>
<td>—
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>78
</td>
<td><a href="/wiki/Stun_Spore_(move)" title="Stun Spore (move)">Stun Spore</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>79
</td>
<td><a href="/wiki/Sleep_Powder_(move)" title="Sleep Powder (move)">Sleep Powder</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>80
</td>
<td><a href="/wiki/Petal_Dance_(move)" title="Petal Dance (move)">Petal Dance</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10<span class="explain" title="20 in Generations I-IV">*</span>
</td>
<td>120<span class="explain" title="70 in Generations I-III, 90 in Generation IV">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>81
</td>
<td><a href="/wiki/String_Shot_(move)" title="String Shot (move)">String Shot</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>95%
</td>
<td>I
</td></tr>
<tr>
<td>82
</td>
<td><a href="/wiki/Dragon_Rage_(move)" title="Dragon Rage (move)">Dragon Rage</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>—<span class="explain" title="Always deals 40 HP damage">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>83
</td>
<td><a href="/wiki/Fire_Spin_(move)" title="Fire Spin (move)">Fire Spin</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>35<span class="explain" title="15 in Generations I-IV">*</span>
</td>
<td>85%<span class="explain" title="70% in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>84
</td>
<td><a href="/wiki/Thunder_Shock_(move)" title="Thunder Shock (move)">Thunder Shock</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>85
</td>
<td><a href="/wiki/Thunderbolt_(move)" title="Thunderbolt (move)">Thunderbolt</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>90<span class="explain" title="95 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>86
</td>
<td><a href="/wiki/Thunder_Wave_(move)" title="Thunder Wave (move)">Thunder Wave</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>90%<span class="explain" title="100% in Generations I-VI">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>87
</td>
<td><a href="/wiki/Thunder_(move)" title="Thunder (move)">Thunder</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>110<span class="explain" title="120 in Generations I-V">*</span>
</td>
<td>70%
</td>
<td>I
</td></tr>
<tr>
<td>88
</td>
<td><a href="/wiki/Rock_Throw_(move)" title="Rock Throw (move)">Rock Throw</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>50
</td>
<td>90%<span class="explain" title="65% in Generation I">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>89
</td>
<td><a href="/wiki/Earthquake_(move)" title="Earthquake (move)">Earthquake</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>90
</td>
<td><a href="/wiki/Fissure_(move)" title="Fissure (move)">Fissure</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td><span class="explain" title="Success is calculated using a custom formula.">30%</span>
</td>
<td>I
</td></tr>
<tr>
<td>91
</td>
<td><a href="/wiki/Dig_(move)" title="Dig (move)">Dig</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80<span class="explain" title="100 in Generation I, 60 in Generations II-III">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>92
</td>
<td><a href="/wiki/Toxic_(move)" title="Toxic (move)">Toxic</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>90%<span class="explain" title="85% in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>93
</td>
<td><a href="/wiki/Confusion_(move)" title="Confusion (move)">Confusion</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>25
</td>
<td>50
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>94
</td>
<td><a href="/wiki/Psychic_(move)" title="Psychic (move)">Psychic</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>95
</td>
<td><a href="/wiki/Hypnosis_(move)" title="Hypnosis (move)">Hypnosis</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>60%<span class="explain" title="70% in Diamond and Pearl">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>96
</td>
<td><a href="/wiki/Meditate_(move)" title="Meditate (move)">Meditate</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>97
</td>
<td><a href="/wiki/Agility_(move)" title="Agility (move)">Agility</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>98
</td>
<td><a href="/wiki/Quick_Attack_(move)" title="Quick Attack (move)">Quick Attack</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>99
</td>
<td><a href="/wiki/Rage_(move)" title="Rage (move)">Rage</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>20
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>100
</td>
<td><a href="/wiki/Teleport_(move)" title="Teleport (move)">Teleport</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>101
</td>
<td><a href="/wiki/Night_Shade_(move)" title="Night Shade (move)">Night Shade</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>102
</td>
<td><a href="/wiki/Mimic_(move)" title="Mimic (move)">Mimic</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generations I-II">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>103
</td>
<td><a href="/wiki/Screech_(move)" title="Screech (move)">Screech</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>104
</td>
<td><a href="/wiki/Double_Team_(move)" title="Double Team (move)">Double Team</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>105
</td>
<td><a href="/wiki/Recover_(move)" title="Recover (move)">Recover</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10<span class="explain" title="20 in Generations I-III">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>106
</td>
<td><a href="/wiki/Harden_(move)" title="Harden (move)">Harden</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>107
</td>
<td><a href="/wiki/Minimize_(move)" title="Minimize (move)">Minimize</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10<span class="explain" title="20 in Generations I-V">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>108
</td>
<td><a href="/wiki/Smokescreen_(move)" title="Smokescreen (move)">Smokescreen</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>109
</td>
<td><a href="/wiki/Confuse_Ray_(move)" title="Confuse Ray (move)">Confuse Ray</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>110
</td>
<td><a href="/wiki/Withdraw_(move)" title="Withdraw (move)">Withdraw</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>111
</td>
<td><a href="/wiki/Defense_Curl_(move)" title="Defense Curl (move)">Defense Curl</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>112
</td>
<td><a href="/wiki/Barrier_(move)" title="Barrier (move)">Barrier</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20<span class="explain" title="30 in Generations I-V">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>113
</td>
<td><a href="/wiki/Light_Screen_(move)" title="Light Screen (move)">Light Screen</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>114
</td>
<td><a href="/wiki/Haze_(move)" title="Haze (move)">Haze</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>115
</td>
<td><a href="/wiki/Reflect_(move)" title="Reflect (move)">Reflect</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>116
</td>
<td><a href="/wiki/Focus_Energy_(move)" title="Focus Energy (move)">Focus Energy</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>117
</td>
<td><a href="/wiki/Bide_(move)" title="Bide (move)">Bide</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generations I-III">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>118
</td>
<td><a href="/wiki/Metronome_(move)" title="Metronome (move)">Metronome</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>119
</td>
<td><a href="/wiki/Mirror_Move_(move)" title="Mirror Move (move)">Mirror Move</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>120
</td>
<td><a href="/wiki/Self-Destruct_(move)" title="Self-Destruct (move)">Self-Destruct</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>200<span class="explain" title="130 in Generation I">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>121
</td>
<td><a href="/wiki/Egg_Bomb_(move)" title="Egg Bomb (move)">Egg Bomb</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>122
</td>
<td><a href="/wiki/Lick_(move)" title="Lick (move)">Lick</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>30<span class="explain" title="20 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>123
</td>
<td><a href="/wiki/Smog_(move)" title="Smog (move)">Smog</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>30<span class="explain" title="20 in Generations I-V">*</span>
</td>
<td>70%
</td>
<td>I
</td></tr>
<tr>
<td>124
</td>
<td><a href="/wiki/Sludge_(move)" title="Sludge (move)">Sludge</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>125
</td>
<td><a href="/wiki/Bone_Club_(move)" title="Bone Club (move)">Bone Club</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>126
</td>
<td><a href="/wiki/Fire_Blast_(move)" title="Fire Blast (move)">Fire Blast</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>110<span class="explain" title="120 in Generations I-V">*</span>
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>127
</td>
<td><a href="/wiki/Waterfall_(move)" title="Waterfall (move)">Waterfall</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>128
</td>
<td><a href="/wiki/Clamp_(move)" title="Clamp (move)">Clamp</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15<span class="explain" title="10 in Generations I-IV">*</span>
</td>
<td>35
</td>
<td>85%<span class="explain" title="75% in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>129
</td>
<td><a href="/wiki/Swift_(move)" title="Swift (move)">Swift</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>130
</td>
<td><a href="/wiki/Skull_Bash_(move)" title="Skull Bash (move)">Skull Bash</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="15 in Generations I-V">*</span>
</td>
<td>130<span class="explain" title="100 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>131
</td>
<td><a href="/wiki/Spike_Cannon_(move)" title="Spike Cannon (move)">Spike Cannon</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>20
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>132
</td>
<td><a href="/wiki/Constrict_(move)" title="Constrict (move)">Constrict</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>10
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>133
</td>
<td><a href="/wiki/Amnesia_(move)" title="Amnesia (move)">Amnesia</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>134
</td>
<td><a href="/wiki/Kinesis_(move)" title="Kinesis (move)">Kinesis</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>80%
</td>
<td>I
</td></tr>
<tr>
<td>135
</td>
<td><a href="/wiki/Soft-Boiled_(move)" title="Soft-Boiled (move)">Soft-Boiled</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>136
</td>
<td><a href="/wiki/High_Jump_Kick_(move)" title="High Jump Kick (move)">High Jump Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="20 in Generations I-IV">*</span>
</td>
<td>130<span class="explain" title="85 in Generations I-III, 100 in Generation IV">*</span>
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>137
</td>
<td><a href="/wiki/Glare_(move)" title="Glare (move)">Glare</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>100%<span class="explain" title="75% in Generations I-IV, 90% in Generation V">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>138
</td>
<td><a href="/wiki/Dream_Eater_(move)" title="Dream Eater (move)">Dream Eater</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>100
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>139
</td>
<td><a href="/wiki/Poison_Gas_(move)" title="Poison Gas (move)">Poison Gas</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>90%<span class="explain" title="55% in Generations I-IV, 80% in Generation V">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>140
</td>
<td><a href="/wiki/Barrage_(move)" title="Barrage (move)">Barrage</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>15
</td>
<td>85%
</td>
<td>I
</td></tr>
<tr>
<td>141
</td>
<td><a href="/wiki/Leech_Life_(move)" title="Leech Life (move)">Leech Life</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="15 in Generations I-VI">*</span>
</td>
<td>80<span class="explain" title="20 in Generations I-VI">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>142
</td>
<td><a href="/wiki/Lovely_Kiss_(move)" title="Lovely Kiss (move)">Lovely Kiss</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>75%
</td>
<td>I
</td></tr>
<tr>
<td>143
</td>
<td><a href="/wiki/Sky_Attack_(move)" title="Sky Attack (move)">Sky Attack</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>140<span class="explain" title="200 in LGPE">*</span>
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>144
</td>
<td><a href="/wiki/Transform_(move)" title="Transform (move)">Transform</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>145
</td>
<td><a href="/wiki/Bubble_(move)" title="Bubble (move)">Bubble</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>30
</td>
<td>40<span class="explain" title="20 in Generations I-V">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>146
</td>
<td><a href="/wiki/Dizzy_Punch_(move)" title="Dizzy Punch (move)">Dizzy Punch</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>147
</td>
<td><a href="/wiki/Spore_(move)" title="Spore (move)">Spore</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>148
</td>
<td><a href="/wiki/Flash_(move)" title="Flash (move)">Flash</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%<span class="explain" title="70% in Generations I-III">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>149
</td>
<td><a href="/wiki/Psywave_(move)" title="Psywave (move)">Psywave</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%<span class="explain" title="80% in Generations I-V">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>150
</td>
<td><a href="/wiki/Splash_(move)" title="Splash (move)">Splash</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>151
</td>
<td><a href="/wiki/Acid_Armor_(move)" title="Acid Armor (move)">Acid Armor</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20<span class="explain" title="40 in Generations I-V">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>152
</td>
<td><a href="/wiki/Crabhammer_(move)" title="Crabhammer (move)">Crabhammer</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100<span class="explain" title="90 in Generations I-V">*</span>
</td>
<td>90%<span class="explain" title="85% in Generations I-IV">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>153
</td>
<td><a href="/wiki/Explosion_(move)" title="Explosion (move)">Explosion</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>250<span class="explain" title="170 in Generation I">*</span>
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>154
</td>
<td><a href="/wiki/Fury_Swipes_(move)" title="Fury Swipes (move)">Fury Swipes</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>18
</td>
<td>80%
</td>
<td>I
</td></tr>
<tr>
<td>155
</td>
<td><a href="/wiki/Bonemerang_(move)" title="Bonemerang (move)">Bonemerang</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>156
</td>
<td><a href="/wiki/Rest_(move)" title="Rest (move)">Rest</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>157
</td>
<td><a href="/wiki/Rock_Slide_(move)" title="Rock Slide (move)">Rock Slide</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>158
</td>
<td><a href="/wiki/Hyper_Fang_(move)" title="Hyper Fang (move)">Hyper Fang</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>159
</td>
<td><a href="/wiki/Sharpen_(move)" title="Sharpen (move)">Sharpen</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>160
</td>
<td><a href="/wiki/Conversion_(move)" title="Conversion (move)">Conversion</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>161
</td>
<td><a href="/wiki/Tri_Attack_(move)" title="Tri Attack (move)">Tri Attack</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>162
</td>
<td><a href="/wiki/Super_Fang_(move)" title="Super Fang (move)">Super Fang</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>90%
</td>
<td>I
</td></tr>
<tr>
<td>163
</td>
<td><a href="/wiki/Slash_(move)" title="Slash (move)">Slash</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>I
</td></tr>
<tr>
<td>164
</td>
<td><a href="/wiki/Substitute_(move)" title="Substitute (move)">Substitute</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>I
</td></tr>
<tr>
<td>165
</td>
<td><a href="/wiki/Struggle_(move)" title="Struggle (move)">Struggle</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1<span class="explain" title="10 in Generation I">*</span>
</td>
<td>50
</td>
<td>—<span class="explain" title="100% in Generations I-III">*</span>
</td>
<td>I
</td></tr>
<tr>
<td>166
</td>
<td><a href="/wiki/Sketch_(move)" title="Sketch (move)">Sketch</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>167
</td>
<td><a href="/wiki/Triple_Kick_(move)" title="Triple Kick (move)">Triple Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>10
</td>
<td>90%
</td>
<td>II
</td></tr>
<tr>
<td>168
</td>
<td><a href="/wiki/Thief_(move)" title="Thief (move)">Thief</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25<span class="explain" title="10 in Generations II-V">*</span>
</td>
<td>60<span class="explain" title="40 in Generations II-V">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>169
</td>
<td><a href="/wiki/Spider_Web_(move)" title="Spider Web (move)">Spider Web</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>170
</td>
<td><a href="/wiki/Mind_Reader_(move)" title="Mind Reader (move)">Mind Reader</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generations II-III">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>171
</td>
<td><a href="/wiki/Nightmare_(move)" title="Nightmare (move)">Nightmare</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>172
</td>
<td><a href="/wiki/Flame_Wheel_(move)" title="Flame Wheel (move)">Flame Wheel</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>60
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>173
</td>
<td><a href="/wiki/Snore_(move)" title="Snore (move)">Snore</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>50<span class="explain" title="40 in Generations II-V">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>174
</td>
<td><a href="/wiki/Curse_(move)" title="Curse (move)">Curse</a><span class="explain" title="???-type move in Generations II-IV">*</span>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>175
</td>
<td><a href="/wiki/Flail_(move)" title="Flail (move)">Flail</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>176
</td>
<td><a href="/wiki/Conversion_2_(move)" title="Conversion 2 (move)">Conversion 2</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>177
</td>
<td><a href="/wiki/Aeroblast_(move)" title="Aeroblast (move)">Aeroblast</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>95%
</td>
<td>II
</td></tr>
<tr>
<td>178
</td>
<td><a href="/wiki/Cotton_Spore_(move)" title="Cotton Spore (move)">Cotton Spore</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>100%<span class="explain" title="85% in Generations II-IV">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>179
</td>
<td><a href="/wiki/Reversal_(move)" title="Reversal (move)">Reversal</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>180
</td>
<td><a href="/wiki/Spite_(move)" title="Spite (move)">Spite</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>181
</td>
<td><a href="/wiki/Powder_Snow_(move)" title="Powder Snow (move)">Powder Snow</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>25
</td>
<td>40
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>182
</td>
<td><a href="/wiki/Protect_(move)" title="Protect (move)">Protect</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>183
</td>
<td><a href="/wiki/Mach_Punch_(move)" title="Mach Punch (move)">Mach Punch</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>184
</td>
<td><a href="/wiki/Scary_Face_(move)" title="Scary Face (move)">Scary Face</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%<span class="explain" title="90% in Generations II-IV">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>185
</td>
<td><a href="/wiki/Feint_Attack_(move)" title="Feint Attack (move)">Feint Attack</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>186
</td>
<td><a href="/wiki/Sweet_Kiss_(move)" title="Sweet Kiss (move)">Sweet Kiss</a><span class="explain" title="Normal-type move prior to Gen VI">*</span>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>75%
</td>
<td>II
</td></tr>
<tr>
<td>187
</td>
<td><a href="/wiki/Belly_Drum_(move)" title="Belly Drum (move)">Belly Drum</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>188
</td>
<td><a href="/wiki/Sludge_Bomb_(move)" title="Sludge Bomb (move)">Sludge Bomb</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>189
</td>
<td><a href="/wiki/Mud-Slap_(move)" title="Mud-Slap (move)">Mud-Slap</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>20
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>190
</td>
<td><a href="/wiki/Octazooka_(move)" title="Octazooka (move)">Octazooka</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>85%
</td>
<td>II
</td></tr>
<tr>
<td>191
</td>
<td><a href="/wiki/Spikes_(move)" title="Spikes (move)">Spikes</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>192
</td>
<td><a href="/wiki/Zap_Cannon_(move)" title="Zap Cannon (move)">Zap Cannon</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>120<span class="explain" title="100 in Generations II-III">*</span>
</td>
<td>50%
</td>
<td>II
</td></tr>
<tr>
<td>193
</td>
<td><a href="/wiki/Foresight_(move)" title="Foresight (move)">Foresight</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generations II-III">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>194
</td>
<td><a href="/wiki/Destiny_Bond_(move)" title="Destiny Bond (move)">Destiny Bond</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>195
</td>
<td><a href="/wiki/Perish_Song_(move)" title="Perish Song (move)">Perish Song</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>196
</td>
<td><a href="/wiki/Icy_Wind_(move)" title="Icy Wind (move)">Icy Wind</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>55
</td>
<td>95%
</td>
<td>II
</td></tr>
<tr>
<td>197
</td>
<td><a href="/wiki/Detect_(move)" title="Detect (move)">Detect</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>198
</td>
<td><a href="/wiki/Bone_Rush_(move)" title="Bone Rush (move)">Bone Rush</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>25
</td>
<td>90%<span class="explain" title="80% in Generations II-IV">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>199
</td>
<td><a href="/wiki/Lock-On_(move)" title="Lock-On (move)">Lock-On</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generations II-III">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>200
</td>
<td><a href="/wiki/Outrage_(move)" title="Outrage (move)">Outrage</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="15 in Generations II-IV">*</span>
</td>
<td>120<span class="explain" title="90 in Generations II-III">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>201
</td>
<td><a href="/wiki/Sandstorm_(move)" title="Sandstorm (move)">Sandstorm</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>202
</td>
<td><a href="/wiki/Giga_Drain_(move)" title="Giga Drain (move)">Giga Drain</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10<span class="explain" title="5 in Generations II-III">*</span>
</td>
<td>75<span class="explain" title="60 in Generations II-IV">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>203
</td>
<td><a href="/wiki/Endure_(move)" title="Endure (move)">Endure</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>204
</td>
<td><a href="/wiki/Charm_(move)" title="Charm (move)">Charm</a><span class="explain" title="Normal-type move prior to Gen VI">*</span>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>205
</td>
<td><a href="/wiki/Rollout_(move)" title="Rollout (move)">Rollout</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>30
</td>
<td>90%
</td>
<td>II
</td></tr>
<tr>
<td>206
</td>
<td><a href="/wiki/False_Swipe_(move)" title="False Swipe (move)">False Swipe</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>40
</td>
<td>40
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>207
</td>
<td><a href="/wiki/Swagger_(move)" title="Swagger (move)">Swagger</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>85%<span class="explain" title="90% in Generations II-VI">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>208
</td>
<td><a href="/wiki/Milk_Drink_(move)" title="Milk Drink (move)">Milk Drink</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>209
</td>
<td><a href="/wiki/Spark_(move)" title="Spark (move)">Spark</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>210
</td>
<td><a href="/wiki/Fury_Cutter_(move)" title="Fury Cutter (move)">Fury Cutter</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>40<span class="explain" title="10 in Generations II-IV, 20 in Generation V">*</span>
</td>
<td>95%
</td>
<td>II
</td></tr>
<tr>
<td>211
</td>
<td><a href="/wiki/Steel_Wing_(move)" title="Steel Wing (move)">Steel Wing</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>70
</td>
<td>90%
</td>
<td>II
</td></tr>
<tr>
<td>212
</td>
<td><a href="/wiki/Mean_Look_(move)" title="Mean Look (move)">Mean Look</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>213
</td>
<td><a href="/wiki/Attract_(move)" title="Attract (move)">Attract</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>214
</td>
<td><a href="/wiki/Sleep_Talk_(move)" title="Sleep Talk (move)">Sleep Talk</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>215
</td>
<td><a href="/wiki/Heal_Bell_(move)" title="Heal Bell (move)">Heal Bell</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>216
</td>
<td><a href="/wiki/Return_(move)" title="Return (move)">Return</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>217
</td>
<td><a href="/wiki/Present_(move)" title="Present (move)">Present</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>90%
</td>
<td>II
</td></tr>
<tr>
<td>218
</td>
<td><a href="/wiki/Frustration_(move)" title="Frustration (move)">Frustration</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>219
</td>
<td><a href="/wiki/Safeguard_(move)" title="Safeguard (move)">Safeguard</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>25
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>220
</td>
<td><a href="/wiki/Pain_Split_(move)" title="Pain Split (move)">Pain Split</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generation II">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>221
</td>
<td><a href="/wiki/Sacred_Fire_(move)" title="Sacred Fire (move)">Sacred Fire</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>95%
</td>
<td>II
</td></tr>
<tr>
<td>222
</td>
<td><a href="/wiki/Magnitude_(move)" title="Magnitude (move)">Magnitude</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>223
</td>
<td><a href="/wiki/Dynamic_Punch_(move)" title="Dynamic Punch (move)">Dynamic Punch</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>50%
</td>
<td>II
</td></tr>
<tr>
<td>224
</td>
<td><a href="/wiki/Megahorn_(move)" title="Megahorn (move)">Megahorn</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>120
</td>
<td>85%
</td>
<td>II
</td></tr>
<tr>
<td>225
</td>
<td><a href="/wiki/Dragon_Breath_(move)" title="Dragon Breath (move)">Dragon Breath</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>226
</td>
<td><a href="/wiki/Baton_Pass_(move)" title="Baton Pass (move)">Baton Pass</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>227
</td>
<td><a href="/wiki/Encore_(move)" title="Encore (move)">Encore</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>228
</td>
<td><a href="/wiki/Pursuit_(move)" title="Pursuit (move)">Pursuit</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>40
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>229
</td>
<td><a href="/wiki/Rapid_Spin_(move)" title="Rapid Spin (move)">Rapid Spin</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>40
</td>
<td>50<span class="explain" title="20 in Generations II-VII">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>230
</td>
<td><a href="/wiki/Sweet_Scent_(move)" title="Sweet Scent (move)">Sweet Scent</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>231
</td>
<td><a href="/wiki/Iron_Tail_(move)" title="Iron Tail (move)">Iron Tail</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>100
</td>
<td>75%
</td>
<td>II
</td></tr>
<tr>
<td>232
</td>
<td><a href="/wiki/Metal_Claw_(move)" title="Metal Claw (move)">Metal Claw</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>35
</td>
<td>50
</td>
<td>95%
</td>
<td>II
</td></tr>
<tr>
<td>233
</td>
<td><a href="/wiki/Vital_Throw_(move)" title="Vital Throw (move)">Vital Throw</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>234
</td>
<td><a href="/wiki/Morning_Sun_(move)" title="Morning Sun (move)">Morning Sun</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>235
</td>
<td><a href="/wiki/Synthesis_(move)" title="Synthesis (move)">Synthesis</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>236
</td>
<td><a href="/wiki/Moonlight_(move)" title="Moonlight (move)">Moonlight</a><span class="explain" title="Normal-type move prior to Gen VI">*</span>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>237
</td>
<td><a href="/wiki/Hidden_Power_(move)" title="Hidden Power (move)">Hidden Power</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>60<span class="explain" title="— in Generations II-V">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>238
</td>
<td><a href="/wiki/Cross_Chop_(move)" title="Cross Chop (move)">Cross Chop</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>80%
</td>
<td>II
</td></tr>
<tr>
<td>239
</td>
<td><a href="/wiki/Twister_(move)" title="Twister (move)">Twister</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>40
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>240
</td>
<td><a href="/wiki/Rain_Dance_(move)" title="Rain Dance (move)">Rain Dance</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>241
</td>
<td><a href="/wiki/Sunny_Day_(move)" title="Sunny Day (move)">Sunny Day</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>242
</td>
<td><a href="/wiki/Crunch_(move)" title="Crunch (move)">Crunch</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>243
</td>
<td><a href="/wiki/Mirror_Coat_(move)" title="Mirror Coat (move)">Mirror Coat</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>244
</td>
<td><a href="/wiki/Psych_Up_(move)" title="Psych Up (move)">Psych Up</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>II
</td></tr>
<tr>
<td>245
</td>
<td><a href="/wiki/Extreme_Speed_(move)" title="Extreme Speed (move)">Extreme Speed</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>80
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>246
</td>
<td><a href="/wiki/Ancient_Power_(move)" title="Ancient Power (move)">Ancient Power</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>60
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>247
</td>
<td><a href="/wiki/Shadow_Ball_(move)" title="Shadow Ball (move)">Shadow Ball</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>248
</td>
<td><a href="/wiki/Future_Sight_(move)" title="Future Sight (move)">Future Sight</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10<span class="explain" title="15 in Generations II-IV">*</span>
</td>
<td>120<span class="explain" title="80 in Generations II-IV, 100 in Generation V">*</span>
</td>
<td>100%<span class="explain" title="90% in Generations II-IV">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>249
</td>
<td><a href="/wiki/Rock_Smash_(move)" title="Rock Smash (move)">Rock Smash</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>40<span class="explain" title="20 in Generations II-III">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>250
</td>
<td><a href="/wiki/Whirlpool_(move)" title="Whirlpool (move)">Whirlpool</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>35<span class="explain" title="15 in Generations II-IV">*</span>
</td>
<td>85%<span class="explain" title="70% in Generations II-IV">*</span>
</td>
<td>II
</td></tr>
<tr>
<td>251
</td>
<td><a href="/wiki/Beat_Up_(move)" title="Beat Up (move)">Beat Up</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—<span class="explain" title="10 in Generations II-IV">*</span>
</td>
<td>100%
</td>
<td>II
</td></tr>
<tr>
<td>252
</td>
<td><a href="/wiki/Fake_Out_(move)" title="Fake Out (move)">Fake Out</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>40
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>253
</td>
<td><a href="/wiki/Uproar_(move)" title="Uproar (move)">Uproar</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90<span class="explain" title="50 in Generations III-IV">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>254
</td>
<td><a href="/wiki/Stockpile_(move)" title="Stockpile (move)">Stockpile</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20<span class="explain" title="10 in Generation III">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>255
</td>
<td><a href="/wiki/Spit_Up_(move)" title="Spit Up (move)">Spit Up</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>256
</td>
<td><a href="/wiki/Swallow_(move)" title="Swallow (move)">Swallow</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>257
</td>
<td><a href="/wiki/Heat_Wave_(move)" title="Heat Wave (move)">Heat Wave</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>95<span class="explain" title="100 in Generations III-V">*</span>
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>258
</td>
<td><a href="/wiki/Hail_(move)" title="Hail (move)">Hail</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>259
</td>
<td><a href="/wiki/Torment_(move)" title="Torment (move)">Torment</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>260
</td>
<td><a href="/wiki/Flatter_(move)" title="Flatter (move)">Flatter</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>261
</td>
<td><a href="/wiki/Will-O-Wisp_(move)" title="Will-O-Wisp (move)">Will-O-Wisp</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>85%<span class="explain" title="75% in Generations III-V">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>262
</td>
<td><a href="/wiki/Memento_(move)" title="Memento (move)">Memento</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>263
</td>
<td><a href="/wiki/Facade_(move)" title="Facade (move)">Facade</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>264
</td>
<td><a href="/wiki/Focus_Punch_(move)" title="Focus Punch (move)">Focus Punch</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>150
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>265
</td>
<td><a href="/wiki/Smelling_Salts_(move)" title="Smelling Salts (move)">Smelling Salts</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70<span class="explain" title="60 in Generations III-V">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>266
</td>
<td><a href="/wiki/Follow_Me_(move)" title="Follow Me (move)">Follow Me</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>267
</td>
<td><a href="/wiki/Nature_Power_(move)" title="Nature Power (move)">Nature Power</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>268
</td>
<td><a href="/wiki/Charge_(move)" title="Charge (move)">Charge</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>269
</td>
<td><a href="/wiki/Taunt_(move)" title="Taunt (move)">Taunt</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>270
</td>
<td><a href="/wiki/Helping_Hand_(move)" title="Helping Hand (move)">Helping Hand</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>271
</td>
<td><a href="/wiki/Trick_(move)" title="Trick (move)">Trick</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>272
</td>
<td><a href="/wiki/Role_Play_(move)" title="Role Play (move)">Role Play</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>273
</td>
<td><a href="/wiki/Wish_(move)" title="Wish (move)">Wish</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>274
</td>
<td><a href="/wiki/Assist_(move)" title="Assist (move)">Assist</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>275
</td>
<td><a href="/wiki/Ingrain_(move)" title="Ingrain (move)">Ingrain</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>276
</td>
<td><a href="/wiki/Superpower_(move)" title="Superpower (move)">Superpower</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>277
</td>
<td><a href="/wiki/Magic_Coat_(move)" title="Magic Coat (move)">Magic Coat</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>278
</td>
<td><a href="/wiki/Recycle_(move)" title="Recycle (move)">Recycle</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>279
</td>
<td><a href="/wiki/Revenge_(move)" title="Revenge (move)">Revenge</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>280
</td>
<td><a href="/wiki/Brick_Break_(move)" title="Brick Break (move)">Brick Break</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>75
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>281
</td>
<td><a href="/wiki/Yawn_(move)" title="Yawn (move)">Yawn</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>282
</td>
<td><a href="/wiki/Knock_Off_(move)" title="Knock Off (move)">Knock Off</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>65<span class="explain" title="20 in Generations III-V">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>283
</td>
<td><a href="/wiki/Endeavor_(move)" title="Endeavor (move)">Endeavor</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>284
</td>
<td><a href="/wiki/Eruption_(move)" title="Eruption (move)">Eruption</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>285
</td>
<td><a href="/wiki/Skill_Swap_(move)" title="Skill Swap (move)">Skill Swap</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>286
</td>
<td><a href="/wiki/Imprison_(move)" title="Imprison (move)">Imprison</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>287
</td>
<td><a href="/wiki/Refresh_(move)" title="Refresh (move)">Refresh</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>288
</td>
<td><a href="/wiki/Grudge_(move)" title="Grudge (move)">Grudge</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>289
</td>
<td><a href="/wiki/Snatch_(move)" title="Snatch (move)">Snatch</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>290
</td>
<td><a href="/wiki/Secret_Power_(move)" title="Secret Power (move)">Secret Power</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>291
</td>
<td><a href="/wiki/Dive_(move)" title="Dive (move)">Dive</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80<span class="explain" title="60 in Generation III">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>292
</td>
<td><a href="/wiki/Arm_Thrust_(move)" title="Arm Thrust (move)">Arm Thrust</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>15
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>293
</td>
<td><a href="/wiki/Camouflage_(move)" title="Camouflage (move)">Camouflage</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>294
</td>
<td><a href="/wiki/Tail_Glow_(move)" title="Tail Glow (move)">Tail Glow</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>295
</td>
<td><a href="/wiki/Luster_Purge_(move)" title="Luster Purge (move)">Luster Purge</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>70
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>296
</td>
<td><a href="/wiki/Mist_Ball_(move)" title="Mist Ball (move)">Mist Ball</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>70
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>297
</td>
<td><a href="/wiki/Feather_Dance_(move)" title="Feather Dance (move)">Feather Dance</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>298
</td>
<td><a href="/wiki/Teeter_Dance_(move)" title="Teeter Dance (move)">Teeter Dance</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>299
</td>
<td><a href="/wiki/Blaze_Kick_(move)" title="Blaze Kick (move)">Blaze Kick</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>300
</td>
<td><a href="/wiki/Mud_Sport_(move)" title="Mud Sport (move)">Mud Sport</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>301
</td>
<td><a href="/wiki/Ice_Ball_(move)" title="Ice Ball (move)">Ice Ball</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>30
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>302
</td>
<td><a href="/wiki/Needle_Arm_(move)" title="Needle Arm (move)">Needle Arm</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>303
</td>
<td><a href="/wiki/Slack_Off_(move)" title="Slack Off (move)">Slack Off</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>304
</td>
<td><a href="/wiki/Hyper_Voice_(move)" title="Hyper Voice (move)">Hyper Voice</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>305
</td>
<td><a href="/wiki/Poison_Fang_(move)" title="Poison Fang (move)">Poison Fang</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>50
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>306
</td>
<td><a href="/wiki/Crush_Claw_(move)" title="Crush Claw (move)">Crush Claw</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>95%
</td>
<td>III
</td></tr>
<tr>
<td>307
</td>
<td><a href="/wiki/Blast_Burn_(move)" title="Blast Burn (move)">Blast Burn</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>308
</td>
<td><a href="/wiki/Hydro_Cannon_(move)" title="Hydro Cannon (move)">Hydro Cannon</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>309
</td>
<td><a href="/wiki/Meteor_Mash_(move)" title="Meteor Mash (move)">Meteor Mash</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90<span class="explain" title="100 in Generations III-V">*</span>
</td>
<td>90%<span class="explain" title="85% in Generations III-V">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>310
</td>
<td><a href="/wiki/Astonish_(move)" title="Astonish (move)">Astonish</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>30
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>311
</td>
<td><a href="/wiki/Weather_Ball_(move)" title="Weather Ball (move)">Weather Ball</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>312
</td>
<td><a href="/wiki/Aromatherapy_(move)" title="Aromatherapy (move)">Aromatherapy</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>313
</td>
<td><a href="/wiki/Fake_Tears_(move)" title="Fake Tears (move)">Fake Tears</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>314
</td>
<td><a href="/wiki/Air_Cutter_(move)" title="Air Cutter (move)">Air Cutter</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>25
</td>
<td>60<span class="explain" title="55 in Generations III-V">*</span>
</td>
<td>95%
</td>
<td>III
</td></tr>
<tr>
<td>315
</td>
<td><a href="/wiki/Overheat_(move)" title="Overheat (move)">Overheat</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>130<span class="explain" title="140 in Generations III-V">*</span>
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>316
</td>
<td><a href="/wiki/Odor_Sleuth_(move)" title="Odor Sleuth (move)">Odor Sleuth</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generation III">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>317
</td>
<td><a href="/wiki/Rock_Tomb_(move)" title="Rock Tomb (move)">Rock Tomb</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15<span class="explain" title="10 in Generations III-V">*</span>
</td>
<td>60<span class="explain" title="50 in Generations III-V">*</span>
</td>
<td>95%<span class="explain" title="80% in Generations III-V">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>318
</td>
<td><a href="/wiki/Silver_Wind_(move)" title="Silver Wind (move)">Silver Wind</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>60
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>319
</td>
<td><a href="/wiki/Metal_Sound_(move)" title="Metal Sound (move)">Metal Sound</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>85%
</td>
<td>III
</td></tr>
<tr>
<td>320
</td>
<td><a href="/wiki/Grass_Whistle_(move)" title="Grass Whistle (move)">Grass Whistle</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>55%
</td>
<td>III
</td></tr>
<tr>
<td>321
</td>
<td><a href="/wiki/Tickle_(move)" title="Tickle (move)">Tickle</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>322
</td>
<td><a href="/wiki/Cosmic_Power_(move)" title="Cosmic Power (move)">Cosmic Power</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>323
</td>
<td><a href="/wiki/Water_Spout_(move)" title="Water Spout (move)">Water Spout</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>324
</td>
<td><a href="/wiki/Signal_Beam_(move)" title="Signal Beam (move)">Signal Beam</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>75
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>325
</td>
<td><a href="/wiki/Shadow_Punch_(move)" title="Shadow Punch (move)">Shadow Punch</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>326
</td>
<td><a href="/wiki/Extrasensory_(move)" title="Extrasensory (move)">Extrasensory</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20<span class="explain" title="30 in Generations III-V">*</span>
</td>
<td>80
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>327
</td>
<td><a href="/wiki/Sky_Uppercut_(move)" title="Sky Uppercut (move)">Sky Uppercut</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>85
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>328
</td>
<td><a href="/wiki/Sand_Tomb_(move)" title="Sand Tomb (move)">Sand Tomb</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>35<span class="explain" title="15 in Generations III-IV">*</span>
</td>
<td>85%<span class="explain" title="70 in Generations III-IV">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>329
</td>
<td><a href="/wiki/Sheer_Cold_(move)" title="Sheer Cold (move)">Sheer Cold</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td><span class="explain" title="Success is calculated using a custom formula.">30%</span>
</td>
<td>III
</td></tr>
<tr>
<td>330
</td>
<td><a href="/wiki/Muddy_Water_(move)" title="Muddy Water (move)">Muddy Water</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90<span class="explain" title="95 in Generations III-V">*</span>
</td>
<td>85%
</td>
<td>III
</td></tr>
<tr>
<td>331
</td>
<td><a href="/wiki/Bullet_Seed_(move)" title="Bullet Seed (move)">Bullet Seed</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>25<span class="explain" title="10 in Generations III-IV">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>332
</td>
<td><a href="/wiki/Aerial_Ace_(move)" title="Aerial Ace (move)">Aerial Ace</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>333
</td>
<td><a href="/wiki/Icicle_Spear_(move)" title="Icicle Spear (move)">Icicle Spear</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>25<span class="explain" title="10 in Generations III-IV">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>334
</td>
<td><a href="/wiki/Iron_Defense_(move)" title="Iron Defense (move)">Iron Defense</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>335
</td>
<td><a href="/wiki/Block_(move)" title="Block (move)">Block</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>336
</td>
<td><a href="/wiki/Howl_(move)" title="Howl (move)">Howl</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>337
</td>
<td><a href="/wiki/Dragon_Claw_(move)" title="Dragon Claw (move)">Dragon Claw</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>338
</td>
<td><a href="/wiki/Frenzy_Plant_(move)" title="Frenzy Plant (move)">Frenzy Plant</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>339
</td>
<td><a href="/wiki/Bulk_Up_(move)" title="Bulk Up (move)">Bulk Up</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>340
</td>
<td><a href="/wiki/Bounce_(move)" title="Bounce (move)">Bounce</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>85
</td>
<td>85%
</td>
<td>III
</td></tr>
<tr>
<td>341
</td>
<td><a href="/wiki/Mud_Shot_(move)" title="Mud Shot (move)">Mud Shot</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>55
</td>
<td>95%
</td>
<td>III
</td></tr>
<tr>
<td>342
</td>
<td><a href="/wiki/Poison_Tail_(move)" title="Poison Tail (move)">Poison Tail</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>50
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>343
</td>
<td><a href="/wiki/Covet_(move)" title="Covet (move)">Covet</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25<span class="explain" title="40 in Generations III-V">*</span>
</td>
<td>60<span class="explain" title="40 in Generations III-IV">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>344
</td>
<td><a href="/wiki/Volt_Tackle_(move)" title="Volt Tackle (move)">Volt Tackle</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>120
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>345
</td>
<td><a href="/wiki/Magical_Leaf_(move)" title="Magical Leaf (move)">Magical Leaf</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>346
</td>
<td><a href="/wiki/Water_Sport_(move)" title="Water Sport (move)">Water Sport</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>347
</td>
<td><a href="/wiki/Calm_Mind_(move)" title="Calm Mind (move)">Calm Mind</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>348
</td>
<td><a href="/wiki/Leaf_Blade_(move)" title="Leaf Blade (move)">Leaf Blade</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90<span class="explain" title="70 in Generation III">*</span>
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>349
</td>
<td><a href="/wiki/Dragon_Dance_(move)" title="Dragon Dance (move)">Dragon Dance</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>350
</td>
<td><a href="/wiki/Rock_Blast_(move)" title="Rock Blast (move)">Rock Blast</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>25
</td>
<td>90%<span class="explain" title="80% in Generations III-IV">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>351
</td>
<td><a href="/wiki/Shock_Wave_(move)" title="Shock Wave (move)">Shock Wave</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>III
</td></tr>
<tr>
<td>352
</td>
<td><a href="/wiki/Water_Pulse_(move)" title="Water Pulse (move)">Water Pulse</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>III
</td></tr>
<tr>
<td>353
</td>
<td><a href="/wiki/Doom_Desire_(move)" title="Doom Desire (move)">Doom Desire</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>140<span class="explain" title="120 in Generations III-IV">*</span>
</td>
<td>100%<span class="explain" title="85% in Generations III-IV">*</span>
</td>
<td>III
</td></tr>
<tr>
<td>354
</td>
<td><a href="/wiki/Psycho_Boost_(move)" title="Psycho Boost (move)">Psycho Boost</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>140
</td>
<td>90%
</td>
<td>III
</td></tr>
<tr>
<td>355
</td>
<td><a href="/wiki/Roost_(move)" title="Roost (move)">Roost</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>356
</td>
<td><a href="/wiki/Gravity_(move)" title="Gravity (move)">Gravity</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>357
</td>
<td><a href="/wiki/Miracle_Eye_(move)" title="Miracle Eye (move)">Miracle Eye</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>358
</td>
<td><a href="/wiki/Wake-Up_Slap_(move)" title="Wake-Up Slap (move)">Wake-Up Slap</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70<span class="explain" title="60 in Generations IV-V">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>359
</td>
<td><a href="/wiki/Hammer_Arm_(move)" title="Hammer Arm (move)">Hammer Arm</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>360
</td>
<td><a href="/wiki/Gyro_Ball_(move)" title="Gyro Ball (move)">Gyro Ball</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>361
</td>
<td><a href="/wiki/Healing_Wish_(move)" title="Healing Wish (move)">Healing Wish</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>362
</td>
<td><a href="/wiki/Brine_(move)" title="Brine (move)">Brine</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>363
</td>
<td><a href="/wiki/Natural_Gift_(move)" title="Natural Gift (move)">Natural Gift</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>364
</td>
<td><a href="/wiki/Feint_(move)" title="Feint (move)">Feint</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>30<span class="explain" title="50 in Generation IV">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>365
</td>
<td><a href="/wiki/Pluck_(move)" title="Pluck (move)">Pluck</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>366
</td>
<td><a href="/wiki/Tailwind_(move)" title="Tailwind (move)">Tailwind</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15<span class="explain" title="30 in Generations IV-V">*</span>
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>367
</td>
<td><a href="/wiki/Acupressure_(move)" title="Acupressure (move)">Acupressure</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>368
</td>
<td><a href="/wiki/Metal_Burst_(move)" title="Metal Burst (move)">Metal Burst</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>369
</td>
<td><a href="/wiki/U-turn_(move)" title="U-turn (move)">U-turn</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>370
</td>
<td><a href="/wiki/Close_Combat_(move)" title="Close Combat (move)">Close Combat</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>371
</td>
<td><a href="/wiki/Payback_(move)" title="Payback (move)">Payback</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>372
</td>
<td><a href="/wiki/Assurance_(move)" title="Assurance (move)">Assurance</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60<span class="explain" title="50 in Generations IV-V">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>373
</td>
<td><a href="/wiki/Embargo_(move)" title="Embargo (move)">Embargo</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>374
</td>
<td><a href="/wiki/Fling_(move)" title="Fling (move)">Fling</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>375
</td>
<td><a href="/wiki/Psycho_Shift_(move)" title="Psycho Shift (move)">Psycho Shift</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%<span class="explain" title="90% in Generations IV-V">*</span>
</td>
<td>IV
</td></tr>
<tr>
<td>376
</td>
<td><a href="/wiki/Trump_Card_(move)" title="Trump Card (move)">Trump Card</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>377
</td>
<td><a href="/wiki/Heal_Block_(move)" title="Heal Block (move)">Heal Block</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>378
</td>
<td><a href="/wiki/Wring_Out_(move)" title="Wring Out (move)">Wring Out</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>379
</td>
<td><a href="/wiki/Power_Trick_(move)" title="Power Trick (move)">Power Trick</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>380
</td>
<td><a href="/wiki/Gastro_Acid_(move)" title="Gastro Acid (move)">Gastro Acid</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>381
</td>
<td><a href="/wiki/Lucky_Chant_(move)" title="Lucky Chant (move)">Lucky Chant</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>382
</td>
<td><a href="/wiki/Me_First_(move)" title="Me First (move)">Me First</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>383
</td>
<td><a href="/wiki/Copycat_(move)" title="Copycat (move)">Copycat</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>384
</td>
<td><a href="/wiki/Power_Swap_(move)" title="Power Swap (move)">Power Swap</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>385
</td>
<td><a href="/wiki/Guard_Swap_(move)" title="Guard Swap (move)">Guard Swap</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>386
</td>
<td><a href="/wiki/Punishment_(move)" title="Punishment (move)">Punishment</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>387
</td>
<td><a href="/wiki/Last_Resort_(move)" title="Last Resort (move)">Last Resort</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>140<span class="explain" title="130 in Generation IV">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>388
</td>
<td><a href="/wiki/Worry_Seed_(move)" title="Worry Seed (move)">Worry Seed</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>389
</td>
<td><a href="/wiki/Sucker_Punch_(move)" title="Sucker Punch (move)">Sucker Punch</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>70<span class="explain" title="80 in Generations IV-VI">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>390
</td>
<td><a href="/wiki/Toxic_Spikes_(move)" title="Toxic Spikes (move)">Toxic Spikes</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>391
</td>
<td><a href="/wiki/Heart_Swap_(move)" title="Heart Swap (move)">Heart Swap</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>392
</td>
<td><a href="/wiki/Aqua_Ring_(move)" title="Aqua Ring (move)">Aqua Ring</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>393
</td>
<td><a href="/wiki/Magnet_Rise_(move)" title="Magnet Rise (move)">Magnet Rise</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>394
</td>
<td><a href="/wiki/Flare_Blitz_(move)" title="Flare Blitz (move)">Flare Blitz</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>120
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>395
</td>
<td><a href="/wiki/Force_Palm_(move)" title="Force Palm (move)">Force Palm</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>396
</td>
<td><a href="/wiki/Aura_Sphere_(move)" title="Aura Sphere (move)">Aura Sphere</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>80<span class="explain" title="90 in Generations IV-V">*</span>
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>397
</td>
<td><a href="/wiki/Rock_Polish_(move)" title="Rock Polish (move)">Rock Polish</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>398
</td>
<td><a href="/wiki/Poison_Jab_(move)" title="Poison Jab (move)">Poison Jab</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>399
</td>
<td><a href="/wiki/Dark_Pulse_(move)" title="Dark Pulse (move)">Dark Pulse</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>400
</td>
<td><a href="/wiki/Night_Slash_(move)" title="Night Slash (move)">Night Slash</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>70
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>401
</td>
<td><a href="/wiki/Aqua_Tail_(move)" title="Aqua Tail (move)">Aqua Tail</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>402
</td>
<td><a href="/wiki/Seed_Bomb_(move)" title="Seed Bomb (move)">Seed Bomb</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>403
</td>
<td><a href="/wiki/Air_Slash_(move)" title="Air Slash (move)">Air Slash</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15<span class="explain" title="20 in Generations IV-V">*</span>
</td>
<td>75
</td>
<td>95%
</td>
<td>IV
</td></tr>
<tr>
<td>404
</td>
<td><a href="/wiki/X-Scissor_(move)" title="X-Scissor (move)">X-Scissor</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>405
</td>
<td><a href="/wiki/Bug_Buzz_(move)" title="Bug Buzz (move)">Bug Buzz</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>406
</td>
<td><a href="/wiki/Dragon_Pulse_(move)" title="Dragon Pulse (move)">Dragon Pulse</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>85<span class="explain" title="90 in Generations IV-V">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>407
</td>
<td><a href="/wiki/Dragon_Rush_(move)" title="Dragon Rush (move)">Dragon Rush</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>75%
</td>
<td>IV
</td></tr>
<tr>
<td>408
</td>
<td><a href="/wiki/Power_Gem_(move)" title="Power Gem (move)">Power Gem</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>80<span class="explain" title="70 in Generations IV-V">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>409
</td>
<td><a href="/wiki/Drain_Punch_(move)" title="Drain Punch (move)">Drain Punch</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="5 in Generation IV">*</span>
</td>
<td>75<span class="explain" title="60 in Generation IV">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>410
</td>
<td><a href="/wiki/Vacuum_Wave_(move)" title="Vacuum Wave (move)">Vacuum Wave</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>411
</td>
<td><a href="/wiki/Focus_Blast_(move)" title="Focus Blast (move)">Focus Blast</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>70%
</td>
<td>IV
</td></tr>
<tr>
<td>412
</td>
<td><a href="/wiki/Energy_Ball_(move)" title="Energy Ball (move)">Energy Ball</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90<span class="explain" title="80 in Generations IV-V">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>413
</td>
<td><a href="/wiki/Brave_Bird_(move)" title="Brave Bird (move)">Brave Bird</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>120
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>414
</td>
<td><a href="/wiki/Earth_Power_(move)" title="Earth Power (move)">Earth Power</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>415
</td>
<td><a href="/wiki/Switcheroo_(move)" title="Switcheroo (move)">Switcheroo</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>416
</td>
<td><a href="/wiki/Giga_Impact_(move)" title="Giga Impact (move)">Giga Impact</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>417
</td>
<td><a href="/wiki/Nasty_Plot_(move)" title="Nasty Plot (move)">Nasty Plot</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>418
</td>
<td><a href="/wiki/Bullet_Punch_(move)" title="Bullet Punch (move)">Bullet Punch</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>419
</td>
<td><a href="/wiki/Avalanche_(move)" title="Avalanche (move)">Avalanche</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>420
</td>
<td><a href="/wiki/Ice_Shard_(move)" title="Ice Shard (move)">Ice Shard</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>421
</td>
<td><a href="/wiki/Shadow_Claw_(move)" title="Shadow Claw (move)">Shadow Claw</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>70
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>422
</td>
<td><a href="/wiki/Thunder_Fang_(move)" title="Thunder Fang (move)">Thunder Fang</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>65
</td>
<td>95%
</td>
<td>IV
</td></tr>
<tr>
<td>423
</td>
<td><a href="/wiki/Ice_Fang_(move)" title="Ice Fang (move)">Ice Fang</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>65
</td>
<td>95%
</td>
<td>IV
</td></tr>
<tr>
<td>424
</td>
<td><a href="/wiki/Fire_Fang_(move)" title="Fire Fang (move)">Fire Fang</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>65
</td>
<td>95%
</td>
<td>IV
</td></tr>
<tr>
<td>425
</td>
<td><a href="/wiki/Shadow_Sneak_(move)" title="Shadow Sneak (move)">Shadow Sneak</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>426
</td>
<td><a href="/wiki/Mud_Bomb_(move)" title="Mud Bomb (move)">Mud Bomb</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>85%
</td>
<td>IV
</td></tr>
<tr>
<td>427
</td>
<td><a href="/wiki/Psycho_Cut_(move)" title="Psycho Cut (move)">Psycho Cut</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>428
</td>
<td><a href="/wiki/Zen_Headbutt_(move)" title="Zen Headbutt (move)">Zen Headbutt</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>429
</td>
<td><a href="/wiki/Mirror_Shot_(move)" title="Mirror Shot (move)">Mirror Shot</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>85%
</td>
<td>IV
</td></tr>
<tr>
<td>430
</td>
<td><a href="/wiki/Flash_Cannon_(move)" title="Flash Cannon (move)">Flash Cannon</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>431
</td>
<td><a href="/wiki/Rock_Climb_(move)" title="Rock Climb (move)">Rock Climb</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>90
</td>
<td>85%
</td>
<td>IV
</td></tr>
<tr>
<td>432
</td>
<td><a href="/wiki/Defog_(move)" title="Defog (move)">Defog</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>433
</td>
<td><a href="/wiki/Trick_Room_(move)" title="Trick Room (move)">Trick Room</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>434
</td>
<td><a href="/wiki/Draco_Meteor_(move)" title="Draco Meteor (move)">Draco Meteor</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>130<span class="explain" title="140 in Generations IV-V">*</span>
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>435
</td>
<td><a href="/wiki/Discharge_(move)" title="Discharge (move)">Discharge</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>436
</td>
<td><a href="/wiki/Lava_Plume_(move)" title="Lava Plume (move)">Lava Plume</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>437
</td>
<td><a href="/wiki/Leaf_Storm_(move)" title="Leaf Storm (move)">Leaf Storm</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>130<span class="explain" title="140 in Generations IV-V">*</span>
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>438
</td>
<td><a href="/wiki/Power_Whip_(move)" title="Power Whip (move)">Power Whip</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>120
</td>
<td>85%
</td>
<td>IV
</td></tr>
<tr>
<td>439
</td>
<td><a href="/wiki/Rock_Wrecker_(move)" title="Rock Wrecker (move)">Rock Wrecker</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>440
</td>
<td><a href="/wiki/Cross_Poison_(move)" title="Cross Poison (move)">Cross Poison</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>441
</td>
<td><a href="/wiki/Gunk_Shot_(move)" title="Gunk Shot (move)">Gunk Shot</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>80%<span class="explain" title="70% in Generations IV-V">*</span>
</td>
<td>IV
</td></tr>
<tr>
<td>442
</td>
<td><a href="/wiki/Iron_Head_(move)" title="Iron Head (move)">Iron Head</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>443
</td>
<td><a href="/wiki/Magnet_Bomb_(move)" title="Magnet Bomb (move)">Magnet Bomb</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>444
</td>
<td><a href="/wiki/Stone_Edge_(move)" title="Stone Edge (move)">Stone Edge</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>80%
</td>
<td>IV
</td></tr>
<tr>
<td>445
</td>
<td><a href="/wiki/Captivate_(move)" title="Captivate (move)">Captivate</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>446
</td>
<td><a href="/wiki/Stealth_Rock_(move)" title="Stealth Rock (move)">Stealth Rock</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>447
</td>
<td><a href="/wiki/Grass_Knot_(move)" title="Grass Knot (move)">Grass Knot</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>448
</td>
<td><a href="/wiki/Chatter_(move)" title="Chatter (move)">Chatter</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>65<span class="explain" title="60 in Generations IV-V">*</span>
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>449
</td>
<td><a href="/wiki/Judgment_(move)" title="Judgment (move)">Judgment</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>450
</td>
<td><a href="/wiki/Bug_Bite_(move)" title="Bug Bite (move)">Bug Bite</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>451
</td>
<td><a href="/wiki/Charge_Beam_(move)" title="Charge Beam (move)">Charge Beam</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>452
</td>
<td><a href="/wiki/Wood_Hammer_(move)" title="Wood Hammer (move)">Wood Hammer</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>120
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>453
</td>
<td><a href="/wiki/Aqua_Jet_(move)" title="Aqua Jet (move)">Aqua Jet</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>40
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>454
</td>
<td><a href="/wiki/Attack_Order_(move)" title="Attack Order (move)">Attack Order</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>455
</td>
<td><a href="/wiki/Defend_Order_(move)" title="Defend Order (move)">Defend Order</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>456
</td>
<td><a href="/wiki/Heal_Order_(move)" title="Heal Order (move)">Heal Order</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>457
</td>
<td><a href="/wiki/Head_Smash_(move)" title="Head Smash (move)">Head Smash</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>80%
</td>
<td>IV
</td></tr>
<tr>
<td>458
</td>
<td><a href="/wiki/Double_Hit_(move)" title="Double Hit (move)">Double Hit</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>35
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>459
</td>
<td><a href="/wiki/Roar_of_Time_(move)" title="Roar of Time (move)">Roar of Time</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>90%
</td>
<td>IV
</td></tr>
<tr>
<td>460
</td>
<td><a href="/wiki/Spacial_Rend_(move)" title="Spacial Rend (move)">Spacial Rend</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>95%
</td>
<td>IV
</td></tr>
<tr>
<td>461
</td>
<td><a href="/wiki/Lunar_Dance_(move)" title="Lunar Dance (move)">Lunar Dance</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>IV
</td></tr>
<tr>
<td>462
</td>
<td><a href="/wiki/Crush_Grip_(move)" title="Crush Grip (move)">Crush Grip</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>463
</td>
<td><a href="/wiki/Magma_Storm_(move)" title="Magma Storm (move)">Magma Storm</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100<span class="explain" title="120 in Generations IV-V">*</span>
</td>
<td>75%<span class="explain" title="70% in Generation IV">*</span>
</td>
<td>IV
</td></tr>
<tr>
<td>464
</td>
<td><a href="/wiki/Dark_Void_(move)" title="Dark Void (move)">Dark Void</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>50%<span class="explain" title="80% in Generations IV-VI">*</span>
</td>
<td>IV
</td></tr>
<tr>
<td>465
</td>
<td><a href="/wiki/Seed_Flare_(move)" title="Seed Flare (move)">Seed Flare</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>85%
</td>
<td>IV
</td></tr>
<tr>
<td>466
</td>
<td><a href="/wiki/Ominous_Wind_(move)" title="Ominous Wind (move)">Ominous Wind</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>60
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>467
</td>
<td><a href="/wiki/Shadow_Force_(move)" title="Shadow Force (move)">Shadow Force</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>100%
</td>
<td>IV
</td></tr>
<tr>
<td>468
</td>
<td><a href="/wiki/Hone_Claws_(move)" title="Hone Claws (move)">Hone Claws</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>469
</td>
<td><a href="/wiki/Wide_Guard_(move)" title="Wide Guard (move)">Wide Guard</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>470
</td>
<td><a href="/wiki/Guard_Split_(move)" title="Guard Split (move)">Guard Split</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>471
</td>
<td><a href="/wiki/Power_Split_(move)" title="Power Split (move)">Power Split</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>472
</td>
<td><a href="/wiki/Wonder_Room_(move)" title="Wonder Room (move)">Wonder Room</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>473
</td>
<td><a href="/wiki/Psyshock_(move)" title="Psyshock (move)">Psyshock</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>474
</td>
<td><a href="/wiki/Venoshock_(move)" title="Venoshock (move)">Venoshock</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>475
</td>
<td><a href="/wiki/Autotomize_(move)" title="Autotomize (move)">Autotomize</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>476
</td>
<td><a href="/wiki/Rage_Powder_(move)" title="Rage Powder (move)">Rage Powder</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>477
</td>
<td><a href="/wiki/Telekinesis_(move)" title="Telekinesis (move)">Telekinesis</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>478
</td>
<td><a href="/wiki/Magic_Room_(move)" title="Magic Room (move)">Magic Room</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>479
</td>
<td><a href="/wiki/Smack_Down_(move)" title="Smack Down (move)">Smack Down</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>50
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>480
</td>
<td><a href="/wiki/Storm_Throw_(move)" title="Storm Throw (move)">Storm Throw</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60<span class="explain" title="40 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>481
</td>
<td><a href="/wiki/Flame_Burst_(move)" title="Flame Burst (move)">Flame Burst</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>70
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>482
</td>
<td><a href="/wiki/Sludge_Wave_(move)" title="Sludge Wave (move)">Sludge Wave</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>95
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>483
</td>
<td><a href="/wiki/Quiver_Dance_(move)" title="Quiver Dance (move)">Quiver Dance</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>484
</td>
<td><a href="/wiki/Heavy_Slam_(move)" title="Heavy Slam (move)">Heavy Slam</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>485
</td>
<td><a href="/wiki/Synchronoise_(move)" title="Synchronoise (move)">Synchronoise</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10<span class="explain" title="15 in Generation V">*</span>
</td>
<td>120<span class="explain" title="70 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>486
</td>
<td><a href="/wiki/Electro_Ball_(move)" title="Electro Ball (move)">Electro Ball</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>487
</td>
<td><a href="/wiki/Soak_(move)" title="Soak (move)">Soak</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>488
</td>
<td><a href="/wiki/Flame_Charge_(move)" title="Flame Charge (move)">Flame Charge</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>50
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>489
</td>
<td><a href="/wiki/Coil_(move)" title="Coil (move)">Coil</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>490
</td>
<td><a href="/wiki/Low_Sweep_(move)" title="Low Sweep (move)">Low Sweep</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>65<span class="explain" title="60 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>491
</td>
<td><a href="/wiki/Acid_Spray_(move)" title="Acid Spray (move)">Acid Spray</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>40
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>492
</td>
<td><a href="/wiki/Foul_Play_(move)" title="Foul Play (move)">Foul Play</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>95
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>493
</td>
<td><a href="/wiki/Simple_Beam_(move)" title="Simple Beam (move)">Simple Beam</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>494
</td>
<td><a href="/wiki/Entrainment_(move)" title="Entrainment (move)">Entrainment</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>495
</td>
<td><a href="/wiki/After_You_(move)" title="After You (move)">After You</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>496
</td>
<td><a href="/wiki/Round_(move)" title="Round (move)">Round</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>497
</td>
<td><a href="/wiki/Echoed_Voice_(move)" title="Echoed Voice (move)">Echoed Voice</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>40
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>498
</td>
<td><a href="/wiki/Chip_Away_(move)" title="Chip Away (move)">Chip Away</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>499
</td>
<td><a href="/wiki/Clear_Smog_(move)" title="Clear Smog (move)">Clear Smog</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>50
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>500
</td>
<td><a href="/wiki/Stored_Power_(move)" title="Stored Power (move)">Stored Power</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>20
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>501
</td>
<td><a href="/wiki/Quick_Guard_(move)" title="Quick Guard (move)">Quick Guard</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>502
</td>
<td><a href="/wiki/Ally_Switch_(move)" title="Ally Switch (move)">Ally Switch</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>503
</td>
<td><a href="/wiki/Scald_(move)" title="Scald (move)">Scald</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>504
</td>
<td><a href="/wiki/Shell_Smash_(move)" title="Shell Smash (move)">Shell Smash</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>505
</td>
<td><a href="/wiki/Heal_Pulse_(move)" title="Heal Pulse (move)">Heal Pulse</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>506
</td>
<td><a href="/wiki/Hex_(move)" title="Hex (move)">Hex</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65<span class="explain" title="50 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>507
</td>
<td><a href="/wiki/Sky_Drop_(move)" title="Sky Drop (move)">Sky Drop</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>508
</td>
<td><a href="/wiki/Shift_Gear_(move)" title="Shift Gear (move)">Shift Gear</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>509
</td>
<td><a href="/wiki/Circle_Throw_(move)" title="Circle Throw (move)">Circle Throw</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>510
</td>
<td><a href="/wiki/Incinerate_(move)" title="Incinerate (move)">Incinerate</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>60<span class="explain" title="30 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>511
</td>
<td><a href="/wiki/Quash_(move)" title="Quash (move)">Quash</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>512
</td>
<td><a href="/wiki/Acrobatics_(move)" title="Acrobatics (move)">Acrobatics</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>55
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>513
</td>
<td><a href="/wiki/Reflect_Type_(move)" title="Reflect Type (move)">Reflect Type</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>514
</td>
<td><a href="/wiki/Retaliate_(move)" title="Retaliate (move)">Retaliate</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>70
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>515
</td>
<td><a href="/wiki/Final_Gambit_(move)" title="Final Gambit (move)">Final Gambit</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>516
</td>
<td><a href="/wiki/Bestow_(move)" title="Bestow (move)">Bestow</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>517
</td>
<td><a href="/wiki/Inferno_(move)" title="Inferno (move)">Inferno</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>50%
</td>
<td>V
</td></tr>
<tr>
<td>518
</td>
<td><a href="/wiki/Water_Pledge_(move)" title="Water Pledge (move)">Water Pledge</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80<span class="explain" title="50 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>519
</td>
<td><a href="/wiki/Fire_Pledge_(move)" title="Fire Pledge (move)">Fire Pledge</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80<span class="explain" title="50 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>520
</td>
<td><a href="/wiki/Grass_Pledge_(move)" title="Grass Pledge (move)">Grass Pledge</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80<span class="explain" title="50 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>521
</td>
<td><a href="/wiki/Volt_Switch_(move)" title="Volt Switch (move)">Volt Switch</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>522
</td>
<td><a href="/wiki/Struggle_Bug_(move)" title="Struggle Bug (move)">Struggle Bug</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>50<span class="explain" title="30 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>523
</td>
<td><a href="/wiki/Bulldoze_(move)" title="Bulldoze (move)">Bulldoze</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>524
</td>
<td><a href="/wiki/Frost_Breath_(move)" title="Frost Breath (move)">Frost Breath</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>60<span class="explain" title="40 in Generation V">*</span>
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>525
</td>
<td><a href="/wiki/Dragon_Tail_(move)" title="Dragon Tail (move)">Dragon Tail</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>60
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>526
</td>
<td><a href="/wiki/Work_Up_(move)" title="Work Up (move)">Work Up</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>527
</td>
<td><a href="/wiki/Electroweb_(move)" title="Electroweb (move)">Electroweb</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>55
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>528
</td>
<td><a href="/wiki/Wild_Charge_(move)" title="Wild Charge (move)">Wild Charge</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>529
</td>
<td><a href="/wiki/Drill_Run_(move)" title="Drill Run (move)">Drill Run</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>530
</td>
<td><a href="/wiki/Dual_Chop_(move)" title="Dual Chop (move)">Dual Chop</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>40
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>531
</td>
<td><a href="/wiki/Heart_Stamp_(move)" title="Heart Stamp (move)">Heart Stamp</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>60
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>532
</td>
<td><a href="/wiki/Horn_Leech_(move)" title="Horn Leech (move)">Horn Leech</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>533
</td>
<td><a href="/wiki/Sacred_Sword_(move)" title="Sacred Sword (move)">Sacred Sword</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15<span class="explain" title="20 in Generation V">*</span>
</td>
<td>90
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>534
</td>
<td><a href="/wiki/Razor_Shell_(move)" title="Razor Shell (move)">Razor Shell</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>535
</td>
<td><a href="/wiki/Heat_Crash_(move)" title="Heat Crash (move)">Heat Crash</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>536
</td>
<td><a href="/wiki/Leaf_Tornado_(move)" title="Leaf Tornado (move)">Leaf Tornado</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>537
</td>
<td><a href="/wiki/Steamroller_(move)" title="Steamroller (move)">Steamroller</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>65
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>538
</td>
<td><a href="/wiki/Cotton_Guard_(move)" title="Cotton Guard (move)">Cotton Guard</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>V
</td></tr>
<tr>
<td>539
</td>
<td><a href="/wiki/Night_Daze_(move)" title="Night Daze (move)">Night Daze</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>540
</td>
<td><a href="/wiki/Psystrike_(move)" title="Psystrike (move)">Psystrike</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>541
</td>
<td><a href="/wiki/Tail_Slap_(move)" title="Tail Slap (move)">Tail Slap</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>25
</td>
<td>85%
</td>
<td>V
</td></tr>
<tr>
<td>542
</td>
<td><a href="/wiki/Hurricane_(move)" title="Hurricane (move)">Hurricane</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>110<span class="explain" title="120 in Generation V">*</span>
</td>
<td>70%
</td>
<td>V
</td></tr>
<tr>
<td>543
</td>
<td><a href="/wiki/Head_Charge_(move)" title="Head Charge (move)">Head Charge</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>120
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>544
</td>
<td><a href="/wiki/Gear_Grind_(move)" title="Gear Grind (move)">Gear Grind</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>50
</td>
<td>85%
</td>
<td>V
</td></tr>
<tr>
<td>545
</td>
<td><a href="/wiki/Searing_Shot_(move)" title="Searing Shot (move)">Searing Shot</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>546
</td>
<td><a href="/wiki/Techno_Blast_(move)" title="Techno Blast (move)">Techno Blast</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>120<span class="explain" title="85 in Generation V">*</span>
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>547
</td>
<td><a href="/wiki/Relic_Song_(move)" title="Relic Song (move)">Relic Song</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>548
</td>
<td><a href="/wiki/Secret_Sword_(move)" title="Secret Sword (move)">Secret Sword</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>549
</td>
<td><a href="/wiki/Glaciate_(move)" title="Glaciate (move)">Glaciate</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>65
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>550
</td>
<td><a href="/wiki/Bolt_Strike_(move)" title="Bolt Strike (move)">Bolt Strike</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>130
</td>
<td>85%
</td>
<td>V
</td></tr>
<tr>
<td>551
</td>
<td><a href="/wiki/Blue_Flare_(move)" title="Blue Flare (move)">Blue Flare</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>130
</td>
<td>85%
</td>
<td>V
</td></tr>
<tr>
<td>552
</td>
<td><a href="/wiki/Fiery_Dance_(move)" title="Fiery Dance (move)">Fiery Dance</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>553
</td>
<td><a href="/wiki/Freeze_Shock_(move)" title="Freeze Shock (move)">Freeze Shock</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>140
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>554
</td>
<td><a href="/wiki/Ice_Burn_(move)" title="Ice Burn (move)">Ice Burn</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>140
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>555
</td>
<td><a href="/wiki/Snarl_(move)" title="Snarl (move)">Snarl</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>55
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>556
</td>
<td><a href="/wiki/Icicle_Crash_(move)" title="Icicle Crash (move)">Icicle Crash</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>90%
</td>
<td>V
</td></tr>
<tr>
<td>557
</td>
<td><a href="/wiki/V-create_(move)" title="V-create (move)">V-create</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>180
</td>
<td>95%
</td>
<td>V
</td></tr>
<tr>
<td>558
</td>
<td><a href="/wiki/Fusion_Flare_(move)" title="Fusion Flare (move)">Fusion Flare</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>559
</td>
<td><a href="/wiki/Fusion_Bolt_(move)" title="Fusion Bolt (move)">Fusion Bolt</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>V
</td></tr>
<tr>
<td>560
</td>
<td><a href="/wiki/Flying_Press_(move)" title="Flying Press (move)">Flying Press</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100<span class="explain" title="80 in Generation VI">*</span>
</td>
<td>95%
</td>
<td>VI
</td></tr>
<tr>
<td>561
</td>
<td><a href="/wiki/Mat_Block_(move)" title="Mat Block (move)">Mat Block</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>562
</td>
<td><a href="/wiki/Belch_(move)" title="Belch (move)">Belch</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>120
</td>
<td>90%
</td>
<td>VI
</td></tr>
<tr>
<td>563
</td>
<td><a href="/wiki/Rototiller_(move)" title="Rototiller (move)">Rototiller</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>564
</td>
<td><a href="/wiki/Sticky_Web_(move)" title="Sticky Web (move)">Sticky Web</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>565
</td>
<td><a href="/wiki/Fell_Stinger_(move)" title="Fell Stinger (move)">Fell Stinger</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>25
</td>
<td>50<span class="explain" title="30 in Generation VI">*</span>
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>566
</td>
<td><a href="/wiki/Phantom_Force_(move)" title="Phantom Force (move)">Phantom Force</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>567
</td>
<td><a href="/wiki/Trick-or-Treat_(move)" title="Trick-or-Treat (move)">Trick-or-Treat</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>568
</td>
<td><a href="/wiki/Noble_Roar_(move)" title="Noble Roar (move)">Noble Roar</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>569
</td>
<td><a href="/wiki/Ion_Deluge_(move)" title="Ion Deluge (move)">Ion Deluge</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>25
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>570
</td>
<td><a href="/wiki/Parabolic_Charge_(move)" title="Parabolic Charge (move)">Parabolic Charge</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>65<span class="explain" title="50 in Generation VI">*</span>
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>571
</td>
<td><a href="/wiki/Forest%27s_Curse_(move)" title="Forest's Curse (move)">Forest's Curse</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>572
</td>
<td><a href="/wiki/Petal_Blizzard_(move)" title="Petal Blizzard (move)">Petal Blizzard</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>573
</td>
<td><a href="/wiki/Freeze-Dry_(move)" title="Freeze-Dry (move)">Freeze-Dry</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>574
</td>
<td><a href="/wiki/Disarming_Voice_(move)" title="Disarming Voice (move)">Disarming Voice</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>40
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>575
</td>
<td><a href="/wiki/Parting_Shot_(move)" title="Parting Shot (move)">Parting Shot</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>576
</td>
<td><a href="/wiki/Topsy-Turvy_(move)" title="Topsy-Turvy (move)">Topsy-Turvy</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—<span class="explain" title="100% in Generation VI">*</span>
</td>
<td>VI
</td></tr>
<tr>
<td>577
</td>
<td><a href="/wiki/Draining_Kiss_(move)" title="Draining Kiss (move)">Draining Kiss</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>578
</td>
<td><a href="/wiki/Crafty_Shield_(move)" title="Crafty Shield (move)">Crafty Shield</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>579
</td>
<td><a href="/wiki/Flower_Shield_(move)" title="Flower Shield (move)">Flower Shield</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>580
</td>
<td><a href="/wiki/Grassy_Terrain_(move)" title="Grassy Terrain (move)">Grassy Terrain</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>581
</td>
<td><a href="/wiki/Misty_Terrain_(move)" title="Misty Terrain (move)">Misty Terrain</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>582
</td>
<td><a href="/wiki/Electrify_(move)" title="Electrify (move)">Electrify</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>583
</td>
<td><a href="/wiki/Play_Rough_(move)" title="Play Rough (move)">Play Rough</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>90%
</td>
<td>VI
</td></tr>
<tr>
<td>584
</td>
<td><a href="/wiki/Fairy_Wind_(move)" title="Fairy Wind (move)">Fairy Wind</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>30
</td>
<td>40
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>585
</td>
<td><a href="/wiki/Moonblast_(move)" title="Moonblast (move)">Moonblast</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>95
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>586
</td>
<td><a href="/wiki/Boomburst_(move)" title="Boomburst (move)">Boomburst</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>140
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>587
</td>
<td><a href="/wiki/Fairy_Lock_(move)" title="Fairy Lock (move)">Fairy Lock</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>588
</td>
<td><a href="/wiki/King%27s_Shield_(move)" title="King's Shield (move)">King's Shield</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>589
</td>
<td><a href="/wiki/Play_Nice_(move)" title="Play Nice (move)">Play Nice</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>590
</td>
<td><a href="/wiki/Confide_(move)" title="Confide (move)">Confide</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>591
</td>
<td><a href="/wiki/Diamond_Storm_(move)" title="Diamond Storm (move)">Diamond Storm</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>95%
</td>
<td>VI
</td></tr>
<tr>
<td>592
</td>
<td><a href="/wiki/Steam_Eruption_(move)" title="Steam Eruption (move)">Steam Eruption</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>110
</td>
<td>95%
</td>
<td>VI
</td></tr>
<tr>
<td>593
</td>
<td><a href="/wiki/Hyperspace_Hole_(move)" title="Hyperspace Hole (move)">Hyperspace Hole</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>80
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>594
</td>
<td><a href="/wiki/Water_Shuriken_(move)" title="Water Shuriken (move)">Water Shuriken</a><span class="explain" title="Physical move in Generation VI">*</span>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>15
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>595
</td>
<td><a href="/wiki/Mystical_Fire_(move)" title="Mystical Fire (move)">Mystical Fire</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>75<span class="explain" title="65 in Generation VI">*</span>
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>596
</td>
<td><a href="/wiki/Spiky_Shield_(move)" title="Spiky Shield (move)">Spiky Shield</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>597
</td>
<td><a href="/wiki/Aromatic_Mist_(move)" title="Aromatic Mist (move)">Aromatic Mist</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>598
</td>
<td><a href="/wiki/Eerie_Impulse_(move)" title="Eerie Impulse (move)">Eerie Impulse</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>599
</td>
<td><a href="/wiki/Venom_Drench_(move)" title="Venom Drench (move)">Venom Drench</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>600
</td>
<td><a href="/wiki/Powder_(move)" title="Powder (move)">Powder</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>601
</td>
<td><a href="/wiki/Geomancy_(move)" title="Geomancy (move)">Geomancy</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>602
</td>
<td><a href="/wiki/Magnetic_Flux_(move)" title="Magnetic Flux (move)">Magnetic Flux</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>603
</td>
<td><a href="/wiki/Happy_Hour_(move)" title="Happy Hour (move)">Happy Hour</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>604
</td>
<td><a href="/wiki/Electric_Terrain_(move)" title="Electric Terrain (move)">Electric Terrain</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>605
</td>
<td><a href="/wiki/Dazzling_Gleam_(move)" title="Dazzling Gleam (move)">Dazzling Gleam</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>606
</td>
<td><a href="/wiki/Celebrate_(move)" title="Celebrate (move)">Celebrate</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>607
</td>
<td><a href="/wiki/Hold_Hands_(move)" title="Hold Hands (move)">Hold Hands</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>—
</td>
<td>VI
</td></tr>
<tr>
<td>608
</td>
<td><a href="/wiki/Baby-Doll_Eyes_(move)" title="Baby-Doll Eyes (move)">Baby-Doll Eyes</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>609
</td>
<td><a href="/wiki/Nuzzle_(move)" title="Nuzzle (move)">Nuzzle</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>20
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>610
</td>
<td><a href="/wiki/Hold_Back_(move)" title="Hold Back (move)">Hold Back</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>40
</td>
<td>40
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>611
</td>
<td><a href="/wiki/Infestation_(move)" title="Infestation (move)">Infestation</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>20
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>612
</td>
<td><a href="/wiki/Power-Up_Punch_(move)" title="Power-Up Punch (move)">Power-Up Punch</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>40
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>613
</td>
<td><a href="/wiki/Oblivion_Wing_(move)" title="Oblivion Wing (move)">Oblivion Wing</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>614
</td>
<td><a href="/wiki/Thousand_Arrows_(move)" title="Thousand Arrows (move)">Thousand Arrows</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>615
</td>
<td><a href="/wiki/Thousand_Waves_(move)" title="Thousand Waves (move)">Thousand Waves</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>616
</td>
<td><a href="/wiki/Land%27s_Wrath_(move)" title="Land's Wrath (move)">Land's Wrath</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VI
</td></tr>
<tr>
<td>617
</td>
<td><a href="/wiki/Light_of_Ruin_(move)" title="Light of Ruin (move)">Light of Ruin</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>140
</td>
<td>90%
</td>
<td>VI
</td></tr>
<tr>
<td>618
</td>
<td><a href="/wiki/Origin_Pulse_(move)" title="Origin Pulse (move)">Origin Pulse</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>110
</td>
<td>85%
</td>
<td>VI<span class="explain" title="Introduced in ORAS">*</span>
</td></tr>
<tr>
<td>619
</td>
<td><a href="/wiki/Precipice_Blades_(move)" title="Precipice Blades (move)">Precipice Blades</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>120
</td>
<td>85%
</td>
<td>VI<span class="explain" title="Introduced in ORAS">*</span>
</td></tr>
<tr>
<td>620
</td>
<td><a href="/wiki/Dragon_Ascent_(move)" title="Dragon Ascent (move)">Dragon Ascent</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>100%
</td>
<td>VI<span class="explain" title="Introduced in ORAS">*</span>
</td></tr>
<tr>
<td>621
</td>
<td><a href="/wiki/Hyperspace_Fury_(move)" title="Hyperspace Fury (move)">Hyperspace Fury</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>—
</td>
<td>VI<span class="explain" title="Introduced in ORAS">*</span>
</td></tr>
<tr>
<td>622
</td>
<td><a href="/wiki/Breakneck_Blitz_(move)" title="Breakneck Blitz (move)">Breakneck Blitz</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>623
</td>
<td><a href="/wiki/Breakneck_Blitz_(move)" title="Breakneck Blitz (move)">Breakneck Blitz</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>624
</td>
<td><a href="/wiki/All-Out_Pummeling_(move)" title="All-Out Pummeling (move)">All-Out Pummeling</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>625
</td>
<td><a href="/wiki/All-Out_Pummeling_(move)" title="All-Out Pummeling (move)">All-Out Pummeling</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>626
</td>
<td><a href="/wiki/Supersonic_Skystrike_(move)" title="Supersonic Skystrike (move)">Supersonic Skystrike</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>627
</td>
<td><a href="/wiki/Supersonic_Skystrike_(move)" title="Supersonic Skystrike (move)">Supersonic Skystrike</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>628
</td>
<td><a href="/wiki/Acid_Downpour_(move)" title="Acid Downpour (move)">Acid Downpour</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>629
</td>
<td><a href="/wiki/Acid_Downpour_(move)" title="Acid Downpour (move)">Acid Downpour</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>630
</td>
<td><a href="/wiki/Tectonic_Rage_(move)" title="Tectonic Rage (move)">Tectonic Rage</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>631
</td>
<td><a href="/wiki/Tectonic_Rage_(move)" title="Tectonic Rage (move)">Tectonic Rage</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>632
</td>
<td><a href="/wiki/Continental_Crush_(move)" title="Continental Crush (move)">Continental Crush</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>633
</td>
<td><a href="/wiki/Continental_Crush_(move)" title="Continental Crush (move)">Continental Crush</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>634
</td>
<td><a href="/wiki/Savage_Spin-Out_(move)" title="Savage Spin-Out (move)">Savage Spin-Out</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>635
</td>
<td><a href="/wiki/Savage_Spin-Out_(move)" title="Savage Spin-Out (move)">Savage Spin-Out</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>636
</td>
<td><a href="/wiki/Never-Ending_Nightmare_(move)" title="Never-Ending Nightmare (move)">Never-Ending Nightmare</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>637
</td>
<td><a href="/wiki/Never-Ending_Nightmare_(move)" title="Never-Ending Nightmare (move)">Never-Ending Nightmare</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>638
</td>
<td><a href="/wiki/Corkscrew_Crash_(move)" title="Corkscrew Crash (move)">Corkscrew Crash</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>639
</td>
<td><a href="/wiki/Corkscrew_Crash_(move)" title="Corkscrew Crash (move)">Corkscrew Crash</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>640
</td>
<td><a href="/wiki/Inferno_Overdrive_(move)" title="Inferno Overdrive (move)">Inferno Overdrive</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>641
</td>
<td><a href="/wiki/Inferno_Overdrive_(move)" title="Inferno Overdrive (move)">Inferno Overdrive</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>642
</td>
<td><a href="/wiki/Hydro_Vortex_(move)" title="Hydro Vortex (move)">Hydro Vortex</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>643
</td>
<td><a href="/wiki/Hydro_Vortex_(move)" title="Hydro Vortex (move)">Hydro Vortex</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>644
</td>
<td><a href="/wiki/Bloom_Doom_(move)" title="Bloom Doom (move)">Bloom Doom</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>645
</td>
<td><a href="/wiki/Bloom_Doom_(move)" title="Bloom Doom (move)">Bloom Doom</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>646
</td>
<td><a href="/wiki/Gigavolt_Havoc_(move)" title="Gigavolt Havoc (move)">Gigavolt Havoc</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>647
</td>
<td><a href="/wiki/Gigavolt_Havoc_(move)" title="Gigavolt Havoc (move)">Gigavolt Havoc</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>648
</td>
<td><a href="/wiki/Shattered_Psyche_(move)" title="Shattered Psyche (move)">Shattered Psyche</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>649
</td>
<td><a href="/wiki/Shattered_Psyche_(move)" title="Shattered Psyche (move)">Shattered Psyche</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>650
</td>
<td><a href="/wiki/Subzero_Slammer_(move)" title="Subzero Slammer (move)">Subzero Slammer</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>651
</td>
<td><a href="/wiki/Subzero_Slammer_(move)" title="Subzero Slammer (move)">Subzero Slammer</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>652
</td>
<td><a href="/wiki/Devastating_Drake_(move)" title="Devastating Drake (move)">Devastating Drake</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>653
</td>
<td><a href="/wiki/Devastating_Drake_(move)" title="Devastating Drake (move)">Devastating Drake</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>654
</td>
<td><a href="/wiki/Black_Hole_Eclipse_(move)" title="Black Hole Eclipse (move)">Black Hole Eclipse</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>655
</td>
<td><a href="/wiki/Black_Hole_Eclipse_(move)" title="Black Hole Eclipse (move)">Black Hole Eclipse</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>656
</td>
<td><a href="/wiki/Twinkle_Tackle_(move)" title="Twinkle Tackle (move)">Twinkle Tackle</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>657
</td>
<td><a href="/wiki/Twinkle_Tackle_(move)" title="Twinkle Tackle (move)">Twinkle Tackle</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>658
</td>
<td><a href="/wiki/Catastropika_(move)" title="Catastropika (move)">Catastropika</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>210
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>659
</td>
<td><a href="/wiki/Shore_Up_(move)" title="Shore Up (move)">Shore Up</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>660
</td>
<td><a href="/wiki/First_Impression_(move)" title="First Impression (move)">First Impression</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>661
</td>
<td><a href="/wiki/Baneful_Bunker_(move)" title="Baneful Bunker (move)">Baneful Bunker</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>662
</td>
<td><a href="/wiki/Spirit_Shackle_(move)" title="Spirit Shackle (move)">Spirit Shackle</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>663
</td>
<td><a href="/wiki/Darkest_Lariat_(move)" title="Darkest Lariat (move)">Darkest Lariat</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>664
</td>
<td><a href="/wiki/Sparkling_Aria_(move)" title="Sparkling Aria (move)">Sparkling Aria</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>665
</td>
<td><a href="/wiki/Ice_Hammer_(move)" title="Ice Hammer (move)">Ice Hammer</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>90%
</td>
<td>VII
</td></tr>
<tr>
<td>666
</td>
<td><a href="/wiki/Floral_Healing_(move)" title="Floral Healing (move)">Floral Healing</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>667
</td>
<td><a href="/wiki/High_Horsepower_(move)" title="High Horsepower (move)">High Horsepower</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>95
</td>
<td>95%
</td>
<td>VII
</td></tr>
<tr>
<td>668
</td>
<td><a href="/wiki/Strength_Sap_(move)" title="Strength Sap (move)">Strength Sap</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>669
</td>
<td><a href="/wiki/Solar_Blade_(move)" title="Solar Blade (move)">Solar Blade</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>125
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>670
</td>
<td><a href="/wiki/Leafage_(move)" title="Leafage (move)">Leafage</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>40
</td>
<td>40
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>671
</td>
<td><a href="/wiki/Spotlight_(move)" title="Spotlight (move)">Spotlight</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>672
</td>
<td><a href="/wiki/Toxic_Thread_(move)" title="Toxic Thread (move)">Toxic Thread</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>673
</td>
<td><a href="/wiki/Laser_Focus_(move)" title="Laser Focus (move)">Laser Focus</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>30
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>674
</td>
<td><a href="/wiki/Gear_Up_(move)" title="Gear Up (move)">Gear Up</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>675
</td>
<td><a href="/wiki/Throat_Chop_(move)" title="Throat Chop (move)">Throat Chop</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>676
</td>
<td><a href="/wiki/Pollen_Puff_(move)" title="Pollen Puff (move)">Pollen Puff</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>677
</td>
<td><a href="/wiki/Anchor_Shot_(move)" title="Anchor Shot (move)">Anchor Shot</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>80
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>678
</td>
<td><a href="/wiki/Psychic_Terrain_(move)" title="Psychic Terrain (move)">Psychic Terrain</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>679
</td>
<td><a href="/wiki/Lunge_(move)" title="Lunge (move)">Lunge</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>680
</td>
<td><a href="/wiki/Fire_Lash_(move)" title="Fire Lash (move)">Fire Lash</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>681
</td>
<td><a href="/wiki/Power_Trip_(move)" title="Power Trip (move)">Power Trip</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>20
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>682
</td>
<td><a href="/wiki/Burn_Up_(move)" title="Burn Up (move)">Burn Up</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>130
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>683
</td>
<td><a href="/wiki/Speed_Swap_(move)" title="Speed Swap (move)">Speed Swap</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>684
</td>
<td><a href="/wiki/Smart_Strike_(move)" title="Smart Strike (move)">Smart Strike</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>685
</td>
<td><a href="/wiki/Purify_(move)" title="Purify (move)">Purify</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>686
</td>
<td><a href="/wiki/Revelation_Dance_(move)" title="Revelation Dance (move)">Revelation Dance</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>687
</td>
<td><a href="/wiki/Core_Enforcer_(move)" title="Core Enforcer (move)">Core Enforcer</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>100
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>688
</td>
<td><a href="/wiki/Trop_Kick_(move)" title="Trop Kick (move)">Trop Kick</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>70
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>689
</td>
<td><a href="/wiki/Instruct_(move)" title="Instruct (move)">Instruct</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>690
</td>
<td><a href="/wiki/Beak_Blast_(move)" title="Beak Blast (move)">Beak Blast</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>100
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>691
</td>
<td><a href="/wiki/Clanging_Scales_(move)" title="Clanging Scales (move)">Clanging Scales</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>110
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>692
</td>
<td><a href="/wiki/Dragon_Hammer_(move)" title="Dragon Hammer (move)">Dragon Hammer</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>693
</td>
<td><a href="/wiki/Brutal_Swing_(move)" title="Brutal Swing (move)">Brutal Swing</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>694
</td>
<td><a href="/wiki/Aurora_Veil_(move)" title="Aurora Veil (move)">Aurora Veil</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>695
</td>
<td><a href="/wiki/Sinister_Arrow_Raid_(move)" title="Sinister Arrow Raid (move)">Sinister Arrow Raid</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>180
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>696
</td>
<td><a href="/wiki/Malicious_Moonsault_(move)" title="Malicious Moonsault (move)">Malicious Moonsault</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>180
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>697
</td>
<td><a href="/wiki/Oceanic_Operetta_(move)" title="Oceanic Operetta (move)">Oceanic Operetta</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>195
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>698
</td>
<td><a href="/wiki/Guardian_of_Alola_(move)" title="Guardian of Alola (move)">Guardian of Alola</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>699
</td>
<td><a href="/wiki/Soul-Stealing_7-Star_Strike_(move)" title="Soul-Stealing 7-Star Strike (move)">Soul-Stealing 7-Star Strike</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>195
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>700
</td>
<td><a href="/wiki/Stoked_Sparksurfer_(move)" title="Stoked Sparksurfer (move)">Stoked Sparksurfer</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>175
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>701
</td>
<td><a href="/wiki/Pulverizing_Pancake_(move)" title="Pulverizing Pancake (move)">Pulverizing Pancake</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>210
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>702
</td>
<td><a href="/wiki/Extreme_Evoboost_(move)" title="Extreme Evoboost (move)">Extreme Evoboost</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>1
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>703
</td>
<td><a href="/wiki/Genesis_Supernova_(move)" title="Genesis Supernova (move)">Genesis Supernova</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>185
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>704
</td>
<td><a href="/wiki/Shell_Trap_(move)" title="Shell Trap (move)">Shell Trap</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>705
</td>
<td><a href="/wiki/Fleur_Cannon_(move)" title="Fleur Cannon (move)">Fleur Cannon</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>130
</td>
<td>90%
</td>
<td>VII
</td></tr>
<tr>
<td>706
</td>
<td><a href="/wiki/Psychic_Fangs_(move)" title="Psychic Fangs (move)">Psychic Fangs</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>707
</td>
<td><a href="/wiki/Stomping_Tantrum_(move)" title="Stomping Tantrum (move)">Stomping Tantrum</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>708
</td>
<td><a href="/wiki/Shadow_Bone_(move)" title="Shadow Bone (move)">Shadow Bone</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>709
</td>
<td><a href="/wiki/Accelerock_(move)" title="Accelerock (move)">Accelerock</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>40
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>710
</td>
<td><a href="/wiki/Liquidation_(move)" title="Liquidation (move)">Liquidation</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>711
</td>
<td><a href="/wiki/Prismatic_Laser_(move)" title="Prismatic Laser (move)">Prismatic Laser</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>160
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>712
</td>
<td><a href="/wiki/Spectral_Thief_(move)" title="Spectral Thief (move)">Spectral Thief</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>713
</td>
<td><a href="/wiki/Sunsteel_Strike_(move)" title="Sunsteel Strike (move)">Sunsteel Strike</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>714
</td>
<td><a href="/wiki/Moongeist_Beam_(move)" title="Moongeist Beam (move)">Moongeist Beam</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>715
</td>
<td><a href="/wiki/Tearful_Look_(move)" title="Tearful Look (move)">Tearful Look</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>716
</td>
<td><a href="/wiki/Zing_Zap_(move)" title="Zing Zap (move)">Zing Zap</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>717
</td>
<td><a href="/wiki/Nature%27s_Madness_(move)" title="Nature's Madness (move)">Nature's Madness</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>90%
</td>
<td>VII
</td></tr>
<tr>
<td>718
</td>
<td><a href="/wiki/Multi-Attack_(move)" title="Multi-Attack (move)">Multi-Attack</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>120<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>100%
</td>
<td>VII
</td></tr>
<tr>
<td>719
</td>
<td><a href="/wiki/10,000,000_Volt_Thunderbolt_(move)" title="10,000,000 Volt Thunderbolt (move)">10,000,000 Volt Thunderbolt</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>195
</td>
<td>—
</td>
<td>VII
</td></tr>
<tr>
<td>720
</td>
<td><a href="/wiki/Mind_Blown_(move)" title="Mind Blown (move)">Mind Blown</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>721
</td>
<td><a href="/wiki/Plasma_Fists_(move)" title="Plasma Fists (move)">Plasma Fists</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>100
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>722
</td>
<td><a href="/wiki/Photon_Geyser_(move)" title="Photon Geyser (move)">Photon Geyser</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>723
</td>
<td><a href="/wiki/Light_That_Burns_the_Sky_(move)" title="Light That Burns the Sky (move)">Light That Burns the Sky</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>200
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>724
</td>
<td><a href="/wiki/Searing_Sunraze_Smash_(move)" title="Searing Sunraze Smash (move)">Searing Sunraze Smash</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>200
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>725
</td>
<td><a href="/wiki/Menacing_Moonraze_Maelstrom_(move)" title="Menacing Moonraze Maelstrom (move)">Menacing Moonraze Maelstrom</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>200
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>726
</td>
<td><a href="/wiki/Let%27s_Snuggle_Forever_(move)" title="Let's Snuggle Forever (move)">Let's Snuggle Forever</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>190
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>727
</td>
<td><a href="/wiki/Splintered_Stormshards_(move)" title="Splintered Stormshards (move)">Splintered Stormshards</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>1
</td>
<td>190
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>728
</td>
<td><a href="/wiki/Clangorous_Soulblaze_(move)" title="Clangorous Soulblaze (move)">Clangorous Soulblaze</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>1
</td>
<td>185
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in USUM">*</span>
</td></tr>
<tr>
<td>729
</td>
<td><a href="/wiki/Zippy_Zap_(move)" title="Zippy Zap (move)">Zippy Zap</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>80<span class="explain" title="50 in Generation VII">*</span>
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>730
</td>
<td><a href="/wiki/Splishy_Splash_(move)" title="Splishy Splash (move)">Splishy Splash</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>731
</td>
<td><a href="/wiki/Floaty_Fall_(move)" title="Floaty Fall (move)">Floaty Fall</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>90
</td>
<td>95%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>732
</td>
<td><a href="/wiki/Pika_Papow_(move)" title="Pika Papow (move)">Pika Papow</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>733
</td>
<td><a href="/wiki/Bouncy_Bubble_(move)" title="Bouncy Bubble (move)">Bouncy Bubble</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>60<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>734
</td>
<td><a href="/wiki/Buzzy_Buzz_(move)" title="Buzzy Buzz (move)">Buzzy Buzz</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>60<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>735
</td>
<td><a href="/wiki/Sizzly_Slide_(move)" title="Sizzly Slide (move)">Sizzly Slide</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>60<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>736
</td>
<td><a href="/wiki/Glitzy_Glow_(move)" title="Glitzy Glow (move)">Glitzy Glow</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>95%<span class="explain" title="100% in Generation VII">*</span>
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>737
</td>
<td><a href="/wiki/Baddy_Bad_(move)" title="Baddy Bad (move)">Baddy Bad</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>95%<span class="explain" title="100% in Generation VII">*</span>
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>738
</td>
<td><a href="/wiki/Sappy_Seed_(move)" title="Sappy Seed (move)">Sappy Seed</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>100<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>90%<span class="explain" title="100% in Generation VII">*</span>
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>739
</td>
<td><a href="/wiki/Freezy_Frost_(move)" title="Freezy Frost (move)">Freezy Frost</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>100<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>90%<span class="explain" title="100% in Generation VII">*</span>
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>740
</td>
<td><a href="/wiki/Sparkly_Swirl_(move)" title="Sparkly Swirl (move)">Sparkly Swirl</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5<span class="explain" title="15 in Generation VII">*</span>
</td>
<td>120<span class="explain" title="90 in Generation VII">*</span>
</td>
<td>85%<span class="explain" title="100% in Generation VII">*</span>
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>741
</td>
<td><a href="/wiki/Veevee_Volley_(move)" title="Veevee Volley (move)">Veevee Volley</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>—
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>742
</td>
<td><a href="/wiki/Double_Iron_Bash_(move)" title="Double Iron Bash (move)">Double Iron Bash</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>60
</td>
<td>100%
</td>
<td>VII<span class="explain" title="Introduced in LGPE">*</span>
</td></tr>
<tr>
<td>743
</td>
<td><a href="/wiki/Max_Guard_(move)" title="Max Guard (move)">Max Guard</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>744
</td>
<td><a href="/wiki/Dynamax_Cannon_(move)" title="Dynamax Cannon (move)">Dynamax Cannon</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>745
</td>
<td><a href="/wiki/Snipe_Shot_(move)" title="Snipe Shot (move)">Snipe Shot</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>746
</td>
<td><a href="/wiki/Jaw_Lock_(move)" title="Jaw Lock (move)">Jaw Lock</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>747
</td>
<td><a href="/wiki/Stuff_Cheeks_(move)" title="Stuff Cheeks (move)">Stuff Cheeks</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>748
</td>
<td><a href="/wiki/No_Retreat_(move)" title="No Retreat (move)">No Retreat</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>749
</td>
<td><a href="/wiki/Tar_Shot_(move)" title="Tar Shot (move)">Tar Shot</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>750
</td>
<td><a href="/wiki/Magic_Powder_(move)" title="Magic Powder (move)">Magic Powder</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>20
</td>
<td>—
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>751
</td>
<td><a href="/wiki/Dragon_Darts_(move)" title="Dragon Darts (move)">Dragon Darts</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>752
</td>
<td><a href="/wiki/Teatime_(move)" title="Teatime (move)">Teatime</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>753
</td>
<td><a href="/wiki/Octolock_(move)" title="Octolock (move)">Octolock</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>754
</td>
<td><a href="/wiki/Bolt_Beak_(move)" title="Bolt Beak (move)">Bolt Beak</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>755
</td>
<td><a href="/wiki/Fishious_Rend_(move)" title="Fishious Rend (move)">Fishious Rend</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>85
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>756
</td>
<td><a href="/wiki/Court_Change_(move)" title="Court Change (move)">Court Change</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>757
</td>
<td><a href="/wiki/Max_Flare_(move)" title="Max Flare (move)">Max Flare</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>758
</td>
<td><a href="/wiki/Max_Flutterby_(move)" title="Max Flutterby (move)">Max Flutterby</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>759
</td>
<td><a href="/wiki/Max_Lightning_(move)" title="Max Lightning (move)">Max Lightning</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>760
</td>
<td><a href="/wiki/Max_Strike_(move)" title="Max Strike (move)">Max Strike</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>761
</td>
<td><a href="/wiki/Max_Knuckle_(move)" title="Max Knuckle (move)">Max Knuckle</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>762
</td>
<td><a href="/wiki/Max_Phantasm_(move)" title="Max Phantasm (move)">Max Phantasm</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>763
</td>
<td><a href="/wiki/Max_Hailstorm_(move)" title="Max Hailstorm (move)">Max Hailstorm</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>764
</td>
<td><a href="/wiki/Max_Ooze_(move)" title="Max Ooze (move)">Max Ooze</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>765
</td>
<td><a href="/wiki/Max_Geyser_(move)" title="Max Geyser (move)">Max Geyser</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>766
</td>
<td><a href="/wiki/Max_Airstream_(move)" title="Max Airstream (move)">Max Airstream</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>767
</td>
<td><a href="/wiki/Max_Starfall_(move)" title="Max Starfall (move)">Max Starfall</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>768
</td>
<td><a href="/wiki/Max_Wyrmwind_(move)" title="Max Wyrmwind (move)">Max Wyrmwind</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>769
</td>
<td><a href="/wiki/Max_Mindstorm_(move)" title="Max Mindstorm (move)">Max Mindstorm</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>770
</td>
<td><a href="/wiki/Max_Rockfall_(move)" title="Max Rockfall (move)">Max Rockfall</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>771
</td>
<td><a href="/wiki/Max_Quake_(move)" title="Max Quake (move)">Max Quake</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>772
</td>
<td><a href="/wiki/Max_Darkness_(move)" title="Max Darkness (move)">Max Darkness</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>773
</td>
<td><a href="/wiki/Max_Overgrowth_(move)" title="Max Overgrowth (move)">Max Overgrowth</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>774
</td>
<td><a href="/wiki/Max_Steelspike_(move)" title="Max Steelspike (move)">Max Steelspike</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#68A090" align="center"><a href="/wiki/%3F%3F%3F_move" class="mw-redirect" title="??? move"><span style="color:#FFF;">???</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>775
</td>
<td><a href="/wiki/Clangorous_Soul_(move)" title="Clangorous Soul (move)">Clangorous Soul</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>5
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>776
</td>
<td><a href="/wiki/Body_Press_(move)" title="Body Press (move)">Body Press</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>777
</td>
<td><a href="/wiki/Decorate_(move)" title="Decorate (move)">Decorate</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>15
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>778
</td>
<td><a href="/wiki/Drum_Beating_(move)" title="Drum Beating (move)">Drum Beating</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>779
</td>
<td><a href="/wiki/Snap_Trap_(move)" title="Snap Trap (move)">Snap Trap</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>35
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>780
</td>
<td><a href="/wiki/Pyro_Ball_(move)" title="Pyro Ball (move)">Pyro Ball</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>781
</td>
<td><a href="/wiki/Behemoth_Blade_(move)" title="Behemoth Blade (move)">Behemoth Blade</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>782
</td>
<td><a href="/wiki/Behemoth_Bash_(move)" title="Behemoth Bash (move)">Behemoth Bash</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>783
</td>
<td><a href="/wiki/Aura_Wheel_(move)" title="Aura Wheel (move)">Aura Wheel</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>110
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>784
</td>
<td><a href="/wiki/Breaking_Swipe_(move)" title="Breaking Swipe (move)">Breaking Swipe</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>785
</td>
<td><a href="/wiki/Branch_Poke_(move)" title="Branch Poke (move)">Branch Poke</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>40
</td>
<td>40
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>786
</td>
<td><a href="/wiki/Overdrive_(move)" title="Overdrive (move)">Overdrive</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>787
</td>
<td><a href="/wiki/Apple_Acid_(move)" title="Apple Acid (move)">Apple Acid</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>788
</td>
<td><a href="/wiki/Grav_Apple_(move)" title="Grav Apple (move)">Grav Apple</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>789
</td>
<td><a href="/wiki/Spirit_Break_(move)" title="Spirit Break (move)">Spirit Break</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>75
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>790
</td>
<td><a href="/wiki/Strange_Steam_(move)" title="Strange Steam (move)">Strange Steam</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>95%
</td>
<td>VIII
</td></tr>
<tr>
<td>791
</td>
<td><a href="/wiki/Life_Dew_(move)" title="Life Dew (move)">Life Dew</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>792
</td>
<td><a href="/wiki/Obstruct_(move)" title="Obstruct (move)">Obstruct</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>793
</td>
<td><a href="/wiki/False_Surrender_(move)" title="False Surrender (move)">False Surrender</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>794
</td>
<td><a href="/wiki/Meteor_Assault_(move)" title="Meteor Assault (move)">Meteor Assault</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>795
</td>
<td><a href="/wiki/Eternabeam_(move)" title="Eternabeam (move)">Eternabeam</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>160
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>796
</td>
<td><a href="/wiki/Steel_Beam_(move)" title="Steel Beam (move)">Steel Beam</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>140
</td>
<td>95%
</td>
<td>VIII
</td></tr>
<tr>
<td>797
</td>
<td><a href="/wiki/Expanding_Force_(move)" title="Expanding Force (move)">Expanding Force</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>798
</td>
<td><a href="/wiki/Steel_Roller_(move)" title="Steel Roller (move)">Steel Roller</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>130
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>799
</td>
<td><a href="/wiki/Scale_Shot_(move)" title="Scale Shot (move)">Scale Shot</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>25
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>800
</td>
<td><a href="/wiki/Meteor_Beam_(move)" title="Meteor Beam (move)">Meteor Beam</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>120
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>801
</td>
<td><a href="/wiki/Shell_Side_Arm_(move)" title="Shell Side Arm (move)">Shell Side Arm</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>802
</td>
<td><a href="/wiki/Misty_Explosion_(move)" title="Misty Explosion (move)">Misty Explosion</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>803
</td>
<td><a href="/wiki/Grassy_Glide_(move)" title="Grassy Glide (move)">Grassy Glide</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>804
</td>
<td><a href="/wiki/Rising_Voltage_(move)" title="Rising Voltage (move)">Rising Voltage</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>20
</td>
<td>70
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>805
</td>
<td><a href="/wiki/Terrain_Pulse_(move)" title="Terrain Pulse (move)">Terrain Pulse</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>50
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>806
</td>
<td><a href="/wiki/Skitter_Smack_(move)" title="Skitter Smack (move)">Skitter Smack</a>
</td>
<td style="text-align:center; background:#A8B820"><a href="/wiki/Bug_(type)" title="Bug (type)"><span style="color:#FFF">Bug</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>807
</td>
<td><a href="/wiki/Burning_Jealousy_(move)" title="Burning Jealousy (move)">Burning Jealousy</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>70
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>808
</td>
<td><a href="/wiki/Lash_Out_(move)" title="Lash Out (move)">Lash Out</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>75
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>809
</td>
<td><a href="/wiki/Poltergeist_(move)" title="Poltergeist (move)">Poltergeist</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>110
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>810
</td>
<td><a href="/wiki/Corrosive_Gas_(move)" title="Corrosive Gas (move)">Corrosive Gas</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>40
</td>
<td>—
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>811
</td>
<td><a href="/wiki/Coaching_(move)" title="Coaching (move)">Coaching</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>812
</td>
<td><a href="/wiki/Flip_Turn_(move)" title="Flip Turn (move)">Flip Turn</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>20
</td>
<td>60
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>813
</td>
<td><a href="/wiki/Triple_Axel_(move)" title="Triple Axel (move)">Triple Axel</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>20
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>814
</td>
<td><a href="/wiki/Dual_Wingbeat_(move)" title="Dual Wingbeat (move)">Dual Wingbeat</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>40
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>815
</td>
<td><a href="/wiki/Scorching_Sands_(move)" title="Scorching Sands (move)">Scorching Sands</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>816
</td>
<td><a href="/wiki/Jungle_Healing_(move)" title="Jungle Healing (move)">Jungle Healing</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>817
</td>
<td><a href="/wiki/Wicked_Blow_(move)" title="Wicked Blow (move)">Wicked Blow</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>818
</td>
<td><a href="/wiki/Surging_Strikes_(move)" title="Surging Strikes (move)">Surging Strikes</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>25
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>819
</td>
<td><a href="/wiki/Thunder_Cage_(move)" title="Thunder Cage (move)">Thunder Cage</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>80
</td>
<td>90%
</td>
<td>VIII
</td></tr>
<tr>
<td>820
</td>
<td><a href="/wiki/Dragon_Energy_(move)" title="Dragon Energy (move)">Dragon Energy</a>
</td>
<td style="text-align:center; background:#7038F8"><a href="/wiki/Dragon_(type)" title="Dragon (type)"><span style="color:#FFF">Dragon</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>150
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>821
</td>
<td><a href="/wiki/Freezing_Glare_(move)" title="Freezing Glare (move)">Freezing Glare</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>822
</td>
<td><a href="/wiki/Fiery_Wrath_(move)" title="Fiery Wrath (move)">Fiery Wrath</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>823
</td>
<td><a href="/wiki/Thunderous_Kick_(move)" title="Thunderous Kick (move)">Thunderous Kick</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>824
</td>
<td><a href="/wiki/Glacial_Lance_(move)" title="Glacial Lance (move)">Glacial Lance</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>130
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>825
</td>
<td><a href="/wiki/Astral_Barrage_(move)" title="Astral Barrage (move)">Astral Barrage</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>826
</td>
<td><a href="/wiki/Eerie_Spell_(move)" title="Eerie Spell (move)">Eerie Spell</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>80
</td>
<td>100%
</td>
<td>VIII
</td></tr>
<tr>
<td>827
</td>
<td><a href="/wiki/Dire_Claw_(move)" title="Dire Claw (move)">Dire Claw</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>828
</td>
<td><a href="/wiki/Psyshield_Bash_(move)" title="Psyshield Bash (move)">Psyshield Bash</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>90
</td>
<td>VIII
</td></tr>
<tr>
<td>829
</td>
<td><a href="/wiki/Power_Shift_(move)" title="Power Shift (move)">Power Shift</a>
</td>
<td style="text-align:center; background:#A8A878"><a href="/wiki/Normal_(type)" title="Normal (type)"><span style="color:#FFF">Normal</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>830
</td>
<td><a href="/wiki/Stone_Axe_(move)" title="Stone Axe (move)">Stone Axe</a>
</td>
<td style="text-align:center; background:#B8A038"><a href="/wiki/Rock_(type)" title="Rock (type)"><span style="color:#FFF">Rock</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>65
</td>
<td>90
</td>
<td>VIII
</td></tr>
<tr>
<td>831
</td>
<td><a href="/wiki/Springtide_Storm_(move)" title="Springtide Storm (move)">Springtide Storm</a>
</td>
<td style="text-align:center; background:#EE99AC"><a href="/wiki/Fairy_(type)" title="Fairy (type)"><span style="color:#FFF">Fairy</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>95
</td>
<td>80
</td>
<td>VIII
</td></tr>
<tr>
<td>832
</td>
<td><a href="/wiki/Mystical_Power_(move)" title="Mystical Power (move)">Mystical Power</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>70
</td>
<td>90
</td>
<td>VIII
</td></tr>
<tr>
<td>833
</td>
<td><a href="/wiki/Raging_Fury_(move)" title="Raging Fury (move)">Raging Fury</a>
</td>
<td style="text-align:center; background:#F08030"><a href="/wiki/Fire_(type)" title="Fire (type)"><span style="color:#FFF">Fire</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>90
</td>
<td>85
</td>
<td>VIII
</td></tr>
<tr>
<td>834
</td>
<td><a href="/wiki/Wave_Crash_(move)" title="Wave Crash (move)">Wave Crash</a>
</td>
<td style="text-align:center; background:#6890F0"><a href="/wiki/Water_(type)" title="Water (type)"><span style="color:#FFF">Water</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>835
</td>
<td><a href="/wiki/Chloroblast_(move)" title="Chloroblast (move)">Chloroblast</a>
</td>
<td style="text-align:center; background:#78C850"><a href="/wiki/Grass_(type)" title="Grass (type)"><span style="color:#FFF">Grass</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>120
</td>
<td>95
</td>
<td>VIII
</td></tr>
<tr>
<td>836
</td>
<td><a href="/wiki/Mountain_Gale_(move)" title="Mountain Gale (move)">Mountain Gale</a>
</td>
<td style="text-align:center; background:#98D8D8"><a href="/wiki/Ice_(type)" title="Ice (type)"><span style="color:#FFF">Ice</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>85
</td>
<td>VIII
</td></tr>
<tr>
<td>837
</td>
<td><a href="/wiki/Victory_Dance_(move)" title="Victory Dance (move)">Victory Dance</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>838
</td>
<td><a href="/wiki/Headlong_Rush_(move)" title="Headlong Rush (move)">Headlong Rush</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>5
</td>
<td>100
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>839
</td>
<td><a href="/wiki/Barb_Barrage_(move)" title="Barb Barrage (move)">Barb Barrage</a>
</td>
<td style="text-align:center; background:#A040A0"><a href="/wiki/Poison_(type)" title="Poison (type)"><span style="color:#FFF">Poison</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>840
</td>
<td><a href="/wiki/Esper_Wing_(move)" title="Esper Wing (move)">Esper Wing</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>10
</td>
<td>75
</td>
<td>90
</td>
<td>VIII
</td></tr>
<tr>
<td>841
</td>
<td><a href="/wiki/Bitter_Malice_(move)" title="Bitter Malice (move)">Bitter Malice</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>842
</td>
<td><a href="/wiki/Shelter_(move)" title="Shelter (move)">Shelter</a>
</td>
<td style="text-align:center; background:#B8B8D0"><a href="/wiki/Steel_(type)" title="Steel (type)"><span style="color:#FFF">Steel</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>843
</td>
<td><a href="/wiki/Triple_Arrows_(move)" title="Triple Arrows (move)">Triple Arrows</a>
</td>
<td style="text-align:center; background:#C03028"><a href="/wiki/Fighting_(type)" title="Fighting (type)"><span style="color:#FFF">Fighting</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>50
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>844
</td>
<td><a href="/wiki/Infernal_Parade_(move)" title="Infernal Parade (move)">Infernal Parade</a>
</td>
<td style="text-align:center; background:#705898"><a href="/wiki/Ghost_(type)" title="Ghost (type)"><span style="color:#FFF">Ghost</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>15
</td>
<td>60
</td>
<td>100
</td>
<td>VIII
</td></tr>
<tr>
<td>845
</td>
<td><a href="/wiki/Ceaseless_Edge_(move)" title="Ceaseless Edge (move)">Ceaseless Edge</a>
</td>
<td style="text-align:center; background:#705848"><a href="/wiki/Dark_(type)" title="Dark (type)"><span style="color:#FFF">Dark</span></a>
</td>
<td style="background:#C92112" align="center"><a href="/wiki/Physical_move" title="Physical move"><span style="color:#F67A1A;">Physical</span></a>
</td>
<td>15
</td>
<td>65
</td>
<td>90
</td>
<td>VIII
</td></tr>
<tr>
<td>846
</td>
<td><a href="/wiki/Bleakwind_Storm_(move)" title="Bleakwind Storm (move)">Bleakwind Storm</a>
</td>
<td style="text-align:center; background:#A890F0"><a href="/wiki/Flying_(type)" title="Flying (type)"><span style="color:#FFF">Flying</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>95
</td>
<td>80
</td>
<td>VIII
</td></tr>
<tr>
<td>847
</td>
<td><a href="/wiki/Wildbolt_Storm_(move)" title="Wildbolt Storm (move)">Wildbolt Storm</a>
</td>
<td style="text-align:center; background:#F8D030"><a href="/wiki/Electric_(type)" title="Electric (type)"><span style="color:#FFF">Electric</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>95
</td>
<td>80
</td>
<td>VIII
</td></tr>
<tr>
<td>848
</td>
<td><a href="/wiki/Sandsear_Storm_(move)" title="Sandsear Storm (move)">Sandsear Storm</a>
</td>
<td style="text-align:center; background:#E0C068"><a href="/wiki/Ground_(type)" title="Ground (type)"><span style="color:#FFF">Ground</span></a>
</td>
<td style="background:#4F5870" align="center"><a href="/wiki/Special_move" title="Special move"><span style="color:#FFF;">Special</span></a>
</td>
<td>5
</td>
<td>95
</td>
<td>80
</td>
<td>VIII
</td></tr>
<tr>
<td>849
</td>
<td><a href="/wiki/Lunar_Blessing_(move)" title="Lunar Blessing (move)">Lunar Blessing</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr>
<tr>
<td>850
</td>
<td><a href="/wiki/Take_Heart_(move)" title="Take Heart (move)">Take Heart</a>
</td>
<td style="text-align:center; background:#F85888"><a href="/wiki/Psychic_(type)" title="Psychic (type)"><span style="color:#FFF">Psychic</span></a>
</td>
<td style="background:#8C888C" align="center"><a href="/wiki/Status_move" title="Status move"><span style="color:#FFF;">Status</span></a>
</td>
<td>10
</td>
<td>—
</td>
<td>—
</td>
<td>VIII
</td></tr></tbody><tfoot></tfoot></table>
</td></tr></tbody>
"""
