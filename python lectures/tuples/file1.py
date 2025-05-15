'''
cannot change the tuple
We can print the tuple
In tuple also there is positive indexing as well as negative indexing
tup[:3] = tup[0:3]
tup[1:] = tup[1:<length of tuple>]
Tuples are immutable
Sets are imutable
Lists are mutable

'''
tup = (1,5,6)
print(type(tup))
print(tup)
tup1 = (1,)
print(tup1)
print(tup[0])
print(tup[-1])
print(tup[2])

if 5 in tup:
    print('Yes')
else:
    print('No')

tup2 = tup[1:4]
print(tup2)
for value  in tup:
    print(value)