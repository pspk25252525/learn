def dec(func):
    def asc(a,b):
        print("Before function")
        c=func(a,b)
        d=15
        return func(d,c)
    return asc

@dec
def mahendra(a,b):
    return a+b

print(mahendra(5,7))
