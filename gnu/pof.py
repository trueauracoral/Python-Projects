# POF - Print Out Files 
import sys
import os
args = sys.argv[1:]
special = ["-n", "-b",]

if args == []:
    print("No arguments were given")
    quit()
if "-h" in args:
    print("""Usage:
- python pof.py [FILE]
Print out contents of given file (if they exist)
- python pof.py [FILE] [FILE2] [FILE3]
Print out all given files (if they exist)
- python pof.py -n [FILE]
Print out numbered the lines in the file.
- python pof.py -b [FILE]
Print out numbered only blank lines in the file.
- python pof.py -h
Pring out this help""")
    quit()

num=0
for arg in args:
    if os.path.isfile(arg):
        with open(arg) as f:
            if "-n" in args:
                for line in f.read().splitlines():
                    num = num+1
                    print(num, line)   
            elif "-b" in args:
                for line in f.read().splitlines():
                    if line == "":
                        print(line)
                    else:
                        num = num+1
                        print(num, line)
            else:
                print(f.read())
    elif arg in special:
        pass
    else:
        print(f'Can not find "{arg}"')