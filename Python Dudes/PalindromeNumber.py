number = int(input('Enter an Number: '))
temp = number
revno = 0

while number > 0:
    dig = number%10
    revno = revno * 10 + dig
    number = number // 10

if temp == revno:
    print("Number is a pallindrome.")
else:
    print("Number is not pallindrome.")
