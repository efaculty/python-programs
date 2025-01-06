#1110 -> 14
import math
n=int(input("Enter Binary n="))
d=0
flag=1
num=n
i=0
while num>0:
    r=num%10
    if(r!=0 and r!=1):
        flag=0
        break
    num=int(num/10)
num=n  
if flag==1:       
    while num>0:
        r=num%10
        d = d + r*math.pow(2,i)
        i=i+1
        num=int(num/10)
    print("Decimal=",d)
else:
    print("Enter only binary number")

