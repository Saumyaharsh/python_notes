'''
Four types of arguments
default arguments
Keyword arguments -> a= 9 b=4 -> passing as paramter -> don't need to give order
reqired argument
if no value is returned we will get none

'''

#default arguments
# def average(a=5,b=9):
#     print('The average is '+ (a+b)/2)

def average(*numbers): # It takes numbers as a tuple
    sum = 0
    for i in numbers:
        sum = sum+i
    #print('Average is:',sum/len(numbers))
    return sum/len(numbers)
c = average(5,6,7,9,1)
print(c)

# If we want to take numbers as a dictionary
def name(**value):
    print("Hello,",value["fname"],value["mname"],value["lname"])
name(mname="bachan",lname="Barnes",fname="James")