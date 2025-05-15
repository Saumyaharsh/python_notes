class Computer:
    def __init__(self,cpu,ram):
        self.cpu= cpu
        self.ram = ram

  
        
    def config(self):
        print(self.cpu)
        print(self.ram)



a = '8'

comp1 = Computer(13,13)
comp2 = Computer(23,78)
comp1.config()
comp2.config()
