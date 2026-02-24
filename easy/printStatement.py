def printTable():
    user_input = int(input("Enter the number : "))
    for i in range(1 , 11):
        print(f"{user_input} X {i} = {i*user_input}")


#printTable()

def findFectorial():
    user_input = int(input("Enter the number : "))
    sum = 1
    if (user_input<=0):
        print(f"{user_input} is not a valid number ")
        return user_input
    for i in range (1, user_input+1):
        sum = sum*i
        i +=1
    print(f"{user_input}! = {sum}")
#findFectorial()

def reverseNumber():
    user_input = int(input("Enter the number : "))
    reverse = 0
    while user_input > 0:
        reminder = user_input % 10
        reverse = (reverse * 10) + reminder
        user_input = user_input // 10
    print(f"Reverse of the number is {reverse}")

#reverseNumber()

def reverseString():
    user_input = input("Enter the string : ")
    reverse = user_input[::-1]
    print(f"Reverse of the string is {reverse}")
reverseString()
   

        