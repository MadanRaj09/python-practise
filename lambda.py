num=[1,2,3,4,5,6,7,8,9,11,12,13,14]
odd = list(filter(lambda a: a % 2 != 0, num))
print(odd)

num1=[1,2,3,4,5,6,7,8,9,11,12,13,14]
even = list(filter(lambda a: a % 2 == 0, num1))
print(even)