import math

me = "Ashmit"
no = 1

# Old method of inserting string in btw another string:

#Method 1
# a1 = "This is %s"%me
# a2 = "The number is %s"%no
# a3 = "This is %s %s"%(me, no)
# print(a1, a2, a3)

#Method 2
# a = "This is (1) (0)"
# b = a.format(me, no)
# print(b)

# ab = "This is () ()"
# ba = ab.format(me, no)
# print(ba)

# F-strings(Fast string)
af = f"This is {me} {no} {math.cos(65)} {6*3+76}"
print(af)