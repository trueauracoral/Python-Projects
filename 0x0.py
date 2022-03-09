import os

file = input("File: ")
print(file)

linux_shell = "%LocalAppData%\\Programs\\Git\\bin\\sh.exe"

command = linux_shell+" -c \"curl -F'file=@"+file+"' http:/0x0.st\""
os.system(command)
