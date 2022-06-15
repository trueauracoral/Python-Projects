#!/usr/bin/env python
#!/usr/bin/env python
import datetime
import subprocess
import sys

cpu = subprocess.getoutput("wmic cpu get numberofcores, name")
cpu = cpu.splitlines()[2]
gpu = subprocess.getoutput("wmic path win32_videoController get name")
gpu = gpu.splitlines()[2]
memory = subprocess.getoutput("wmic MemoryChip get Capacity")
rams = 0
for line in memory.splitlines():
    if "Capacity" in line:
        pass
    elif line == "":
        pass
    else:
        rams = rams + int(line.split()[0])
rams = sys.getsizeof(rams)
uptime = subprocess.getoutput("net statistics workstation")
for line in uptime.splitlines():
    if "Statistics" in line:
        uptimedate = line.split()[2].split("/")
a = datetime.datetime(int(uptimedate[2]),int(uptimedate[0]),int(uptimedate[1]))
b = datetime.datetime.now()
uptimedate = str(b-a).split(",")[0]
version = subprocess.getoutput("wmic os get version")
version = version.splitlines()[2]
name = subprocess.getoutput("wmic os get Caption")
name = name.splitlines()[2]

if len(sys.argv) == 1:
    print(f"""
 _____  _____
|     ||     | CPU: {cpu}
|     ||     | GPU: {gpu}
|_____||_____| RAM: {rams}
 _____  _____  Uptime: {uptimedate}
|     ||     | Version: {version}
|     ||     | OS: {name}
|_____||_____|""")
elif sys.argv[1] == "-u":
    print(f'''
┌────┐ ┌────┐ CPU: {cpu}
│    │ │    │ GPU: {gpu}
└────┘ └────┘ RAM: {rams}
┌────┐ ┌────┐ Uptime: {uptimedate}
│    │ │    │ Version: {version}
└────┘ └────┘ OS: {name}''')
else:
    print("Unsupported command")
