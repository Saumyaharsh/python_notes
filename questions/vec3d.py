from math import sqrt
class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        out = str(self.x) + 'i'
        if self.y>=0:
            out+='+'
        out += str(self.y) + 'j'
        if self.z>=0:
            out += '+'
        out += str(self.z) + 'k'
        return out
    def __add__(self,b):
        return vector(self.x+b.x,self.y+b.y,self.z+b.z)
    def __sub__(self,b):
        return vector(self.x-b.x,self.y-b.y,self.z-b.z)
    def __dot__(self,b):
        return vector(self.x*b.x,self.y*b.y,self.z*b.z)
    def __cross__(self,b):
        return vector(self.y*b.z - b.y*self.z,
               self.z*b.x - self.x*b.z,
               self.x*b.y - self.x*b.x)
    def __len__(self):
        a = sqrt((self.x * self.x) + (self.y*self.y) + (self.z * self.z))
        return a
    def __norm__(self):
        return vector(self.x//self.x, self.y//self.y,self.z//self.z)
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = v1 + v2
print(v3)
v4 = v1-v2
print(v4)
v5 = v1.__dot__(v2)
print(v5)
v5 = v1.__cross__(v2)
print(v5)
v6 = v1.__len__()
print (v6)
v7 = v1.__norm__()
print(v7)
