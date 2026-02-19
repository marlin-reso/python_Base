def calculator():
    num1 = float(input("Enter first Number : "))
    op = input("Enter operator : ")
    num2 = float(input("Enter second Number : "))
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/":
        return num1/num2
    else:    
        print("Invalid operator")

print(calculator())       
