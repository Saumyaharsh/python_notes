class BankAccount:
    def set_details(self,name,contact,balance=0):
        self.name = name
        self.contact = contact
        self.balance = balance
    def withdraw(self,amount):
        self.balance = self.balance-amount
    def deposit(self,amount):
        self.balance = amount+self.balance
    def display_details(self):
        print('Name of the person is ',self.name)
        print('Contact of the person is ',self.contact)
        print('Net balance in the account of the person is ',self.balance)

a = BankAccount()
b = BankAccount()
a.set_details('s',56,100)
a.withdraw(50)
a.deposit(10)
a.display_details()
b.set_details('p',56,99)
a.withdraw(10)
a.deposit(50)
a.display_details()