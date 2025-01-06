#135 = 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
import math
n=int(input("Enter n="))
sum=0
num=n
c=0
while num>0:
    c=c+1
    num=int(num/10)
num=n
while num>0:
    r=num%10
    sum = sum + math.pow(r,c)
    c=c-1
    num=int(num/10)
if n==sum:
    print("Disarium")
else:
    print("Not Disarium")