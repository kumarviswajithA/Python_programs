# MAP : A Map function is used to apply a given function to every item of an iterable, such as a list or tuple,
#       and it returns a map object.

# Example 1 -->

l1 = [1,2,3,4]
l2 = [5,6,7,8]

res = list(map(lambda a,b:a+b,l1,l2))
print(res)

# Example 2 -->
def myfun(a,b):
    return a+b

res = map(myfun,('apple', 'banana', 'cherry'),('orange', 'lemon', 'pineapple'))
print(res)
print(list(res))

# Example 3 -->
def Fun(n):
    return len(n)
res = list(map(Fun,('apple', 'banana', 'cherry')))
print(res)