num1 = input('Enter number 1: ')
num2 = input('Enter Number 2: ')
try:
    print('The sum of these two number is: ',
          int(num1) + int(num2))
 except Exception as e:
     print(e)

 print('This is a very important line.')