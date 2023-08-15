class Main:
    def __init__(self):
        self.name = "susheel"
        self.age = 21
    def update(self,age):
        self.age = age

    def compare(self,obj2):
        if obj2.age == self.age:
            return True
        else:
            return False
    def __str__(self):
        return (f"{self.name} {self.age}")    
    
obj1 = Main()
obj2 = Main()
obj1.update(30)
if obj1.compare(obj2):
    print("equal")
else:
    print("not equal")    
print(obj1)
print(obj2)