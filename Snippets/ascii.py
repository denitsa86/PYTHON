# The ord() function returns the number representing the unicode code of a specified character.
def return_ascii_in_between(char1, char2):
    ascii_characters = []
    ascii_one = ord(char1)  #
    ascii_two = ord(char2)
    for i in range(ascii_one + 1, ascii_two):
        ascii_characters.append(chr(i))
    return ascii_characters


# The chr() function returns the character that represents the specified unicode.
x = chr(97)
print(x)  # a
