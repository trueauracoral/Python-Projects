#!/usr/bin/env/ python
import subprocess
import os
import shutil

header = """
<!DOCTYPE html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Welcome to Zortazert's website!</title>
<link rel="stylesheet" href="https://zortazert.codeberg.page/style/styles.css">
<link rel="shortcut icon" href="https://zortazert.codeberg.page/images/Denshi-Meme-Server-Icon.png"/>
</head>

<body>
<h1 class="title">Welcome to Zortazert's website!</h1>
<p>
<b>[ <a href='./animations.html'>Animations</a> <a href='./art.html'>Art Portfoldio</a> <a href='./internet-friends.html'>Internet Friends</a> <a href='./projects.html'>Projects</a> <a href='./donate.html'>Donate</a> ]</b>
</p>"""
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
        output.append(f"<a href='..{full}index.html'>{s}</a>")
    return f"/<a href='{num*'../'}index.html'>{cwd_folder}</a>/"+"/".join(output)

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
        except:
            print("This is most likely not a text file")
    command = f'cd {git_repo} && git log --pretty=format:\'%h%x09%an%x09%ad%x09%s\' --no-decorate -1 -- {file}'
    commit = subprocess.getoutput(command)
    with open(new+".html", "w", encoding="utf-8") as f:
        f.write(f"""{header}
<code>{commit}</code>
<h2>{linkify(file)}</h2>
<pre>{text}</pre>
</body>
</html>""")

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
        command = f'cd {git_repo} && git log --pretty=format:\'%h%x09%an%x09%ad%x09%s\' --no-decorate -1 -- {dir.replace(os.getcwd(),"")[1:]}'
        commit = subprocess.getoutput(command)
        link = linkify(dir.replace(os.getcwd(), "").replace("\\", "/")[1:])
        f.write(f"""{header}
<code>{commit}</code>
<h2>{link}</h2>
<ul>
{files}
</ul>
</body>
</html>""")
