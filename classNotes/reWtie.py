def printFactorOfNum():
    try:
        user_input = int(input("Enter the number : "))
    except ValueError:
        print("Please write a valid number.")
        return
    count = 0
    for i in range(1, user_input):
        if user_input%i == 0:
         count+=1
         print(i,end=" ")
    print(f"\nthere are {count} factors of {user_input}")


while True:
 printFactorOfNum()

 choice = input("Do you want to find another factor (yes/no) : ").lower()
 if choice == "no" or choice == "n" or choice == "exit":
    print("Exit the program")
    break

