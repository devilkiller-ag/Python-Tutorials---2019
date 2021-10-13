mystr = 'ag is a good boy'
print(mystr)
'''Finding length of string'''
print('''Finding length of string''')
print(len(mystr))
'''Slicing of String'''
print('''Slicing of String''')
print(mystr[4])
print(mystr[0:4])
print(mystr[0:17]) # = print(mystr)
print(mystr[0:878]) # = print(mystr[0:17]) = print(mystr)
print(mystr[0:])
print(mystr[:5])
'''Advance Slicing: Extended Slicing'''
print('''Advance Slicing: Extended Slicing''')
print(mystr[::])# = [0:17:1] = [:17:1] = = [::1] = [0::1]; very important syntax
print(mystr[0:7:2])# very important syntax; th)is will print the slice 0:5 with 1 character skiped after each character
print(mystr[0::2])# very important syntax; this will print the slice 0: with 1 character skiped after each character
print(mystr[::34545645])
'''Advance Slicing: Negetive index slicing'''
print('''Advance Slicing: Negetive index slicing''')
print(mystr[-1:0])
print(mystr[-4:]) # = [12:]
print(mystr[-4:-2]) # = [12:14] = [12:-2] = [-4:14]
print(mystr[::-1]) # advance technique to reverse the string
print(mystr[::-2]) # first reverses the string and then skips 1 character after each character
'''Some Functions in String'''
print('''Some Functions in String''')
print(mystr.isalnum()) #checks whether the function is alphanumeric or not; returns false because mystr has spaces
print(mystr.isalpha()) #checks whether the function is alpha or not
print(mystr.endswith('boy'))
print(mystr.count('o'))
print(mystr.capitalize())
print(mystr.find('is')) #returns the index from where 'is' first occurs in mystr
print(mystr.upper())
print(mystr.lower())
print(mystr.replace('is', 'is not'))