from time import time

initial = time()

def func1(a, b):
    #By Me
    return a + b;

def func2(a, b):
    #By You
    num1 = a;
    num2 = b;
    if a<b and b>2:
        pass
    return a+b;

if __name__ == '__main__':

    init = time()
    for i in range(1, 100000):
        func1(1, 2)
    print("Time taken by Me: ", time()-init)

    init = time()
    for i in range(1, 100000):
        func2(1, 2)
    print("Time taken by You: ", time() - init)

print("Overall time of program: ", time()-initial)