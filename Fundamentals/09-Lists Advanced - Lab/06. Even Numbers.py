#Write a program that reads a single string with numbers separated by comma and space ", ".
# Print the indices of all even numbers
numbers = list(map(lambda x: int(x), input().split(", ")))
indices = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        indices.append(i)
print(indices)
