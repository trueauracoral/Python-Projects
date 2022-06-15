#!/usr/bin/env python
import os
import subprocess
import sys
import platform
red = "\033[41m"
norm = "\033[00m"
instance = "http://0x0.st"
fuzzy_picker = "fzf"
platform = platform.system()

if platform == "Windows":
    home = "C:\\"
    file = home + subprocess.getoutput(f"cd {home} && {fuzzy_picker}")
    git_bash_shell = "%LocalAppData%\\Programs\\Git\\bin\\sh.exe"
    windows_command = f"{git_bash_shell} -c \"curl -F'file=@{file}' {instance}\""
    os.system(windows_command)
else:
    home = "~"
    file = subprocess.getoutput(f"cd {home} && {fuzzy_picker}")
    print(f"Uploading.... {file}")
    linux_command = f"curl -F'file=@{file}' {instance}"
    os.system(linux_command)
