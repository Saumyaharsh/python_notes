'''

a = 10
def something():
    a = 12
    print("in fun",a)

something()
print("outside",a)

'''

'''

a = 10
def something():
    global a
    a = 15
    print("in fun",a)
something()
print('outside a',a)

'''

'''

a = 10
print(id(a))
b = 9
c = 8
def something():
    a = 9
    x = globals()['a']
    print(id(x))
    print("in fun",a)
    globals()['a'] = 15
something()
print('outside a',a)

'''



