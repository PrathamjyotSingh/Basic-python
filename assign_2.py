n=int(input("enter num1 :"))
s=0
for i in range(1,n):
    if i%7==0:
        if i%9==0:
            s=s+i
print(s)