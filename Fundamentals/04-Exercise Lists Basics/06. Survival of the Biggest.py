# 10 9 8 7 6 5
# 3
import sys
min_num = sys.maxsize
numbers = input().split()
to_be_removed = int(input())
for n in range(to_be_removed):
    for n in range(len(numbers)):
        if int(numbers[n]) < min_num:
            min_num = int(numbers[n])
    numbers.remove(str(min_num))
    min_num = sys.maxsize
print(', '.join(numbers))

