# Snakesay
Snakesay is a less feature rewrite of cowsay in python.

# Install
## Linux
First install the script with curl and move it to usr/bin
```bash
curl -o https://codeberg.org/zortazert/Python-Projects/raw/branch/main/snakesay/snakesay.py snakesay.py
mv snakesay.py usr/bin/snakesay.py
```
Then if you want fortunes, install fortunes.txt and move it to usr/share
```bash
curl -o fortunes.txt https://codeberg.org/zortazert/Python-Projects/raw/branch/main/snakesay/fortunes.txt 
mv fortunes.txt usr/share/fortunes.txt
```
## Windows
In some directory download the fortunes.txt and snakesay.py for windows script. Then search on the internet how to make the directory you installed them in your path.
```
curl -o snakesay-win.py https://codeberg.org/zortazert/Python-Projects/raw/branch/main/snakesay/snakesay.py 
curl -o fortunes.txt https://codeberg.org/zortazert/Python-Projects/raw/branch/main/snakesay/fortunes.txt 
```
# Help
python snakesay.py QUERY - make a snake say something

python snakesay.py fortune - make a snake say a random fortune. Requires requests installed.

python snakesay.py -r QUERY - randomly selected a tux, cow or snake will say something
    
python snakesay.py -t QUERY - a tux will say something

python snakesay.py -s QUERY - a snake will say something

python snakesay.py -c QUERY - a cow will say something
