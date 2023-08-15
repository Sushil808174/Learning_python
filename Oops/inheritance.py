class A:
    def fun1(self):
        print("this is fun1 inside class A")
    def fun2(self):
        print("this is fun2 inside class A")
class B(A):
    def fun3(self):
        print("this is fun3 inside class B")
    def fun4(self):
        print("this is fun4 inside class B")
    def fun5(self):
        print("this is fun5 inside class B")
class C(B):
    def fun6(self):
        print("this is fun6 inside class C")
    def fun7(self):
        print("this is fun7 inside class C")

obj1 = C()
obj1.fun5()