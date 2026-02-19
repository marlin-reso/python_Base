try:
    number = int(input("Enter a number: "))
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input")    