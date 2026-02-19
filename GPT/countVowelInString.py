def countVowelInString():
    vowel = 0
    value = input("Enter the String : ")
    for letter in value:
        if letter in "aeiouAEIOU":
            vowel +=1
    print(vowel)

countVowelInString()
       
               