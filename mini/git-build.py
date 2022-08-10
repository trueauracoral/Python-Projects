#!/usr/bin/env/ python
import subprocess
import os
import shutil
import requests
import urllib.parse
import time
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_lexer_for_filename
from pygments.formatters import HtmlFormatter

header = """<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Welcome to Zortazert's website!</title>
<link rel="stylesheet" href="/style.css">
<link rel="shortcut icon" href="https://zortazert.codeberg.page/images/Denshi-Meme-Server-Icon.png"/>
</head>

<body>
<h1 class="title">Welcome to Zortazert's website!</h1>
<p>
<b>[ <a href='./animations.html'>Animations</a> <a href='./art.html'>Art Portfoldio</a> <a href='./internet-friends.html'>Internet Friends</a> <a href='./projects.html'>Projects</a> <a href='./donate.html'>Donate</a> ]</b>
</p>"""
compile_date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(os.stat(os.getcwd()).st_mtime))
end = f"""
<h1>This was compiled for web view on {compile_date} and may not be the latest version.</h1>
</body>
</html>"""
git_repo = "C:\\SGZ\\Coding-Projects\\Python-Projects"

files = subprocess.getoutput(f"cd {git_repo} && git ls-files")
cwd_folder = os.path.basename(os.getcwd())

def linkify(file):
    output = []
    full = "/"
    num = file.count("/")+1
    print(f"{file} {num}")
    for s in file.split("/"):
        full += s + "/"
        output.append(f"<a href='{full}'>{s}</a>")
    return f"/<a href='/'>{cwd_folder}</a>/"+"/".join(output)

def commit(file):
    return subprocess.getoutput(f'cd {git_repo} && git log --pretty=format:\'%h%x09%an%x09%ad%x09%s\' --no-decorate -1 -- {file}')[1:][:-1]

for file in files.splitlines():
    original = os.path.join(git_repo, file)
    new = os.path.join(str(os.getcwd()), file)
    dirs = []
    if "/" in file:
        dir = os.path.dirname(new)
        dirs.append(dir)
        try:
            os.mkdir(dir)
        except:
            pass
    with open(original, "r", encoding="utf-8") as f:
        try:
            text = f.read()
            try:
                lexer = get_lexer_for_filename(file)
                formatter = HtmlFormatter(noclasses=True, style='monokai')
                text = f"<p>{highlight(text, lexer, formatter)}</p>"
            except Exception as e:
                print(e)
                text = f"<pre>{text}</pre>"
        except Exception as e:
            print(e)
    with open(new+".html", "w", encoding="utf-8") as f:
        f.write(f"""{header}
<code>{commit(file)}</code>
<h2>{linkify(file)}</h2>
{text}
{end}""")

for dir in [x[0] for x in os.walk(os.getcwd())]:
    files = []
    files.append(f"<li><a href='../index.html'>../</a></li>")
    for file in os.listdir(dir):
        if os.path.isdir(os.path.join(dir, file)):
            files.append(f"<li><a href='{file}/index.html'>{file}/</a></li>")
        elif file == "index.html":
            pass
        else:
            files.append(f"<li><a href='{file}'>{file[:-5]}</a></li>")
    files = '\n'.join(files)
    with open(os.path.join(dir, "index.html"), "w") as f:
        link = linkify(dir.replace(os.getcwd(), "").replace("\\", "/")[1:])
        f.write(f"""{header}
<code>{commit(dir.replace(os.getcwd(),"")[1:])}</code>
<h2>{link}</h2>
<ul>
{files}
</ul>
{end}""")
