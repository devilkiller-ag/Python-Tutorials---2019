if __name__ == '__main__':
    number = int(input("Enter an Number: "))
    factorial = 1

    if number < 0:
        print("Error: Factorial of a negative number is not possible!")
    else:
        if number == 0:
            factorial = 1
        else:
            for i in range(1, number + 1):
                factorial = factorial * i
        print("Factorial of ", number, " is ", factorial, ".")
a = input();

