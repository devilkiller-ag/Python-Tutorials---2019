#Anonymous/Lamda Functions - One Liner Function
#
# def add(a, b):
#     return a + b
#
# minus = lambda x, y: x - y # Lamda Function
#
# print(minus(9, 4))

def a_first():
    return a(1)

a = [[1, 4], [5, 4], [6, 22]]
a.sort(key = a_first)
print(a)
