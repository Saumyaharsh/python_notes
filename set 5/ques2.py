
import keyboard
class Toolbooth:
    def __init__(self,paying_car_count=0,nonpaying_car_count=0,toll_collected=0):
        self.paying_car_count = paying_car_count
        self.nonpaying_car_count = nonpaying_car_count
        self.toll_collected = toll_collected
    def paying_car(self):
        self.paying_car_count+=1
        self.toll_collected+=50
    def nonpaying_car(self):
        self.nonpaying_car_count+=1
    def display_details(self):
        print('Paying cars number is ',self.paying_car_count)
        print('Non paying car number is ',self.nonpaying_car_count)
        print('Total toll collected is ',self.toll_collected)
a = Toolbooth()
while True:
    if keyboard.is_pressed('l'):
        a.paying_car()
        while keyboard.is_pressed('l'):
            pass
    elif keyboard.is_pressed('m'):
        a.nonpaying_car()
        while keyboard.is_pressed('m'):
            pass
    elif keyboard.is_pressed('esc'):
        a.display_details()
        break

    
    