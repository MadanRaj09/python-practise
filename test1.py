def add(*a):
    result=0
    for i in a:
        result += a
    print(result)






a=[]
for z in range(1,10000000,1):
    x=int(input(print("enter a number:")))
    a.append(x)
    f=input(print("enter R for resulth"))
    if f=="R":
       break
    else:
       continue
print("addition of",a[0],"and",a[1],"is:",sum(a))

