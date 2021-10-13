'''
i = 0
while True:
    if i+1 < 5:
        i = i + 1
        continue #skip the below statement and return to while statement
    print(i + 1, end=' ')
    if(i == 44):
        i = i + 1
        break # Stop the loop
    i = i + 1
'''
while True:
    inputno = int(input('Enter an Number:\n '))
    if inputno > 100:
        print('Congratulations! You have Entered an number greater than 100')
        break
    else:
        print('Try Again!\n')
        continue
