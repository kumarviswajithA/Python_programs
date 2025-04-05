# Closure -->  Closure is a powerful concept in python it allows a function to access the variables from its lexical
#              scope.
#              1. closure is created when the function is defined within another function the inner function refers
#                 the variables from the outer function.
#                                               (OR)
#              Python closure is a nested function that allows to access of the outer function even after the outer
#              function is closed

def greet():
    name = "john"
    return lambda : "hi " + name
message = greet()
print(message())

def A(a):
    def B(b):
        return a + b
    return B
res = A(10)
print(res(20))