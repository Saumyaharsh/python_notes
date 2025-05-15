'''
Method overriding is a way to change methods coming from parent class to child class in child class
Powerful property of oop



'''
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x*self.y
class circle(Shape):
    def __init__(self, x):
        self.x = x
    def area(self):
        return 3.14*self.x*self.x
c = circle(5)
print(c.area())

    

        