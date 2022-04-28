import datetime

mydate = datetime.datetime.now()

mm = mydate.strftime("%B")
dd = mydate.strftime("%d")
num = 22
num2 = len(mm+" "+dd)
final = int((num-num2)*0.5)
print("-"*final+mm+" "+dd+"-"*final)

print(" Su Mo Tu We Th Fr Sa ")
if mm in ["January", "March", "May", "July", "August", "October", "December"]:
    day_num = 31
elif mm in ["April", "June", "September", "November"]:
    day_num = 30
elif mm == "Febuary":
    day_num = 28
for i in range(1,day_num+1):
    if (i % 7 == 0):
        print(" "+str(i)+"\n",end="")
    elif len(str(i)) == 2:
        print(" "+str(i), end="")
    else:
        print(" "+str(i)+" ", end="")
