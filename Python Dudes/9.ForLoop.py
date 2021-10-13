'''
list = [['Ashmit', 1], ['Little', 2], ['India', 3], ['Asia', 4]]
dict1 = dict(list)
for item in dict1: # prints keys of ditionary
    print(item)
for item, number in dict1.items():# prints items and keys of dictionary
    print(item, 'is ', number)
'''
list1 = ['ashmit', 1, 5, 'ag', 7, 1.2, 8, 3, 'joker']
for item in list1:
    if type(item) == int or type(item) == float and item < 6: #if str(item).isnumeric() and item < 6:
        print(item)
