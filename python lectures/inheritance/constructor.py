'''
class A:
    def __init__(self):
        print("In init of A")
    def feature1(self):
        print('feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')
class B(A):
    def __init__(self):
        super().__init__()
        print('In init of B') 
    def feature3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')
b = B() # it will access init of b when super. method is not given, if it is given then it will go to init of B then init of A then init of B

'''
class A:
    def __init__(self):

        print("In init of A")
    def feature1(self):
        print('feature 1-A is working')
    def feature2(self):
        print('Feature 2 is working')
class B:
    def __init__(self):
        print("In init of B")
    def feature1(self):
        print('Feature 1-B is working')
    def feature4(self):
        print('Feature 4 is working')
class C(A,B): #MRO method resolution order that is from left to right , that is A will more preferred than b
    # because A is in the left of B
    def __init__(self):
        super().__init__()
        print("In init of C")
    def feature1(self):
        super().feature1()
        print('Feature 4 is working')
c = C()
c.feature1()

