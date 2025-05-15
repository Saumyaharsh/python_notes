'''
Set methods 
1. Union -> elements in both the sets
2. update -> s1.update(s2) s1 mei wo values v le aao jo s2 mei nahi h
3. symetric difference -> wo saari values jo common nahi h
a union b - a intersection b
4 isdisjoint-> 2 set ke bich agr koi intersection nahi h toh , will return 0
5 superset -> set which contain all elements of the set is callled superset of that set
6. subset -> A is present in B then A is subset in B
7. <set>.discard(<notpresent_in_set) -> Will not throw error
8. <set>.remove(<notpresent_in_set>) -> it will throw error
9. pop -> koi element pop hoge
10. del -> can delete entire set
11. clear -> delete all elements
12. if <name> in <setname>
'''

'''
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2) 
'''
cities = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Tokyo','Seoul','Kabul'}
print(cities.isdisjoint(cities2))

cities3 = cities.intersection(cities2)
#cities.intersection_update(cities2)
print(cities3)
#print(cities)
cities4 = cities.difference(cities2)
print(cities4)
print(cities3.issubset(cities))
print(cities.issuperset(cities3))
if "Tokyo" in cities:
    print("yes")

