'''
#Built- in function example
a = 8
b = 9
c = sum((a, b))
print(c)
'''

#User-defined function

def func1(a, b):
    '''This is the function which prints Hello!''' # the string inside''' ''' at the first line inside the function is called docstring
    print('Hello! You are in func1', a+b)
    print(func1.__doc__) #prints docstring of func1 #Professional codes always have docstring
print(func1(5, 7))# also prints 'None' at the end of output
#'None' is outputed because  fuction don't have any return statement
func1(5, 7)# do not prints 'None' at the end of output
def func2(a, b):
    avg = (a + b)/2
    return avg
v = func2(5, 7)
print(v)