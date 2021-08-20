n=int(input("enter the length of password"))
pw=input("enter the password")
spl="!@#$%&*()-+"
l=[0,0,0,0]
for i in pw:
    if i.isdigit():
        l[0]=1
    elif i.islower():
        l[1]=1
    elif i.isupper():
        l[2]=1
    elif i in spl:
        l[3]=1
print(max(6-len(pw),4-sum(l)))