'''
Double underscore lagane se private ho jaata hai -> class ke andar sabhi ko access milega par object access nahi karega
polymorphism-> Same method name but different results in a parent-child class
Static method -> waisa methods jo <classname>.<method name> krne sei hi access ho
                use @staticmethod 
Decorators: It is used when we have to implement some conditions
            @property -> ensure karta hai ki jo value de diya gya h ussei change nahi kar paaye
isinstance -> return true or false ki  object x yaa y class ka hai yaa nahi. Parent class par v true show karta h


'''
#protected,setter,abstraction
class Car:
    total_car = 0
    def __init__(self,brand,model): # init is a constructor
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    def get_brand(self):
        return self.__brand+'!'
    def full_name(self):
        return f"{self.__brand},{self.__model}"
    def fuel_type(self):
        return "petrol or Diesel"
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    @property
    def model(self):
        return self.__model
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
    def fuel_type(self):
        return "electric fuel"

    

my_tesla = ElectricCar('Tesla',"Model S","85kwh")
print(isinstance(my_tesla,ElectricCar))
print(isinstance(my_tesla,Car))

'''
print(my_tesla.full_name())
print(my_tesla.get_brand())
print(my_tesla.fuel_type())
safari = Car("Tata","Safari")
print(safari.fuel_type())
# directly accessing class variable
print(Car.total_car)
#print(my_tesla.__brand)

#print static methods
print(Car.general_description())

# safari.model = 'Jaguar' # cann0t change this because it becomes private
print(safari.model())

'''


'''
my_car = Car("Toyota","corolla")
print(my_car.brand)
print(my_car.full_name())
'''

class Battery:
    def battery_info(self):
        return "this is battery"
class Engine:
    def engine_info(self):
        return "This is engine"
class ElectricCarTwo(Battery,Engine,Car):
    pass
my_new_tesla = ElectricCarTwo("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
