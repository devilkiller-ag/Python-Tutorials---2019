mixedlist = ['AG', 646, 767687.989, '!@#$%^&*()()hftftffd43424']
words = ['Ashmit', 'Physics', 'Python', 'Love', 'Chemistry', 'Space', 'Computers', 'Maths']
numbers = [1.6, 5, 7, 89, 87, 878, 7678.8, 45, 35]
print(words)
print(numbers[2])
print(numbers)
'''Some functions in list'''
#print('''Some functions in list''')
#numbers.sort()
#numbers.reverse()
#print(numbers)
'''Slicing of lists'''
print('''Slicing of lists''')
print(numbers[0:8]) # = [:] = [:8] = [0:]
print(numbers[1:7])
'''Advance Slicing: Extended Slicing'''
print('''Advance Slicing: Extended Slicing''')
print(numbers[::-2])
'''Some important functions in string'''
print(numbers.append(7)) #'''iserts element at last'''
numbers.insert(1, 32)#'''inserts element at given index'''
numbers.reverse(7)
numbers.pop()
print(numbers)
numbers[1] = 98