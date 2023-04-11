def madan(data):
    hkl=0
    for kl,vl in data.items():
        if hkl<len(kl):
           hkl=len(kl)
    for k,v in data.items():
        if hkl==len(k):
           print(k,":",v)
        else:
           space=""
           balance=hkl-len(k)
           for xs in range(balance):
               space += " "
           print(k+space,":",v)



userdata = {}
e = 1
while e != "0":
    firstkey = input(print("enter the Key:"))
    firstvalue = input(print("enter the Value:"))
    userdata[firstkey] = firstvalue
    e = input(print("enter 0 to exit or any key to continue"))
madan(userdata)

