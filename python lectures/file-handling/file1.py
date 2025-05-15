'''

f = open('mydata.py','r')
#print(f.read())

#it will print first line
print(f.readline())

'''

'''
f1 = open('abc','w')
f1.write("Something")

'''
# to append data
f1 = open('abc','a')
f1.write('Laptop')

'''
#if data file exists
for data in f:
    f1.write(data)

'''

'''
f = open('my_click.jpg','rb')
for i in f:
    print(i)


'''
'''
f = open('my_click.jpg','rb')

f1 = open('MyPic.JPG','wb')

for i in f:
    f1.write(i)
'''
