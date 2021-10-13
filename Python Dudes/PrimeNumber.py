var = int(input('Enter Number to be checked: '))
count = 0
for i in range(1, var):
    if (var % i == 0):
        count += 1
if count == 1:
    print('Prime Number: ', var)
else:
    print('Not a prime Number: ', var)
