def countDigitInNumber():
    user_input = int(input("Enter the number : "))
    count=0
    while(user_input>0):
        user_input = user_input//10
        count+=1
    print(count)
print(countDigitInNumber())

