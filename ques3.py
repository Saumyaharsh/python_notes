class Point:
    def __init__(self):
        self.x = 0
        self.y = 0
    def read(self):
        a = int(input('Enter the abscissa'))
        b = int(input('Enter the ordinate'))
        self.x = a
        self.y = b
    def display(self):
        if self.x>0 and self.y>0:
            print('Point in first quadrant')
        elif self.x<0 and self.y>0:
            print('Point is in second quadrant')
        elif self.x<0 and self.y<0:
            print('Point is in third quadrant')
        elif self.x>0 and self.y<0:
            print('Point is in fourth quadrant')
a = Point()
a.read()
a.display()


