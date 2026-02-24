# find the sum of the first 100 natural numbers using a while loop
def printNumber(num):
    for i in range (1,num+1):
        print(i)
#printNumber(10)

def lastDigitSeven():
    for i in range (7,101):
        if (i%10 == 7):
            print(f"Digit are : {i}")
#lastDigitSeven()

def dividedByTwelveAndFifteen():
    for i in range (12, 1001):
        if (i%12 == 0 and i%15 == 0):
            print(f"Number are : {i}")
#dividedByTwelveAndFifteen()

def printFactorsOfNumber():
    user_input = int(input("Enter the number : "))
    
