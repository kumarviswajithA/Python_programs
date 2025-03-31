# Decorator : Decorators are used to modify or Extend the behaviour of an existing function or method without changing
#             their Actual code.

def Decorator(fun):
    def method(a,b):
        fun(a,b)
        print("Sub = ",a-b)
        print("mul = ",a*b)
        print("div = ",a/b)
        print("mod = ",a%b)
    return method
@Decorator
def Sum(a,b):
    print("Sum = ",a+b)
a = int(input("Enter a value : "))
b = int(input("Enter b value : "))
Sum(a,b)