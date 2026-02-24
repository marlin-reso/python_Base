
def findSumOfDigits(num):
    sum =0
    while num>0:
        digit = num%10
        sum = sum+digit
        num = num//10
    return sum
value = findSumOfDigits(1234678)
print(value)
   

def reverseNum(num):
    reverse=0
    while num>0:
        digit = num%10
        reverse = reverse*10 + digit
        num = num//10
    return reverse

def checkPalindromeNumber():
    user_input = int(input("Enter the number : "))
    num = reverseNum(user_input)
    if num == user_input:
        print(f"{user_input} is palindrome number")
    else:
        print("Not a palindrome")

#checkPalindromeNumber()
   

def reverseNumber():
    user_input = int(input("Enter number : "))
    reverse=0
    while (user_input>0):
        digit = user_input%10
        reverse = reverse*10 + digit
        user_input = user_input//10
    return reverse
#reverseNumber()

def findFectorial():
    user_input = int(input("Enter the number : "))
    factorial = 1
    for i in range (1, user_input+1):
        factorial= factorial*i
    print(factorial)
#findFectorial()

def checkPrimeNumber():
    user_input = int(input("Enter the number : "))
    count = 0
    if user_input<1:
        return print("Enter positive num")
    for i in range (2,user_input+1):
        if user_input%i ==0:
            count += 1
            if count == 1:
                print(f"{user_input} is a prime number")
            else:
                print(f"{user_input} is not a prime number")
                break

#checkPrimeNumber()
            