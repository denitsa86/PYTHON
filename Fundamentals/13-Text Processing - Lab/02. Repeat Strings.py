#Write a program that reads a sequence of strings, separated by a single space. Each string should be
# repeated N times, where N is the length of the string. Print the final strings concatenated into
# one string. # hi abc add	hihiabcabcabcaddaddadd

data = input().split()
concatenated_word = ""
for word in data:
    concatenated_word += word * len(word)
print(concatenated_word)
