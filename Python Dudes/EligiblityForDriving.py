age = int(input("Enter Your Age: "))
if(age > 7 and age < 150):
    if age > 18:
        print('You are Eligible for Driving!')
    elif age < 18:
        print('You are not Eligible for driving!')
    else:
        print('As your age is 18 your eligiblity is not confirmed. Please come to our office to test your physical and mental status for driving. We will think about you.')
else:
    print('Enter Valid Age!')
