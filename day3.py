
class Car:
    color = "Red"
    brand = "Toyota"
    def show_details(self):
        print(self.color,self.brand)

        #How to make an object of this class
class Car:
    # creating constructors
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    #creating function
    def display_info(self):
        print(self.brand)
        print(self.model)
        print(self.year)
        
#creating objects
car1 = Car("T","C",2022)
car1.display_info()

# The __str__() Method