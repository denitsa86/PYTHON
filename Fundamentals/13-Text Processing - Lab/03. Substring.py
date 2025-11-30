#On the first line, you will receive a string. On the second line, you will receive a second string.
# Write a program that removes all the occurrences of the first string in the second until there is
# no match. At the end, print the remaining string.  ice   kicegiciceeb

word = input()
data = input()
while word in data:
    data = data.replace(word, "")
print(data)
