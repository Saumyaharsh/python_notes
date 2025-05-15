a = [1,2,3,4,7,9]
a.sort() #work for only
print(a)
a.sort(reverse='True')
print(a)
a.append(9)
print(a)
a.extend('abc')
print(a)
a.insert(1,9)
print(a)
a.append('mangoes')
print(a)
a.extend('a')
print(a)
#remove the first occurence of element provided
a.remove(9)
print(a)
a.append(9)
print(a)
print(a.count(9))
#remove the element at the given index and return it
print(a.pop(5))
print(a)
'''
a.clear()
print(a)
// deletes all the elements in the list
del a 
// removes the list a from the memory

'''
a.reverse()
print(a)
b = a.copy()
print(b)
# a.extend(1) int is not iterable
# a.extend('1') add 1 to the last of list since string is iterable
print(len(a))
print(a.pop()) # returns the last element
print(a)
print(type(a.pop())) # returns int 


