def madan(**data):
    for k , v in data.items():
        if k=="name":
            print(k,"  :",v)
        elif k=="place":
            print(k, " :", v)
        elif k=="age":
            print(k, "   :", v)
        else:
            print(k,":",v)
        print()


num=0
while num<89:
         Name = input(print("enter your Name:"))
         Place = input(print("enter your Place:"))
         Age = input(print("enter your Age:"))
         Mobile = input(print("enter your Mobile:"))
         num = num + 1
         print()
         print("Hi,""\n",Name,"\n"   "your register no is:",num,"\n""please check the below details")
         print()
         madan(name=Name,place=Place,age=Age,mobile=Mobile)
         print("ALL THE BEST,",Name)
         print()
         c = input(print("press 0 to exit or any key to continue"))
         if c==1:
             continue
         elif c=="0":
             break
print("welcome",Name,",""visit again")
input()












