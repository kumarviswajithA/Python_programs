# Iterator : In python, Iterators ia an object it allows you to iterate over the collection of data like lists, tuples,
#            sets.


class A:
    def __iter__(self):
        self.n = 2
        return self
    def __next__(self):
        x = self.n
        self.n += 2
        return x

obj = A()
res = iter(obj)
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