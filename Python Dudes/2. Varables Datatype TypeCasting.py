var1 = 'Hello AG, ' # String Variable(Stores sentences, words, charecters
var2 = 4 # Integer Variable(Stores Numbers)
var3 = 36.7 # Floating Point Variable(Stores Decimal Nos.)
'''Printing Variables'''
print(var1)
print(var2)
print(var3)
'''Printing Variable Types'''
print(type(var1))
print(type(var2))
print(type(var3))
'''Operations between variables'''
var4 = 'Ashmit JaiSarita Gupta'
print(var1 + var4)
print(var2 + var3)
'''Type Casting: Changing one datatype to another'''
'''Some Type Cast functions: 1. int()
                             2. str()
                             3. float()'''
var5 = ' 32 '
print(int(var5) + var2)
print(var5 + str(var2))
print(var3 + float(var5))
'''printing an string for n times'''
print(10 * ' AG ')
print(10 * 'AG\n')
print(100 * str(int(var5) + var2))
print(100 * int(var5) + var2)
'''taking input from user'''
print('Enter an number: ')
inpnum = int(input()) # B default input is always string type so int() is used to convert input into integer type
print('You Entered : ', inpnum)
