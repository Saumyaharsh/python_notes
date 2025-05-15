from functools import reduce

'''

def is_even(n):
    return n%2==0


nums= [3,2,6,8,4,6,2,9]
evens = list(filter(is_even,nums))
print(evens)

'''

'''
nums= [3,2,6,8,4,6,2,9]
evens = list(filter(lambda n: n%2==0,nums))
print(evens)


'''

'''

#Using maps
nums = [3,2,6,8,4,6,2,9]
doubles = list(map(lambda n : n+2,nums))
print(doubles)

'''
 #using reduce
 #import it from functools module
nums= [3,2,6,8,4,6,2,9]
sum = reduce(lambda a,b: a+b,nums)
print(sum)
