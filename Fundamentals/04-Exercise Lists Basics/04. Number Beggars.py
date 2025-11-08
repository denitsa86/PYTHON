# 1, 2, 3, 4, 5
# 3
# 100, 94, 24, 99
# 5
numbers = input().split(", ")
beggars = int(input())
sum_beggars = []
start_index = 0

for beg in range(beggars):
    current_sum = 0
    for num in range(start_index, len(numbers), beggars):
        current_sum += int(numbers[num])
    sum_beggars.append(current_sum)
    start_index += 1
print(sum_beggars)





