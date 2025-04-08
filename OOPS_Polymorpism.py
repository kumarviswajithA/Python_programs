# Polymorphism : Polymorphism means many forms in this concept we have method overloading and method overriding

# Method overloading :

class A:
    def sum(self,a,b):
        self.a = a
        self.b = b
        return a + b
    def sum(self,a,b,c=1):
        self.c = c
        return a + b + c
obj = A()
print(obj.sum(2,3))

# Method Overriding :

class A:
    def sum(self,a,b):
        self.a = a
        self.b =  b
        return a + b
class B(A):
    def sum(self,a,b):
        self.a = a
        self.b = b
        return a + b
obj = B()
print(obj.sum(1,2))
