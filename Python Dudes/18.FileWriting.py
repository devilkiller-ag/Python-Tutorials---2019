# f = open("AG01.txt", "w")
# a = f.write("AG loves Physics. \n ")
# print(a)
# f.close()

# f = open("AG00.txt", "a")
# a = f.write("AG loves Chemistry. \n ")
# print(a)
# f.close()

# Handle read and write both
f = open("AG02.txt", "r+") # r+ : read and write
print(f.read())
f.write("Thanks You!")