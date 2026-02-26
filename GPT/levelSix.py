
# List Literal = [ ]
# Dictonary Literal = { }
# tuple = ( )



def rmSpacees(str):
    newStr = str.replace(" ","")
    return newStr
#rmSpacees("hello world")


def countFrequncyOfChar():
    text = "hello world"
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] =1
    print(frequency)
#countFrequncyOfChar()


def countChar():
    text = input("Enter the text : ")
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] +=1
        else:
            frequency[char] =1
    print(frequency)
countChar()

def checkPalindrome(str):
    if str == str[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")
#checkPalindrome("aba")

def reverseString(str):
    reverse = str[::-1]
    return reverse
#reverseString("programe")

def countVowel(str):
    count=0
    for word in str:
        if word in "aeiouAEIOU":
            count+=1
    print(count)
#countVowel("programming")
        