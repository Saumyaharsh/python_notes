chai_types = {"Masala":"spicy","Ginger":"Zesty","Green":"Mild"}
print(chai_types)

# accessing individual items
print(chai_types["Masala"])
#using mehtod , we have to gve key
print(chai_types.get("Masala"))

# changing value of key
chai_types["Green"] = "Fresh"
print(chai_types.get("Green"))

# printing keys
for chai in chai_types:
    print(chai)

# printing keys and values
for chai in chai_types:
    print(chai , chai_types[chai])

# iterating over dictionary
for key,values in chai_types.items():
    print(key, values)

# using if
if "Masala" in chai_types:
    print('I have masala chai')

#printing length
print(len(chai_types))

# adding new key
chai_types["Earl Grey"] = "citrus"
print(chai_types)

# pop -> wwe have to provide key
chai_types.pop("Ginger")
print(chai_types)
#returning last item
print(chai_types.popitem())

#Deleting items
del chai_types["Green"]
print(chai_types)

#making copy
chai_types_copy = chai_types.copy()

# dictionary inside dictionary
tea_sop = {
    "chai":{"Masala":"Spicy","Ginger":"Zesty"},
    "Tea":{"Green":"Mild","Black":"String"}
}
print(tea_sop)

# accessing value of tea_sop
print(tea_sop["chai"])
print(tea_sop["chai"]["Ginger"])

# squared number
squared_num = {x:x**2 for x in range(6)}
print(squared_num)
# clearing all values
squared_num.clear()
print(squared_num)

#Using keys
keys = ["Masala", "Lemon","Ginger"]
default_value = "Delicious"
new_dict = dict.fromkeys(keys,default_value)
print(new_dict)
new_dict = dict.fromkeys(keys,keys)
print(new_dict)


