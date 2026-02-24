import time
'''
*
**
***
****
*****
'''
for i in range(1, 6):          # controls rows
    for j in range(i):         # prints stars
        print("*", end="")
    print()                    # move to next line






def printinLoadingDots():
    for i in range (1,6):
        print(".", end=" ", flush=True)
        time.sleep(1)

#printinLoadingDots()

