# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и
# проверява дали сред тях съществува число, което е равно на сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между
# най-големия елемент и сумата на останалите (по абсолютна стойност)
import sys
import math

max_num = -sys.maxsize
sum_numbers = 0
count = int(input())

for i in range(0,count):
    number = int(input())
    if max_num < number:
        max_num = number
    sum_numbers += number
if max_num == sum_numbers - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {int(math.fabs(max_num - (sum_numbers-max_num)))}")

