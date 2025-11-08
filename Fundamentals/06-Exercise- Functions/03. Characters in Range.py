#Write a function that receives two characters and returns a single string with all the characters in
# between them according to the ASCII code.
def return_ascii_in_between(char1, char2):
    ascii_characters = []
    ascii_one = ord(char1)
    ascii_two = ord(char2)
    for i in range(ascii_one + 1, ascii_two):
        ascii_characters.append(chr(i))
    return ascii_characters

character_one = input()
character_two = input()
output = " ".join(return_ascii_in_between(character_one, character_two))
print(output)