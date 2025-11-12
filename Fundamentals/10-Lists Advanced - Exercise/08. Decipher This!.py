# You are given a secret message you should decipher. To do that, you need to know that in each word:
# •	the second and the last letter are switched (e.g., Holle means Hello)
# •	the first letter is replaced by its character code (e.g., 72 means H)
massage = input().split()
manipulated_massage = []
for number in massage:
    digit_part = []
    letter_part = []
    for i in range(0, len(number)):
        if number[i].isdigit():
            digit_part.append(number[i])
        else:
            letter_part.append(number[i])
    digit_part = ''.join(digit_part)
    ascii_part = chr(int(digit_part))   #olle
    letter_part[0], letter_part[len(letter_part)- 1] = letter_part[len(letter_part)- 1], letter_part[0]
    converted_word = str(ascii_part) + "".join(letter_part)
    manipulated_massage.append(converted_word)
print(" ".join(manipulated_massage))


