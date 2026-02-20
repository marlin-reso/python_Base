
#Check whether a number is even or odd.
def checkEvenOrOdd(num):
    if num%2 ==0:
        print(f"{num} is even")
    else :
        print (f"{num} is odd")
#checkEvenOrOdd()

def checkNumIsPositiveNegativeOrZero():
    user_input = int(input("Enter the number : "))
    if user_input>0:
        return print(f"{user_input} is positive number")
    elif user_input == 0:
        return print(f"{user_input} is Zero")
    else:
        return print(f"{user_input} is negative number")
    
#checkNumIsPositiveNegativeOrZero()

def findLargestBetweenThree(num1, num2, num3):
    if num1 > num2 and num1>num3:
        return num1
    elif num2>num3 and num2>num1:
        return num2
    else:
        return num3
#print(findLargestBetweenThree(10,20,43))

def checkWeatherIsLeap():
    year = int(input("Enter the Year : "))
    if (year%4 == 0 and year%100 !=0) or (year%400==0):
         print(f"{year} is a leap year")
    else:
       print(f"{year} is not a leap year")
#print(checkWeatherIsLeap())

def checkElegibilityToVote():
    user_age_year = int(input("Enter the year count : "))
    user_age_month = int(input("Enter the month count : "))

    if user_age_year>=18 and user_age_year <100 :
        print(f"Person is able to cast its vote and his age is {user_age_year} year and {user_age_month} month")
    else:
        print(f"Person is not able to cast his vote. His age is {user_age_year} year and {user_age_month} month")

checkElegibilityToVote()





