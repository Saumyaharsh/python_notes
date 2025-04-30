my_str = str(input("Enter the roman number "))
dict = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
n = int(len(my_str))
ans = 0
for i in range(1,n,1):
    if dict[my_str[i-1]] >= dict[my_str[i]]:
        ans += dict[my_str[i-1]]
    else:
        ans -= dict[my_str[i-1]]
ans+=dict[my_str[n-1]]
print(f'{ans} is the required number')
