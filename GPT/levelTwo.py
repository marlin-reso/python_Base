
def printNum():
    user_input = int(input("Enter the number : "))
    for i in range (1,user_input+1) :
        print(i)
#printNum()

def printAllEven():
    user_input = int(input("Enter the number : "))
    for i in range(1, user_input+1):
        if i%2==0:
            print(i)
#printAllEven()

def findSumOfNumber():
    user_input = int(input("Enter the number : "))
    total = 0
    for i in range (1,user_input+1):
         total += i
         return total

#print(findSumOfNumber())

def printTable():
    user_input = int(input("Enter the number : "))
    for i in range (1, 11):
        print(i)
       
       # print(f"{user_input} X {i} = {user_input*i}")

#print(printTable())


