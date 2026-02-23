'''
13️⃣ Find the sum of numbers from 1 to N (user input).
14️⃣ Print multiplication table of a number.
15️⃣ Count the number of digits in a number.
'''
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
    for i in range(1, user_input + 1):
        total += i
    return total

print(findSumOfNumber())

