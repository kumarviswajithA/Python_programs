# Inheritance : By using inheritance concept we inherit the variables and methods from super class to sub class.
#                 1. Single-level inheritance
#                 2. Multi-level  inheritance
#                 3. Multiple inheritance
#                 4.Hirarical inheritance

# Single level inheritance

class A:
    def fun1(self):
        print("Iam in fun1")
    def fun2(self):
        print("Iam in fun2")
class B(A):
    def fun3(self):
        print("Iam in fun3")
    def fun4(self):
        print("Iam in fun4")
obj = B()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()


# Multi-level inheritance

class A:
    def fun1(self):
        print("Iam in fun1")
    def fun2(self):
        print("Iam in fun2")
class B(A):
    def fun3(self):
        print("Iam in fun3")
    def fun4(self):
        print("Iam in fun4")
class C(B):
    def fun5(self):
        print("Iam in fun5")
    def fun6(self):
        print("Iam in fun6")
obj = C()
obj.fun6()
obj.fun5()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()

# Multiple inheritance

class A:
    def fun1(self):
        print("Iam in fun1")
    def fun2(self):
        print("Iam in fun2")
class B:
    def fun3(self):
        print("Iam in fun3")
    def fun4(self):
        print("Iam in fun4")
class C(A,B):
    def fun5(self):
        print("Iam in fun5")
    def fun6(self):
        print("Iam in fun6")

obj = C()
obj.fun6()
obj.fun5()
obj.fun4()
obj.fun3()
obj.fun2()
obj.fun1()


# Heirarical inheritance

class A:
    def fun1(self):
        print("Iam in fun1")
    def fun2(self):
        print("Iam in fun2")
class B(A):
    def fun3(self):
        print("Iam in fun3")
    def fun4(self):
        print("Iam in fun4")
class C(A):
    def fun5(self):
        print("Iam in fun5")
    def fun6(self):
        print("Iam in fun6")
obj1 = C()
obj2 = B()
obj1.fun1()
obj1.fun2()
obj1.fun5()
obj1.fun6()
obj2.fun2()
obj2.fun1()
obj2.fun3()
obj2.fun4()

