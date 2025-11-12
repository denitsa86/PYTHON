#Using a list comprehension, write a program that receives numbers, separated by comma and space
# ", ", and prints all the positive, negative, even, and odd numbers on separate lines
#Note: Zero is counted as a positive number
#1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
numbers = (input().split(", "))
numbers = list(map(int, numbers))
positive_numbers = [n for n in numbers if n >= 0]
negative_numbers = [n for n in numbers if n < 0]
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]
#Positive: 1, 0, 5, 3, 4, 12, 19
#('.'.join(map(str, current_version)))
print("Positive: " + ', '.join(map(str, positive_numbers)))
print("Negative: " + ', '.join(map(str, negative_numbers)))
print("Even: " + ', '.join(map(str, even_numbers)))
print("Odd: " + ', '.join(map(str, odd_numbers)))


