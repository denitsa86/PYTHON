#Using comprehension, write a program that receives a text and removes all its vowels,
# case insensitive. Print the new text string after removing the vowels. The vowels that should
# be considered are  'a', 'o', 'u', 'e', 'i'.

text = input()
vowels = ['a', 'e', 'i', 'o', 'u']
non_vowel = [letter for letter in text if letter.lower() not in vowels]
print("".join(non_vowel))