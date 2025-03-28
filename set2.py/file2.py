'''
#program to perform arithmetic operations
def calculate(a,b,c):
    if c== '+':
        return a+b
    elif c=='-':
        return a-b
    elif c=='*':
        return a*b
    elif c=='/':
        if(b!=0):
            return a/b
        else:
            print('Invalid value of b')
a = float(input('Enter the value of a '))
b = float(input('Enter the value of b '))
c = (input('Enter the operation to be performed '))
a = calculate(a,b,c)
print(a)

'''

'''
#function to print npr and ncr
from math import factorial
n = int(input('Enter the value of n '))
r = int(input('Enter the value of r '))
a = factorial(n)//(factorial(r))*factorial(n-r)
b = factorial(n)//factorial(n-r)
print('npr is ',b)
print('ncr is ',a)

'''

'''

#area of pentagon
def calculate(p,s):
    area = (p*5*s*(0.5))
    return area
a = float(input('Enter apothem of the pentagon '))
b = float(input('Enter the side of the pentagon '))
area = calculate(p=a,s=b)
print('Area of given pentagon is ',area)

'''

'''

import math
def sum(a,d,n):
    m = math.log((2*a + (((2*n)-1)*d))/((2*a)-d))
    m = m/d
    return m

d = float(input('Enter the common difference of AP '))
a = float(input('Enter the first term of the AP '))
n = float(input('Enter the number of terms '))
ans = sum(a,d,n)
print('Required sum is ',ans)

'''

'''

#finding emi
def emi(p,r,n):
    a = p*r*((1+r)**n)/(((1+r)**n)-1)
    print('EMI is ',a)
p = float(input('Enter the loan amount '))
r = float(input('Enter the rate '))
n = float(input('Enter the number of years '))
r = r/12
n = n*12
emi(p,r,n)

'''

'''
#Sides of triangle
from math import sqrt
def triangle():
    a = float(input('Enter the first side of the triangle '))
    b = float(input('Enter the second side of the triangle '))
    c = float(input('Enter the third side of the triangle '))
    if a+b>c:
        print('The sum of {} and {} is greater than side {}'.format(a,b,c))
    elif c+b>a:
        print('The sum of {} and {} is greater than side {}'.format(b,c,a))
    elif c+a>b:
        print('The sum of {} and {} is greater than side {}'.format(c,a,b))
    s = (a+b+c)/2
    area_sq = s*(s-a)*(s-b)*(s-c)
    area = sqrt(area_sq)
    print('{} is the required area of the given triangle'.format(area))

triangle()

'''

'''
#Salesman question
def calculate(s):
    c = 0
    if s>=50000:
        c = (0.05)*s
    print('Total sales done by salesman is {} and the commission is {}'.format(s,c))
    if s>=80000:
        print("Remarrks : Excellent")
    elif s>=60000 and s<80000:
        print("Remarrks : Good")
    elif s>=40000 and s<60000:
        print("Remarrks : Average")
    elif s<40000 :
        print("Remarrks : Work hard")
a = int(input('Enter the sales done by person is week 1 '))
b = int(input('Enter the sales done by person is week 2 '))
c = int(input('Enter the sales done by person is week 3 '))
d = int(input('Enter the sales done by person is week 4 '))
e = a+b+c+d
calculate(e)

'''

'''
#Take a number as input and compute its factorial
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

a = int(input('Enter the number '))
ans = fact(a)
print("Required number is ",ans)
'''

'''

# fibonacci series
def fibo(n):
    if n==1:
        print(0)
        return
    a = int(0)
    b = int(1)
    print(a)
    print(b)
    for i in range(1,n-2+1):
        sum = a+b
        a = b
        b = sum
        print(sum)
n = int(input('Enter the number of terms '))
fibo(n)
'''

'''

def number(n):
   
    sum = int(0)
    rev = int(0)
    while n>0:
        ld = n%10
        sum+=ld
        rev = rev*10 + ld
        n = n//10
    print("The reversed number is : ",rev)
    print('Sum of digits is : ',sum)

n = int(input('Enter the number '))
number(n)

'''

'''

def prime(n):
    flag = False
    for i in range(2,n,1):
        if(n%i==0):
            flag = True
            break
    if flag==False:
        print('{} is prime'.format(n))
    else:
        print('{} is composite'.format(n))
n = int(input('Enter the number '))
prime(n)

'''