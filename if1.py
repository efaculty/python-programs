h= float(input("Enter H="))
e= float(input("Enter E="))
m= float(input("Enter M="))
s= float(input("Enter S="))
c= float(input("Enter C="))

total = h+e+m+s+c
per = total/5

if per>=90:
    print("Grade 1")
elif per>=80 and per<90:
    print("Grade 2")
elif per>=70 and per<80:
    print("Grade 3")
elif per>=60 and per<70:
    print("Grade 4")
elif per>=50 and per<60:
    print("Grade 5")
else:
    print("Fail")