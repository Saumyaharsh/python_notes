'''

# 1. Addition, subtraction multiplication,division
a = int(input('Enter the first number'))
b = int(input('Enter the second number'))
c = input('Enter the operator')
if(c=='+'):
    print(f'Required sum is {a+b}')
elif(c=='-'):
    print(f'Required difference is {a-b}')
elif(c=='*'):
    print(f'Required product is {a*b}')
elif(c=='/'):
    if(b!=0):
        print(f'Required answer is {a//b}')
    else:
        print('Invalid value of b')

     
'''

'''

# 2  read marks of three subjects and print answer of them
a = float(input("Enter the marks of first subject "))
b = float(input("Enter the marks of second subject "))
c = float(input("Enter the marks of third subject "))
res = (a+b+c)/3
print(f'The average of sum of marks of three students is {res}')

'''

'''

#3 Convert kg to pound and vice versa
a = float(input("Enter the weight in kilogram"))
b = float(input("Enter the weight in pounds"))
c = 2.20462262
d = 0.45359237
print(f'There is {c*a} pounds in {a} kilogram')
print(f'There is {d*b} kilograms in {b} pounds')

'''

'''

#4 Print surface area of the prism

a = int(input("Enter the first side of prism "))
b = int(input("Enter the second side of prism "))
c = int(input("Enter the third side of prism "))
d = float(a)
e = float(b)
f = float(c)
res = ((2*d*e) + (2*e*f) + (2*d*f))
print(f"The surface area of prism is {res} ")

'''

'''

#5 Pool question
a = int(12)
b = int(7)
c = int(2)
res = a*b*c
res1 = float(res)/17
print(f'Required time is {(res1)} hours')


'''

'''

#6 Centigrade to fahrenheit and vice versa
a = float(input("Enter the temperature in fahrenheit "))
b = float(input("Enter the temperature in celsius "))
celsius = (a - 32) / 1.8
fahrenheit = (b * 1.8) + 32
print(f"{a} fahrenheit in celsuis is {celsius}C")
print(f"{b} celsius in fahrenheit is {fahrenheit}F")

'''
'''

#7 car question
a = float(10)
b = float(0)
t = float(20)
res = (a-b)/t
print(f'required acceleration is {res}')


'''

'''

#8 Earthquake question
a = float(input("Enter the Ritcher magnitude of the earthquake "))
if(a>float(1.0) and a<float(2)):
    print('Microearthquakes not felt or rarely felt')
elif(a>float(2) and a<float(4)):
    print('Very rarely cause damage')
elif(a>float(4) and a<float(5)):
    print('Damage done to weak buildings')
elif(a>float(5) and a<float(6)):
    print('Cause damage to only poorly constructed building')
elif(a>float(6) and a<float(7)):
    print('Cause damage to well built structure')
elif(a>float(7) and a<float(8)):
    print('Cause damage to most buildings')
elif(a>float(8) and a<float(9)):
    print('Cause major destruction')
elif(a>float(9) ):
    print('Cause unbelievable damage')

'''

'''

#9 ques 1
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(i ,end='')
    print(end='\n')

# ques 2
for i in range(1,6,1):
    a = int(i)
    for j in range(1,6,1):
        if(j >= 5-i+1 and j<= 5):
            print(a ,end='')
            a-=1
        else:
            print(" ",end='')

        
    print(end='\n')

'''

'''

#Add even numbers

sum = int(0)
for i in range(100,201,2):
    sum += i
print(sum)   #7650

'''



#Series sum
# question 1
'''

a = float(1)
n = float(input("Enter the number of terms "))
sum = float(0)

while(n>float(0)):
    sum += (a/n)
    n-=1
print(f'Required sum is {sum}')

'''

'''

#question 2
n  = float(input("Enter the number of terms "))
j = 1
res = float(1)
while(n>float(1)):
    res += (((n*10)+n)/n)
    n-=1
    
print(f"The required result is {res}")

'''

'''

# to calculate depreciation value
a = float(input('Enter purchase value '))
b = float(input('Enter value of depreciation '))
t = float(input('Enter the time '))
dep_value = (b-a)/t
print(f"Required value is {dep_value}")

'''

