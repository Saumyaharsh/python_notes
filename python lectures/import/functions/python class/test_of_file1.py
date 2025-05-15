a = [1,2,3,4,5]
#print(a.append(6))
# returns none so it is operating in place no new list is formed


#print(a.extend('124'))
#returns none since it is operating in place no new copy of list is formed

# a.insert(1,'7') is also operating in place so it will not return anything

# operating in place
# print(a.remove(5))
a.pop()
print(a)

