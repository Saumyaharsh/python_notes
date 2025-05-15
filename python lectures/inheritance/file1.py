'''

class A:
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')
class B(A):
    def feature3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')
b = B()
b.feature1()
'''

'''
#Multi level inheritance
class A:
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')
class B(A):
    def feature3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')
class C(B):
    def feature(self):
        print('Feature 4 is working')
c = C()
c.feature2()
'''
#Multi level inheritance
class A:
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')
class B:
    def feature3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')
class C(A,B):
    def feature(self):
        print('Feature 4 is working')
c = C()
c.feature1()
b = B()
b.feature3()