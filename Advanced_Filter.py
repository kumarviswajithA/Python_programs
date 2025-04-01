# Filter : Filter method filter the given sequence with the help of the function that test  each element in the sequence
#          to be true or not.

# Example 1 -->
l = [1,2,3,4,5,6,7]
res = list(filter(lambda a:a>2,l))
print(res)

# Example 2 -->  Filter the array, and return a new array with only the values equal to or above 18:

ages = [5, 12, 17, 18, 24, 32]

def myfun(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myfun,ages)

for x in adults:
    print(x)
