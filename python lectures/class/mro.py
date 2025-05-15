'''
mro is used in inheritance in python
child pehle apna same name waale fun chalata, then according to mro

'''
class Grandparent:
    def grand_func(self):
        print('This is grand funcn from grandparent')
class Father(Grandparent):
    def grand_func(self):
        print("This is grand func from father")
class Uncle(Grandparent):
    def grand_func(self):
        print("this is grand_func from uncle")
class Child(Father,Uncle,Grandparent):
   
   def grand_func(self):
    super(Father,self).grand_func()

    #    print("This is grand func from child")
    pass
obj = Child()
obj.grand_func()
print(Child.__mro__)
