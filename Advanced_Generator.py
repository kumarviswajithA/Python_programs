# Generator : Generator look's like a function but generator contains Yield keyword by using this yield keyword we
#             return multiple values.
import time
def generator():
    for i in range(1,21):
        yield i
res = generator()
# for j in res:
#     time.sleep(0.25)
    # print(j)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))

# Example : 2 -->

def gen():
    yield [x**2 for x in range(1,21)]
result = gen()
for i in result:
    time.sleep(0.25)
    print(i)
# print(next(result))