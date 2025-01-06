import math
n=int(input("Enter Binary n="))
num=n
b=""
while num>0:
    r=num%2
    b=str(r)+b
    num=int(num/2)
print(b)

