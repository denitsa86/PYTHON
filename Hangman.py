secret_word= input("Enter your secret word: ").lower()
guessed_letters =[]
incorrect_guesses = []
valid_characters = list("abcdefghijklmnopqrstuvwxyz")
tries = len(secret_word)*2
empty_word = "_"*len(secret_word)
updated_word=empty_word
print(f"The word has {len(secret_word)} letters")
print(updated_word)
#Player suggests a letter if not out of tries or word is not guessed
while tries > 0 and "_" in updated_word:
    guess = input("Suggest a letter: ").lower()
    # check if input is valid
    if guess not in valid_characters:
        print("Not a valid character, please try again.")
        continue
    #check if letter is already used
    if guess in guessed_letters or guess in incorrect_guesses:
        print("You've already used that letter.")
        continue
    #if letter is correct
    if guess in secret_word:
        guessed_letters.append(guess)
        new_word = ""
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                new_word += guess
            else:
                new_word += updated_word[i]
        updated_word = new_word
        print("That's right!")
    else:
        #letter is not correct
        incorrect_guesses.append(guess)
        tries -= 1
        print("The letter wasn't found. Try again.")

    print(f"Word: {updated_word}")
    print(f"Tries left: {tries}")
#Output: letter is guessed or player lost
if "_" not in updated_word:
    print("You won!")
    print(f"The word is {updated_word}")
else:
    print("Game over! Good luck next time :)")



