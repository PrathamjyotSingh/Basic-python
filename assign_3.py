def fun(n):
    s=0
    for i in range(1,n):
        if i%2==1:
            s=s+i
    return s
print(fun(10))
