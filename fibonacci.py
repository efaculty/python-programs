n=int(input("Enter n="))
a=0
b=1
for i in range(1,n+1):
    if i==n:
        print(a,end=" ")    
    else:
        print(a,end=", ")      
    c=a+b
    a=b
    b=c