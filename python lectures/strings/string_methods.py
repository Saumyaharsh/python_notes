'''
strings are immutable
you cannot change it in place (but can change it)
but can make a new copy
.rstrip() -> strip trailing part -> peeche ka part
.rplace(<name1>,<name2>) -> replace all instances of name 1
.split -> converts string in list
.capitalize() -> Capitalize the first letter of string and convert all characters to lowercase
.center(<no._of_spaces>) -> add spaces in front
.count(<name>) -> count number of given terms
.endswith('value') -> return true or false
.endswith('to',<start idx>,<end idx+1>)
.find(<string>) -> returns index of string if found  else return -1
.index(<string>) -> throw error if not found if found then return index
.isalpha()
.isaphanum()
.islower()
.isprintable() -. if\n then return false
.isspace() -> if whitespaces or tab there
.istitle() -> return true if all letters is capital
.isupper() ->
.startswith(<string_name>)
.swapcase() -> convert upper to lower and upper to lower
.title() -> convert each letter capiatal
'''



a = "Harry!!!!!!! Harry Saumya"

print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip('!'))
print(a.replace("Harry","John"))
print(a.split(' '))
blogHeading = 'introduction tO jS'
print(blogHeading.capitalize())
print(a.center(5))
print(a.count("Harry"))
str1 = "Welcome to the console!!!"
print(str1.end('!!!'))
print(a.endswith('to',4,10))
str2 = "He's name is Dan. He is an innocent man"
print(str1.find('is'))
print(str1.index('is'))
print(str1.isalnum)
print(str1.isalpha)
str3 = "hello world"
print()


