from scipy.linalg import inv
class matrix:
    def __init__(self,a1,n1,m1):
        self.a1 = a1
        
        self.n1 = n1
        self.m1 = m1
       
    def __add__(self,b):
        
        if self.n1==b.n1 and self.m1 == b.m1:
            ans_matrix = []
            for i in range(0,self.n1):
                l1= []
                ans = 0
                for j in range(0,self.m1):
                    ans  = self.a1[i][j] + b.a1[j][i]
                    l1.append(ans)
                ans_matrix.append(l1)
        else:
            print('Invalid size')
        return ans_matrix
    def __sub__(self,b):
        
        if self.n1==b.n1 and self.m1 == b.m1:
            ans_matrix = []
            for i in range(0,self.n1):
                l1 = []
                ans = 0
                for j in range(0,self.m1):
                    ans = self.a1[i][j] - b.a1[i][j]
                    l1.append(ans)
                ans_matrix.append(l1)
        else:
            print('Invalid size')
        return ans_matrix
    def __mul__(self,b):
        ans_matrix = []
        if self.m1 == b.n1:
            for i in range(0,self.n1,1):
                ans = 0
                l1 = []
                for j in range(0,self.m1,1):
                    val =  self.a1[j][i]*b.a1[j][i]
                    ans += val
                    l1.append(ans)
                ans_matrix.append(l1)
            return ans_matrix
        else:
            print('Invalid size')
            
        

    def __inv__(self):
        ans = inv(self.a1)
        return ans
    
# n1 = int(input('Enter the no. of row of matrix1 '))
# m1 = int(input('Enter the no. of column of matrix 1 '))
# n2 = int(input('Enter the no. of row of matrix2 '))
# m2 = int(input('Enter the no. of column of matrix2 ' ))
# array1 = []
# array2 = []
# for i in range(0,n1):
#     l1 = []
#     for j in range(0,m1):
#         a = float(input('Enter elements of matrix1 '))
#         l1.append(a)
#     array1.append(l1)
# for i in range(0,n2):
#     l1 = []
#     for j in range(0,m2):
#         a = float(input('Enter elements of matrix2 '))
#         l1.append(a)
#     array2.append(l1)
    
# m1 = matrix(array1,n1,m1)
# m2 = matrix(array2,n2,m2)
# ans = m1+m2
# ans2 = m1 - m2
# ans3 = m1*m2
# ans4 = m1.__inv__()
# print(ans)
# print(ans2)
# print(ans3)
# print(ans4)
f = open('file1.txt','r')
l1 = (f.read())


array1 = []

a = l1.split('\n')
print(a)
for line in a:
    m = line.split(',')
    l1 = []
    for charc in m:
        p = int(charc)
        l1.append(p)
    array1.append(l1)


f = open('file2.txt','r')
l12 = (f.read())
array2 = []

a2 = l12.split('\n')

for line in a2:
    m2 = line.split(',')
    l2 = []
    for charc in m2:
        p = int(charc)
        l2.append(p)
    array2.append(l2)

n1 = len(array1)
m1 = len(array1[0])
n2 = len(array2)
m2 = len(array2[0])
mat1 = matrix(array1,n1,m1)
mat2= matrix(array2,n2,m2)
ans = mat1+mat2
ans2 = mat1 - mat2
ans3 = mat1*mat2
ans4 = mat1.__inv__()
print(ans)
print(ans2)
print(ans3)
print(ans4)