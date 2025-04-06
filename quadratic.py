import cmath
from math import sqrt
def quadratic(a,b,c):
    d = (b*b)-(4*a*c)
    if d>=0:
        d1 = sqrt(d)
        r1 = (-b/(2*a))+(d1/(2*a))
        r2 = (-b/(2*a))-(d1/(2*a))
        print('{} and {} are the roots of the quadratic equation'.format(r1,r2))
    elif d<0:
        d = d*-1
        d1 = sqrt(d)
        r = (-b/(2*a))
        i = (d1/(2*a))
        z1 = complex(r,i)
        z2 = complex(r,-1*i)
        print('{} and {} are the roots of the given quadratic equation'.format(z1,z2))
a = float(input('Enter the value of a '))
if a==0:
    print('Invalid value of a, a can never be zero ')
elif a!=0:
    b = float(input('Enter the value of b '))
    c = float(input('Enter the value of c '))
    quadratic(a,b,c)

        