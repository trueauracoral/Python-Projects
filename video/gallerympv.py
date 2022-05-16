import os
from pathlib import Path

dir = "C:\\SGZ_Pro\\Hobbys\\Media\\xy\\thumbnails\\"
files2 = sorted(Path(dir).iterdir(), key=os.path.getmtime)
files = os.listdir(dir)
nums = list(range(int(len(files))))
vidbrack = []
for num in nums:
    vidbrack.append(f"[vid{num}]")
def divide_chunks(l,n):
    for i in range(0, len(l), n):
        yield l[i:i +n]
chunks = list(divide_chunks(vidbrack[1:],6))
external_file = dir+files[0]
t = ""
num = 0
lafvi = ""
for file in files2:
    external_file = external_file+f" --external-file={file}"
for i, file in enumerate(files[1:]):
    if (i % 3):
        num = num+1
        t = t+f"[t{num}]"
        lafvi = lafvi+''.join(chunks[num-1])+f"hstack=inputs=6[t{num}];"
    elif i == 3:
        break
inputs = i+1
vidbrack = ''.join(vidbrack)
command = f'mpv --lavfi-complex="{lafvi}{t} vstack [vo]" {external_file}'
print(command)
os.system(command)

#command = f'mpv --lavfi-complex="{vidbrack}hstack=inputs={inputs}[vo]" {external_file}'
#command = f'mpv --lavfi-complex="[vid1][vid2][vid3]hstack=inputs=3[t1];[vid6][vid5][vid6]hstack=inputs=3[t2];{t} vstack [vo]" {external_file}'
