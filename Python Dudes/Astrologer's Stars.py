# Pattern printing
# Input = Integer no. of rows(n) , Boolean True or False
# eg:-
# @if n = 4, True
# Print:
# *
# **
# ***
# ****
#
# @if n = 4, False
# Print:
# ****
# ***
# **
# *

a = int(input("Please Enter number of rows: "))
b = bool(int(input("Please Enter 0 for False OR 1 for True: ")))

def star(a, b):
    if b == True:
        c = 1
        while c <= a:
            print(c * ' * ')
            c = c + 1
    else:
        while a > 0:
            print(a * " * ")
            a = a- 1

star(a, b)