'''
starts with underscore
Magic methods -> Defined in class
__len__ -> len()
__str__ -> str()
__repr__ -> repr()
__call__ -> obj()

'''
class Employee:
    name= "Harry"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return i
    def __str__(self):
        return "My name is Saumya"
    def __repr__(self):
        return "this is repr magic method"
    def __call__(self):
        print( "function is calling")
e = Employee()
print(str(e))
print(repr(e))
e()

#print(e.name)
#print(len(e))