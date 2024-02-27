a=int(input("enter num1 :"))
s=0
for i in range(2,a):
    if(a%i==0):
        s=s+1
if (s==0):
    print("prime number")
else:
    print("not prime number")