'''
@property decorator lagane se method getter bann jaayega
@<function_name>.setter -> setter ban jaata h; pehle wo function name defined hona chahiye



'''

class MyClass:
    def __init__(self,value):
        self._value = value
    def show(self):
        print(f"Value is {self._value}")
    @property
    def ten_value(self):
        return self._value
    @ten_value.setter
    def ten_value(self,new_val):

        self._value = new_val/10
    
obj = MyClass(10)
obj.ten_value = 67
print(obj._value)
obj.show()