n=int(input("Enter n="))
sum=0
while n>0:
    r=n%10
    sum=sum+r
    n=int(n/10)
print("Digit sum=",sum)
