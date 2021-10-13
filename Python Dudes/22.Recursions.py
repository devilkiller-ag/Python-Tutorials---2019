# Recursions - means using function inside an function
def factorial_iterative(n):
    '''

        :param n: integer
        :return:  n * n-1 * n-2 * n-3 .... 1
    '''
    #n! = n * n-1 * n-2 * n-3 .... 1
    #n! = n * (n-1)!

    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return  fac

def factorial_recurssive(n):
    '''

        :param n: integer
        :return:  n * n-1 * n-2 * n-3 .... 1
    '''
    #n! = n * n-1 * n-2 * n-3 .... 1
    #n! = n * (n-1)!

    if n == 1:
        return 1
    else:
        return n * factorial_recurssive(n-1)
    '''
    Input: 5
    Mechanism:  
    5 * factorial_recurssive(4)
    5 * 4 * factorial_recurssive(3)
    5 * 4 * 3 * factorial_recurssive(2)
    5 * 4 * 3 * 2 * factorial_recurssive(1)
    5 * 4 * 3 * 2 * 1 = 120
    '''


number = int(input("Enter the number: "))

print("Factorial Using Iterative Method: ", factorial_iterative(number))
print("Factorial Using Recurssive Method: ", factorial_recurssive(number))