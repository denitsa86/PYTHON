# Write a program that receives a sequence of numbers (integers) separated by a single space. It should
# print a sorted list of numbers in ascending order. Use sorted().
# Example
# Input	Output
# 6 2 4	[2, 4, 6]
def sort_numbers(nums):
    all_numbers = []
    for num in nums:
        all_numbers.append(int(num))
    sorted_numbers = sorted(all_numbers)
    return sorted_numbers

numbers = input().split()
print(sort_numbers(numbers))