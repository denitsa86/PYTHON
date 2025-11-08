# Write a program that receives a sequence of numbers (integers) separated by a single space. It should
# print the min and max values of the given numbers and the sum of all the numbers in the list.
# Use min(), max() and sum().
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is: {sum of all numbers}"
import sys
def min(nums):
    min_number = sys.maxsize
    for num in nums:
        if int(num) < min_number:
            min_number = int(num)
    print(f"The minimum number is {min_number}")
def max(nums):
    max_number = -sys.maxsize
    for num in nums:
        if int(num) > max_number:
            max_number = int(num)
    print(f"The maximum number is {max_number}")
def sum(nums):
    sum_numbers = 0
    for num in nums:
        sum_numbers += int(num)
    print(f"The sum number is: {sum_numbers}")

numbers = input().split()
min(numbers)
max(numbers)
sum(numbers)