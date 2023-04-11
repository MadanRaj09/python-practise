def madan(num):
    result = 1
    c=1
    while c<=num:
        d=result*c           #FACTORIAL USING  "WHILE" LOOP by defining functions
        result = d
        c=c+1
    print(d)

madan(4)

def maddy(num):
    c=1
    for x in range(1,num+1,1):
        result=c*x                           #FACTORIAL USING  "for" LOOP by defining functions
        c=result
    print(result)

maddy(5)



