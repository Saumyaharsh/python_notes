a = str(input('Enter the filename '))
my_str = str(input('Enter the content of file (only letters) '))
vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

f1 = open(a,'w')
f1.write(my_str)
f1.close()
f2 = open(a,'r')
text = f2.read()
vowel = 0
consonant = 0
for char in text:
    if char in vowels:
        vowel += 1
    elif char in consonants:
        consonant+=1

    
    
print('Consonants are {} and vowels are {}'.format(consonant,vowel))

