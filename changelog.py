# Simple script (not perfect) to generate changelog files from time to
# time.
import subprocess
import os

command = 'git --no-pager log --decorate --oneline --pretty=format:"* `%h` %s (%an) `%ad`" --date=short'
data = subprocess.getoutput(command)

with open("changelog.md", "w") as f:
    f.write(data)

os.system('git add . && git commit -am "Updated changelog.md" && git push')
