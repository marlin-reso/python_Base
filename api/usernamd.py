import time


def validateLogin(username, password):
    if username == "admin" and password == "password":
        return True

    return False


while True:
    for username_attempt in range(1, 4):
        username = input("Enter username: ")

        if username == "admin":
            for password_attempt in range(1, 4):
                password = input("Enter password: ")

                result = validateLogin(username, password)

                if result:
                    print("Login successful")
                    break
                else:
                    remaining_attempts = 3 - password_attempt
                    print("Password is wrong")
                    print(f"Remaining password attempts: {remaining_attempts}")

            else:
                print("You entered wrong password 3 times. Please try again later.")
                print("Please wait for 30 seconds before trying again.")
                time.sleep(30)
                break

            
        else:
            print("Username is wrong")

            if username_attempt == 2:
                print("Hint: username starts with 'a' and has 5 letters.")
    else:
        print("You entered wrong username 3 times. Please try again later.")
        print("Please wait for 30 seconds before trying again.")
        time.sleep(30)
        continue
    if result:
        break