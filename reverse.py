n=int(input("Enter n="))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=int(n/10)
print("Reverse=",rev)