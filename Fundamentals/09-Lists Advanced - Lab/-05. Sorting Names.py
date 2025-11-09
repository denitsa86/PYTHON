#Write a program that reads a single string with names separated by comma and space ", ".
# Sort the names by their length in descending order. If 2 or more names have the same length,
# sort them in ascending order (alphabetically). Print the resulting list.
# Read input string
names_input = input()

# Split the string into a list of names
names = names_input.split(", ")

# Sort by length (descending) and then alphabetically (ascending)
sorted_names = sorted(names, key=lambda name: (-len(name), name))

# Print the result
print(sorted_names)