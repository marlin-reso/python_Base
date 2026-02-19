def sumOfFirstNNumber(num):
    sum=1
    for i in range (num+1):
        sum = sum+i
    print(f"sum of first {num} is {sum}")

#sumOfFirstNNumber(10)

def userInput():
    number = int(input("Enter the number : "))
    sum = 1
    for i in range (number+1):
        sum= sum+i
    print(f"sum of first {number} numbers is {sum}")    


userInput()




    
   