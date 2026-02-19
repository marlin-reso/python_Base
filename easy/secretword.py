secret_word = "girrafe"
guess = ""
guess_count = 0
guess_limit = 3
is_out_of_guesses = False
while guess != secret_word and not is_out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        is_out_of_guesses = True
if is_out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")

    