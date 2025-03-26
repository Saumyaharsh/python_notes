class Library:
    def __init__(self):
        self.acc_number = 32
        self.publisher = "rohan"
        self.title = "Forest of Enchantments"
        self.author = 'Chitra Baneerjee'
    def read(self):
        a = float(input("Enter the account number"))
        b = (input('Enter the publisher name'))
        c = input('Enter the title')
        d = input('Enter the name of author')
        self.acc_number = a
        self.publisher = b
        self.title = c
        self.author = d
    def compute(self):
        a = int(input("Enter the number of days late "))
        b = float(1.5*a)
        print('Fine of late days is $',b)
    def display(self):
        print(self.acc_number)
        print(self.publisher)
        print(self.title)
        print(self.author)
       
a = Library()
a.read()
a.compute()
a.display()

        


