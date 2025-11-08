#Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
# Use round().
# 1.0 2.5 3.0 4.5	[1, 2, 3, 4]

def round_numbers(nums):
    rounded_numbers = []
    for num in nums:
        rounded = round(float(num))
        rounded_numbers.append(rounded)
    print(rounded_numbers)

numbers = input().split()
round_numbers(numbers)