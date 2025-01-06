n=int(input("Enter n="))
cubeSum=0
num=n
while num>0:
    r=num%10
    cubeSum=cubeSum+r*r*r
    num=int(num/10)
if n==cubeSum:
    print("Armstrong")
else:
    print("Not Armstrong")