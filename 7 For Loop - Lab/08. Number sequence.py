#Напишете програма, която чете n на брой цели числа.
# Принтирайте най-голямото и най-малкото число сред въведените.
count = int(input())
numbers = []
for i in range(count):
    number = int(input())
    numbers.append(number)

max_number = max(numbers)
min_number = min(numbers)
print(f"Max number: {max_number}")
print(f"Min number: {min_number}")