var1 = int(input('Enter first number: '))
var2 = int(input('Enter second number: '))
operation = input('Enter the operation to be operated: ')
output = ''
if(operation == '+'):
    output = var1 + var2
elif(operation == '-'):
    output = var1 - var2
elif(operation == '*'):
    output = var1 * var2
elif(operation == '/'):
    output = var1 / var2
else:
    print('Choose Operation From: +, -, *, / ')
    output = 'Error'
print('Output is : ', output)
