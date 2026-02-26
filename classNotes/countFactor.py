def printFactorOfNum():
    user_input = int(input("Enter the number : "))
    count = 0
    for i in range (1, user_input):
        if user_input%i ==0:
            count+=1
            print(i, end=" ")
    print(f"\nthere are {count} factors of {user_input}")
#printFactorOfNum()

def countDigit():
    user_input = int(input("Enter the digit : "))
    count = 0
    while user_input>0:
        user_input= user_input//10
        count+=1
    print(f"{count} is count of digit")
#countDigit()

def strongNumber():
    user_input = int(input("Enter the number to check strong number : "))
    sum =1
    while user_input>0:
        digit = user_input%10
        for i in range (1,digit):
            sum = sum + sum*i

            




