# two methods having same name in class with different parameters -> we call it method overloading(not in python)
# method overriding -> two methods with same name,same no. of same paramters in different class having inheritance
'''

# method overloading
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c =None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s=a
        return a
s1 = student(58,69)
print(s1.sum(5))
'''
class A:
    def show(self):
        print('in a A show')
class B(A):
    def show(self):
        print('in a show B')

a1 = B()
a1.show() # pehle apne mei dekhega agar wo method khud me naa mile tab parent mei dekhega