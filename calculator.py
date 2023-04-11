x =float(input("enter your first number: "))
y = float(input("enter your second number: "))
print("select the operation to be done")
print("    1.addition")
print("    2.subtraction")
print("    3.division")
print("    4.multiplication")
k = int(input("enter the value: "))
if k == 1:
    z = x+y
    print("Addition: ", z)
if k == 2:
    a = x-y
    print("subtraction: ", a)
if k == 3:
    b = x / y
    print("Division: ", b)
if k == 4:
    c = x * y
    print("Multiplication: ", c)
elif k>4:
    print("Invalid value")


