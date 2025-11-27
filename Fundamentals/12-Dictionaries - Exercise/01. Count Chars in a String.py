# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"
data = input()
if " " in data:
    data = data.replace(" ", "")
chars = list(data)

occurrences = {}

for char in chars:
    if char not in occurrences:
        occurrences[char] = 0
    occurrences[char] += 1

for key, value in occurrences.items():
        print(f"{key} -> {value}")
