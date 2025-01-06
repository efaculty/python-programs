n=int(input("Enter n="))
ec=0
oc=0
while n>0:
    r=n%10
    if r%2==1:
        oc=oc+1
    else:
        ec=ec+1    
    n=int(n/10)
print("Total even=",ec)
print("Total odd=",oc)