#S=x/1 + x/2 + x/3 +.....+ x/n
n=int(input("Enter n="))
x=int(input("Enter x="))
sum=0
for i in range(1,n+1):
    sum=sum+x/i
print("Sum=",sum)    