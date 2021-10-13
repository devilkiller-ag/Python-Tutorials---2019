def fibo_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
number = int(input("Enter an Number: "))
print("Fibonacci of ", number, 'is', fibo_recursive(number))
