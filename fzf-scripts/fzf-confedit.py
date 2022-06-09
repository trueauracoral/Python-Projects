import subprocess
import os

editor = "emacs"
fzf = "C:\\SGZ_Pro\\z-Apps_Drivers\\fzf-0.30.0-windows_amd64\\fzf.exe --reverse < FILE"

if platform.system() == "Windows":
    appdata = os.getenv('APPDATA')
configs = f"""
alacritty - {appdata}\\alacritty\\alacritty.yml
emacs - {appdata}\\.emacs.d\\init.el
mpv - {appdata}\\Roaming\\mpv\\mpv.conf
"""

with open("configs.txt","w") as f:
    f.write(configs)

choice = subprocess.getoutput(fzf.replace("FILE","configs.txt")).split(" - ")[1]
if choice is not "":
    subprocess.Popen(f"{editor} {choice}")
os.remove("configs.txt")