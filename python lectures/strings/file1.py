'''
String sequence of characters
fruit[0:-3] -> fruit[0:len(fruit)-3]
fruit[-3:-1] -> fruit[len(fruit)-3: len(fruit)-1] -> fruit[2:4] -> including 2 but not 4


'''

name = "Harry,Shubham"
print(name[0:6])
print(len(name))
nm = "harry"
print(nm[-4:-2])  #nm[1:3] ar