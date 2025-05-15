class pycharm:
    def execute(self):
        print('Compiling')
        print('running')
class Myeditor:
    def execute(self):
        print('Spell-check')
        print('convention check')
        print('Compiling')
        print('running')

        



class Laptop:
    def code(self,ide):
        ide.execute()
ide = Myeditor()
lap1 = Laptop()
lap1.code(pycharm)
