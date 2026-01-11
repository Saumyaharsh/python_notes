from scipy import linalg
import numpy as np

def f(x,y,l_0,y_0):
    n = len(x)
    l1= []
    for i in range (0,n):
        e = y[i] - (y_0 + (l_0*x[i]))
        l1.append(e)
    e_max = abs(max(l1))
    e_min = abs(min(l1))
    s = e_max + e_min
    return s

n = int(input('Enter the number of points'))
x = []
y = []
for i in range(n):
    a = int(input(f"Enter {i+1} x point"))
    b = int(input(f"Enter {i+1} y point"))
    x.append(a)
    y.append(b)


# x = [-2,-1,0,1,2]
# y = [3,5,2,1,2]
# n = len(x)
xi = sum(x)
yi = sum(y)
x_2 = sum(num*num for num in x)
mul_list = list(map(lambda a,b: a*b , x,y))
x_y = sum(mul_list)
A = [[n,xi],[xi,x_2]]
B = [yi,x_y]
A_inv = linalg.inv(A)
#print(A_inv)
ans = np.dot(A_inv,B)
y_0 = ans[0]
l_0 = ans[1]
s = f(x,y,l_0,y_0)
print('straightness is ',s)
# print(ans)
