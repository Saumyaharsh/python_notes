class student:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return((self.m1+self.m2+self.m3)/3)
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value
    @classmethod #class method
    def info1(cls): #writing cls is compulsory
        return cls.school
    @staticmethod
    def info():
        print("this is a student class")




s1 = student(34,67,32)
s2 = student(89,32,12)
print(s1.avg())
print(student.info1())
student.info()
