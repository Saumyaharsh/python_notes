def update(x):
    x = 8
    print(x)
a = 10
update(a)
print(a)

#Call by value and call by reference
#Pass by reference means address is passed
#Pass by value mei different memory location 
# In python we have no such concept
# In python everything is object
# When we call a function both variable inside function and passed variable have same id that is they point to
# same memory location , but here after updating x = 8 the id of 8 gets changed,earlier both a and x was having same id
