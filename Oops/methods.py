class School:
    school = "masai"

    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        print("This is static method inside student class..")



obj1 = School(22,33,44)
obj2 = School(44,22,11)

print(obj1.avg())
print(obj2.avg())

print(School.getSchool())
School.info()