class Demo:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addNumber(self):
        return self.a+self.b
    def mulNumber(self):
        return self.a*self.b
    
obj1 = Demo(4,5);
add = obj1.addNumber();
print(add)
obj2 = Demo(5,9)
mul = obj2.mulNumber()
print(mul)