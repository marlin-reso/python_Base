is_male = True
is_tall = False
if not(is_tall):
    print("You are tall")
else:
    print("You are not tall")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

value = max_num(13,45,19)
print(value)    