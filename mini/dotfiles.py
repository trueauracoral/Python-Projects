import subprocess
import os
import platform
import shutil

# CONFIG LOCATIONS
if platform.system() == "Windows":
    appdata = os.getenv('APPDATA')
configs = f"""
alacritty - {appdata}\\alacritty\\alacritty.yml
emacs - {appdata}\\.emacs.d\\init.el
mpv - {appdata}\\mpv\\mpv.conf
qutebrowser - {appdata}\\qutebrowser\\config\\config.py
"""

git_repo = "C:\SGZ_Pro\Hobbys\coding-projects\Dots\\"

for config in configs.splitlines():
    if config == "":
        pass
    else:
        config = config.split(" - ")
        oldpath = config[1]
        newpath = os.path.join(git_repo, config[0], os.path.basename(oldpath))
        print(oldpath)
        print(newpath)
        shutil.copy(oldpath,newpath)