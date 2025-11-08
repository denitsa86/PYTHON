import math
count = int(input())
fist_sum = 0
second_sum = 0
for i in range(count):
    number = int(input())
    fist_sum += number
for i in range(count):
    number = int(input())
    second_sum += number
if fist_sum == second_sum:
    print(f"Yes, sum = {fist_sum}")
else:
    absolute = int(math.fabs(fist_sum - second_sum))
    print(f"No, diff = {absolute}")
