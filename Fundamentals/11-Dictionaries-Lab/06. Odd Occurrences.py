#that prints all elements from a given sequence of words that occur an odd number of times
# (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.
#Java C# PHP PHP JAVA C java	java c# c
data = input().split()
odd_occurrences = {}
for word in data:
    word_lower = word.lower()
    if word_lower not in odd_occurrences:
        odd_occurrences[word_lower] = 0
    odd_occurrences[word_lower] += 1

for key, value in odd_occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")
