# write a function that counts how many uppercase
# and lowercase characters are in a string
def find_upper_or_lower_characters(word):
    upper_characters = []
    lower_characters = []
    for char in word:
        if char.isupper():
            upper_characters.append(char)
        else:
            lower_characters.append(char)
    return f"Upper characters: {len(upper_characters)}, Lower characters: {len(lower_characters)}"

start_word = input("Enter a word: ")
print(find_upper_or_lower_characters(start_word))
