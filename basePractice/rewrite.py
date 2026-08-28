
def find_even_and_odd():
    try:
        user_input = int(input("Enter the number : "))
    except ValueError:
        print("Please write a valid number.")
        return

    if user_input%2 == 0:
        print(f"{user_input} is even number ")
    else:
        print(f"{user_input} is odd number ")



while True:
    find_even_and_odd()

    choice = input("Do you want to continue ? (yes/no): ").lower()

    if choice == "no" or choice == "n" or choice == "exit":
        print("exit")
        break


