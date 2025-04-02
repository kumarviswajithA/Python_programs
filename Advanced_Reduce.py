# Reduce :



from functools import reduce

l = [1,2,3,4,5,6,7,8,9]

def func(a,b):
    return a+b
res = reduce(func,l)
print(res)