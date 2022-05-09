import os
import random

acronyms = """Organizations
BWIA - BWIA West Indies Airways
VISA - Visa International Service Association
SAAB - Saab Automobile AB
Cygnus Solutions - Cygnus, Your GNU Solutions
Others
Allegro - Allegro Low LEvel Game ROutines
AROS - AROS Research Operating System
ATI - ATI Technologies Inc.
BIRD - BIRD Internet Routing Daemon
CAVE - CAVE Automatic Virtual Environment
cURL - Curl URL Request Library
Darcs - Darcs Advanced Revision Control System
EINE - EINE Is Not Emacs
FIJI - FIJI Is Just ImageJ
GiNaC - GiNaC is Not a CAS
GNU - GNU's Not Unix
GPE - GPE Palmtop Environment
gRPC - grpc Remote Procedure Calls
HIJOS - Hijos por la Identidad y la Justicia contra el Olvido y el Silencio
HIM - HIM International Music, Taiwanese independent record label
JACK - JACK Audio Connection Kit
KGS - KGS Go Server
LAME - LAME Ain't an MP3 Encoder
LiVES - LiVES is a Video Editing System
MEGA - MEGA Encrypted Global Access
MIATA - MIATA is Always the Answer
MINT - MINT Is Not TRAC
Mung - Mung Until No Good
Nano - Nano's Another editor
Nagios - Nagios Ain't Gonna Insist On Sainthood
NiL - NiL Isn't Liero
Ninja-ide - Ninja-IDE Is Not Just Another IDE
PHP - PHP: Hypertext Preprocessor
PINE - PINE Is Nearly Elm
PIP - PIP Installs Packages
P.I.P.S. - P.I.P.S. Is POSIX on Symbian
PNG - PNG's not GIF
RPM - RPM Package Manager
SPARQL - SPARQL Protocol And RDF Query Language
TikZ - TikZ ist kein Zeichenprogramm
TiLP - TiLP is a Linking Program
TIP - TIP isn't Pico
TRESOR - TRESOR Runs Encryption Securely Outside RAM
UIRA - UIRA Isn't a Recursive Acronym
WINE - WINE Is Not an Emulator
XAMPP - XAMPP Apache MariaDB PHP Perl
XBMC - XBMC Media Center
XINU - XINU Is Not Unix
XNA - XNA's Not Acronymed
XNU - X is Not Unix
YAML - YAML Ain't Markup Language
ZINC - ZINC Is Not Commercial
Zinf - Zinf Is Not FreeAmp
ZWEI - ZWEI Was EINE Initially"""
acronyms = acronyms.splitlines()
for acronym in acronyms:
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])][0]
    name = acronym.split(" - ")[0].replace(" ","_").lower()
    command = f"ffmpeg -f lavfi -i color=size=1920x1080:rate=25:color={color} -vf \"drawtext=fontsize=45:fontcolor=#000000:x=(w-text_w)/2:y=(h-text_h)/2:text='{acronym}'\" -c:a copy -t 00:00:10 -shortest {name}.mp4"
    os.system(command)

files = os.listdir()
for file in files:
    if file.endswith(".mp4"):
        with open("list.txt","a") as f:
            f.write(f"\nfile '{file}'")
os.system("ffmpeg -f concat -i list.txt -c copy output.mp4")
#command = f"ffmpeg -f lavfi -i color=size=320x240:rate=25:color=blue -i audio.m4a -vf \"drawtext=fontfile=/path/to/font.ttf:fontsize=30:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text='Stack Overflow'\" -c:a copy -shortest output.mp4"
