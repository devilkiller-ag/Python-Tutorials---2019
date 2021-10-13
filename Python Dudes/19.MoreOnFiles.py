f = open("AG02.txt")
# print(f.tell()) # prints where the pointer is
print(f.readline())
# print(f.tell())
f.seek(10) # resets the pointer to the given input(here, 10)
print(f.readline())
# print(f.tell())

f.close()