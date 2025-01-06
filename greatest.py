a=int(input("Enter a="))
b=int(input("Enter b="))
c=int(input("Enter c="))
"""
if a>b:
    if a>c:
        print("a is greatest.")
    else:
        print("c is greatest.")
else:
    if b>c:
        print("b is greatest.")
    else:
        print("c is greatest.")    
"""
if a>b and a>c:
    print("a is greatest.")
if b>a and b>c:
    print("b is greatest.")
if c>a and c>b:
    print("c is greatest.")    