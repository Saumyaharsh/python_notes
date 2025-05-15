#variable length argument

'''
def sum(a,*b):
    c = a
    for i in b:
        c = c + i
    print(c)
sum(5,6,34,78)

'''

'''

# default argument

def person(name,age = 10):
    print(name)
    print(age)
person('Navin',28) # age will be overrided here

 '''

'''''

#keyword argument

def person(name,age):
    print(name)
    print(age)
person(age=24,name='Navin')

'''''

def person(name,**data):
    print(name)
    print(data)
person('navin',age=28,city='Mumbai',mob = 98789898)
