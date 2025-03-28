'''

#Diamond pattern
n = int(input('Enter the number of rows '))
a = int(n/2)
b = int(n-2)
for i in range(0,a+1):
    for space in range(1,a-i+1):
        print(" ",end='')
  
    for j in range(1,(2*i)+2):
        print('*',end='')
    print()
    
for i in range(1,a+1):
    for space in range(1,i+1):
        print(" ",end='')
        
    for j in range(1,b+1):
        print("*",end='')
    b-=2
    print()

    ''' 

'''
#Sahi run nahi ho rhah
# print the pattern
n = int(input('Enter the number of rows '))
for i in range(0,n):
    a = int(i)
    for space in range(1,n-i):
        print(" ",end='')
    for j in range(0,(2*i)+1):
        b = (2*i)+1
        if j>=b/2:
            a-=1
        else:
            a+=1
        print(a,end='')
    print()

'''


#Pascal Triangle
from math import factorial
a = int(input('Enter the number of rows '))
n = int(a)
for i in range(0,a):
    for k in range(1,n-i):
        print(end=' ')
    for j in range(0,i+1):
        a = factorial((i))//(factorial((j))*(factorial((i-j))))
        print(a,end=' ')
    print()







    