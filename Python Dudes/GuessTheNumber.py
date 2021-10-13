# without using random module
#
# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n = 18
number_of_guesses = 1
print("Number of guesses is limited to only 9 times: ")
while (number_of_guesses <= 9):
    guess_number = int(input("Guess the number :\n"))
    if guess_number < 18:
        print("You have entered smaller number. please input greater number.\n")
    elif guess_number > 18:
        print("You have entered larger number. please input smaller number.\n")
    else:
        print("You Won!\n")
        print("Number of guesses You took to Finish: ", number_of_guesses)
        break
    print("Number of Guesses left: ", 9 - number_of_guesses)
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses > 9):
    print("Game Over!\n")
