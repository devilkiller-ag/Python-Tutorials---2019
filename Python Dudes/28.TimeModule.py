import time

print('AG From for loop: \n')
init1 = time.time(); #returns ticks; 1 tick = 1 second
for i in range(45):
    print("This is AG.")
print(f"\nTime taken by for loop  is {(time.time()-init1)/45} seconds.")

print('\nAG From while loop: \n')
init2 = time.time();
k = 0
while k < 45:
    print("This is AG.")
    time.sleep(1)#pauses program for few limited seconds written inside ()
    k += 1;
print(f"\nTime taken by for loop is {(time.time()-init2)/45} seconds.")

localtime = time.asctime(time.localtime(time.time()))
print((localtime))
