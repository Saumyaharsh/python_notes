import cmath
import math
class Quadratic:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def roots(self):
        a = self.a
        b = self.b
        c = self.c
        d =((b*b) - (4*a*c))
        if(d>=0):
            print('First root is', (-b + math.sqrt(d))/2*a)
            print('Second root is ', (-b-math.sqrt(d))/2*a)
        else:
            d = d*(-1)
            p = math.sqrt(d)
            m = -b/2*a
            n = p/2*a

            z1 = complex(m,n)
            z2 = complex(m,-1*n)
            print('One root is ',z1)
            print('Other root is ',z2)
a = float(input('Enter the value of a'))
b = float(input('Enter the value of b'))
c = float(input('Enter the value of c'))
c1 = Quadratic(a,b,c)
c1.roots()



