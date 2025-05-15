from abc import ABC,abstractmethod
'''
You cannot create object of an abstract class
You can pass abstract class to a class
Abstract class help in designing class
You can have mamy abstract method
ABC->Abstract Base Classes
Abstract class -> aisa abstract class jisme atleast ek abstractmethod ho
using @abstractmethod decorator -> koi v method abstract method bann jaata h
Abstract method mei koi code nahi likha hua hota h
Abstraction se higher level class lower level class ko kucch chize karne parr mazbur kar deta h
Abstract class can have concrete method as well as abstract method but it need to have at least oe abstract class
'''

'''
class Whiteboard:
    def write(self):
        print('its writing')
class Computer(ABC):
    @abstractclassmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("it's running")
class Programmer:
    def work(self):
        print('Solving Bugs')
        com.process()
#com = Computer()
#com.process()
com1 = Laptop()
com2 = Whiteboard()
#com1.process()
prog1 = Programmer()
prog1.work(com1)

'''

class BankApp(ABC):
    def database(self):
        print('connected to database')
    @abstractmethod
    def security(self):
        pass
class MobileApp(BankApp):
    def mobile_login(self):
        print('login into mobile')
    def security(self):
        print('Mobile security')
         # Here this method overrides the previous one and the detalis inside this method will be printed
         # not the details inside abstract method of the previous class
