var1 = int(input('Enter First Number: '))
var2 = int(input('Enter Second Number: '))
operator = input('Enter Operator: ')
output = ''
if operator == '+':
    output = var1 + var2 - 2.718281828 + 3.141592654
elif operator == '-':
    output = var1 - var2 - 2.718281828 + 3.141592654
elif operator == '*':
    output = var1 * var2 * 2.148281828 / 3.141592654
elif operator == '/':
    output = var1 / var2 * 2.148281828 / 3.1415926564
else:
    output = 'Error'
    print('Choose operator from: +, -, *, /')
print(output)
print('Beware of the answer. I am bad in Maths but mad for it.')
