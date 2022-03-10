import os
import sys
import platform
red = "\033[41m"
norm = "\033[00m"
instance = "http://0x0.st"


platform = platform.system()

if platform == "Windows":
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file = filedialog.askopenfilename()
    git_bash_shell = "%LocalAppData%\\Programs\\Git\\bin\\sh.exe"
    windows_command = f"{git_bash_shell} -c \"curl -F'file=@{file}' http:/0x0.st\""
    os.system(windows_command)
else:
    file = ""
    try:
        file = sys.argv[1]
    except:
        while not file:
            file = input("File: ")

    print(f"Uploading.... {file}")
    linux_command = f"curl -F'file=@{file}' {instance}"
    os.system(linux_command)
