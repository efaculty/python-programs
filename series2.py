#S=1/2 + 2/3 + 3/4 +.....+ n/n+1
n=int(input("Enter n="))
sum=0
for i in range(1,n+1):
    sum=sum+i/(i+1)
print("Sum=",sum)    