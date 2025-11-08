#Write a program that receives a sequence of numbers (integers) separated by a single space. It should
# print a list of only the even numbers. Use filter().
def is_even(num):
    return int(num) % 2 == 0

numbers = input().split()
filtered = filter(is_even, numbers)
even_numbers = []
for n in filtered:
    even_numbers.append(int(n))
print(even_numbers)