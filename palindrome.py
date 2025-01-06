n=int(input("Enter n="))
rev=0
num=n
while num>0:
    r=num%10
    rev=rev*10+r
    num=int(num/10)
if n==rev:
    print("Plaindrome")
else:
    print("Not Palindrome")