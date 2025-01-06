n=int(input("Enter n="))
mul=1
while n>0:
    r=n%10
    mul=mul*r
    n=int(n/10)
print("Digit mul=",mul)