#print the number between 10 to 20
def printNum():
    for i in range (10, 21):
        print(i)

#printNum()

def findSumOfNaturalNumber():
    sum = 0
    for i in range(1, 20):
        sum = sum + i
    return sum
#print(findSumOfNaturalNumber())

def findEvenAndOdd():
    user_input = int(input("Enter the number : "))
    if user_input%2==0:
        print(f"{user_input} is even number")
    else:
        print(f"{user_input} is odd number")

#findEvenAndOdd()

def findPrimeNumber():
    user_input = int(input("Enter the number : "))

    if user_input <= 1:
        print("Not prime number")
        return

    for i in range(2, user_input):
        if user_input % i == 0:
            print(f"{user_input} is not prime number")
            return   # stop immediately

    print(f"{user_input} is prime number")

                

findPrimeNumber()

        
    
