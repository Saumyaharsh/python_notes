
f1 = open('abc.txt','w')
f1.close()
f2 = open('abc.txt','a')


for i in range(0,5,1):
    b=''
    for j in range(0,5,1):
        a = float(input('Enter the number'))
       
        b = b + str(a) + "  "
    f2.write(b)
    f2.write('\n')
f2.close()



f3 = open('abc.txt','r')
i = 0
l2 = []
while True:
    l1 = []
    i = i+1
    line = f3.readline()
    if not line:
        break
    m1 = line.split("  ")[0]
    m2 = line.split("  ")[1]
    m3 = line.split("  ")[2]
    m4 = line.split("  ")[3]
    m5 = line.split("  ")[4]
    l1.append(m1)
    l1.append(m2)
    l1.append(m3)
    l1.append(m4)
    l1.append(m5)
    l2.append(l1)
print(l2)



    

