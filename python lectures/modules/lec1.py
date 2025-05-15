'''

#import calc
#print(calc.add(a,b))
from calc import *
a = 8
b = 9
print(add(a,b))

'''
'''
import calc
print(__name__)
''' 
from calc import add
def fun1():
    add()
    print('From fun1')

def fun2():
    print('from fun2')
def main():
    fun1()
    fun2()
main()