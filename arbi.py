#arbitary keyword arguments
def madan(**name):
    print(name)
    for k,v in name.items():
        if k == "name":
            print(k," :",v)
        else:
            print(k, ":", v)


madan(name="madan",place='bangalore')
input()