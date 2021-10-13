'''
Operators in python:
Arithmatic Operators: +, -, *, /, //, **, %
Assignment Operators: =, +=, -=, *=, /=, //=, **=, %=
Comparision Operators: <, >, <=, >=, ==, !=
Logical Operators: and, or
Identity Operators: is, is not
Membership Operators: in, not in
Bitwise Operators: Works on binary numbers (0 and 1): &, |, etc
'''
#Arithmatic Operators
print('Arithmatic Operators')
print('5 + 4 is ', 5 + 4)
print('5 - 4 is ', 5 - 4)
print('5 * 4 is ', 5 * 4)
print('5 / 4 is ', 5 / 4)
print('5 // 4 is ', 5 // 4)#floor division
print('5 ** 4 is ', 5 ** 4)#power
print('5 /% 4 is ', 5 % 4)

#Assignment Operators
print('Assignment Operator')
r = 5
print(r)
r += 9
print(r)

#Logical Operators
print('Logical Operators')
a = True
b = False
print(a and a)
print(a and b)
print(b and b)
print(a or b)
print(a or a)
print(b or b)

#Identity Operators
print('Identity Operators')
print( a is b)
print(a is not b)

#Membership Operators
print('Membership Operators')
lists = [1, 76, 79, 4, 5, 90]
print(1 in lists)
print(1 not in lists)

#Bitwise Operators
'''
0 - 00
1 - 01
2 - 10
3 - 11
'''
print('Bitwise Operators')
print(0 & 2)
print(0 | 3)
