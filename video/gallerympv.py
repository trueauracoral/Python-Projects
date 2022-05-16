import os

dir = "C:\\SGZ_Pro\\Hobbys\\Media\\xy\\thumbnails\\"
files = os.listdir(dir)

nums = list(range(int(len(files))))
vidbrack = []
for num in nums:
    vidbrack.append(f"[vid{num}]")
external_file = dir+files[0]
t = ""
num = 0
lafvi = []
for i, file in enumerate(files[1:]):
    external_file = external_file+f" --external-file={dir+file}"
    if (i % 3):
        num = num+1
        t = t+f"[t{num}]"
        lafvi = ''.join(vidbrack[num:num+3])+f"hstack=inputs=3[t{num}];"
        print(lafvi)
    elif i == 15:
        break
inputs = i+1
vidbrack = ''.join(vidbrack)
lafvi = ''.join(lafvi)
if t == "":
    command = f'mpv --lavfi-complex="{vidbrack}hstack=inputs={inputs}[vo]" {external_file}'
else:
    command = f'mpv --lavfi-complex="{lafvi}{t} vstack [vo]" {external_file}'
    #command = f'mpv --lavfi-complex="[vid1][vid2][vid3]hstack=inputs=3[t1];[vid4][vid5][vid6]hstack=inputs=3[t2];{t} vstack [vo]" {external_file}'
print(command)
#os.system(command)
