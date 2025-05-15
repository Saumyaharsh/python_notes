'''
seek(),tell() part of builtin functions in io model
read mode-> wrapped in io 
using seek()
truncate(<size>) -> truncate the contents in files upto given size

'''

'''
with open('my_file2.txt','r') as f:
    print(type(f))
#move to the 10th type in the file
    f.seek(10)
# Read the next 5 bytes
    data = f.read(5)
    print(data)
    '''
f = open('sample.txt','w')
f.write('Hello World')
f.truncate(5)
f.close()
f = open('sample.txt','r')
print(f.read())
