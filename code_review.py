def calc(a,b,c):
    x=a+b
    y=x*c
    if c==0:
        return 0
    else:
        return y/c


print(calc(10, 20, 5))