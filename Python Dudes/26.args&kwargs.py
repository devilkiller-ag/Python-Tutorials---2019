# def function_name_print(a, b, c, d):
#     print(a, b, c, d)
#
# function_name_print("AG", "PG", "SG", "KG")

''' In function first normal arguments are passed then *args and then **kwargs at last as:
    def fuc(normal_1, normal_2, ... , normal_n, *args_1, *args_2, ... , *args_n, **kwargs_1, **kwargs_2, ... , **kwargs_n):
'''

def funargs(normal, *argsAG, **kwargs):
    print(type(argsAG))
    print(normal)
    for item in argsAG:
        # print(args[0])
        print(item)
    print("\nNow I would like to introduce out hero: ")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

list = ["AG", "PG", "SG", "KG"]
norm = "I am a Normal Argument and the students are: "
kw = {"Rohan":"Monitor", "Mohan":"Sub-Monitor", "Shyam":"Fitness Innstructor", "Sundar":"Attendence Taker"}

funargs(norm, *list, **kw)