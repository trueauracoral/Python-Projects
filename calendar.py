import datetime

mydate = datetime.datetime.now()

# Month+dashes
mm = mydate.strftime("%B")
dd = mydate.strftime("%d")
num = 21
num2 = len(mm+" "+dd)
final = int((num-num2)*0.5)
print("-"*final+mm+" "+dd+"-"*final)
print(" S  M  T  W  T  F  S ")
if mm in ["January", "March", "May", "July", "August", "October", "December"]:
    day_num = 31
elif mm in ["April", "June", "September", "November"]:
    day_num = 30
elif mm == "Febuary":
    day_num = 28
for i in range(1,day_num+1):
    if (i % 7 == 0):
        print()
    if i in [10,16,24]:
        print(str(i),end="")
    elif len(str(i)) == 2:
        print(" "+str(i), end="")
    else:
        print(" "+str(i)+" ", end="")
