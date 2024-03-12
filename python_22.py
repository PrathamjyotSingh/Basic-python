def div3(a):
    if a%3==0:
        return "{} is divisible by 3".format(a)
    else:
        return "{} is not divisible by 3".format(a)


ls1=[1,2,3,4,5,6,7,8,9]

ls2=list(map(div3,ls1))
print(ls2)