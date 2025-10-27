#Create a program that prints on a new line the next n odd numbers (starting from 1).
# On the last row prints the sum of all n odd numbers
#A single number n is read from the console, indicating how many odd numbers need to be printed.
#Print the next n odd numbers, starting from 1, separated by newlines. On the last line,
# print the sum of these numbers.
#•	n will be in the interval [1…100]
number = int(input("Enter a number: "))
count = 0
current = 1
total = 0

while count < number:
    print(current)
    total += current
    current += 2
    count += 1

print(f"Sum: {total}")

