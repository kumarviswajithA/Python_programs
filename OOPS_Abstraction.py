from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def fun1(self):
        None
    def fun2(self):
        print("hello")
class B(A):
    def fun1(self):
        print("hi")
obj = B()
obj.fun2()
obj.fun1()