f = open("ag.txt", "rt")
print(f.readlines())
# content = f.read()

print(f.readline())
print(f.readline()) #new line is by default printed because it is in file
for line in f:
    print(line, end="")

# print(content)
# content = f.read(4)
# print("1: ", content)
#
# content = f.read(343)
# print("2: ", content)

f.close()