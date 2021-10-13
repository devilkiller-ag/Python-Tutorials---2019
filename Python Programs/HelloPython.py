print('Hello Python')

#Store input numbers:
num1 = input('Enter First Number: ')
num2 = input('Enter Second Number: ')

#Add two numbers
sum = float(num1) + float(num2)
#Subtract two numbers
sub = float(num1) - float(num2)
#Multiply two numbers
mul = float(num1) * float(num2)
#Divide two numbers
div = float(num1) / float(num2)

#Display
print('The addition of {0} and {1} is {2}'.format(num1, num2, sum))
print('The subtraction of {0} and {1} is {2}'.format(num1, num2, sub))
print('The multiplication of {0} and {1} is {2}'.format(num1, num2, mul))
print('The division of {0} and {1} is {2}'.format(num1, num2, div))