L= [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)
del L[0]
del L[2]
print(L)
L.sort()
print(L)
L.sort(reverse=True)
print(L)
if (13 in L)==True:
    print("present")
else:
    print("not present")
print(len(L))
s=0
for i in L:
    s=s+i
print(s)
# WAP to sum all ODD numbers in L
s=0
for i in L:
    if i%2!=0:
        s=s+i
print(s)
# WAP to find the sum of all even numbers in L
s=0
for i in L:
    if i%2!=1:
        s=s+i
print(s)
# WAP to sum all PRIME numbers in L
print(L)
s=0
f=0
for i in L:
    for j in range(2,i//2 + 1):
        if i % j == 0:
            break
    else:
      s=s+i
print(s)
L.clear()
print(L)
del L