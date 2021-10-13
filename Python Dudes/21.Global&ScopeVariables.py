# l = 10 # Global Variable: Can be accessed by any function in the program
# def fuction1(n):
#     # l = 5 # Local Variable
#     m = 8 #local
#     # l = l + 5 #error
#     global l # allows function to change the global variable 'l'
#     l = l + 5
#     print(l, m)
#     print("I have Printed: ", n)
#
# fuction1("This is me!")
# print(l)

def ag():
    x = 26
    def kg(): #nested function
        global x
        '''searches x outside all functions(and not inside any functions) since there is no global variable x
        outside so it creates an global variable x and assigns its value as 88'''
        x = 88
    print("before calling function kg(): ", x)#prints local variable x of ag()
    kg()
    print("after calling function kg(): ", x)#prints local variable x of ag()
ag()
print(x) # prints the value of global variable x as created by line 17