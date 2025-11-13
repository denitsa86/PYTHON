# Диапазон
# < 200
# 200 … 399
# 400 … 599
# 600 … 799
# ≥ 800
#Input: число n (1 ≤ n ≤ 1000) – брой числа
count = int(input())
below_200 = []
between_200_399 = []
between_400_599 = []
between_600_799 = []
above_800 = []
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1,count + 1):
    number = int(input())
    if number < 200:
        below_200.append(number)
    elif number < 400:
        between_200_399.append(number)
    elif number < 600:
        between_400_599.append(number)
    elif number < 800:
        between_600_799.append(number)
    else:
        above_800.append(number)
        #p1 = 12 / count * 100 = 60.00%
p1 = len(below_200) / count * 100
p2 = len(between_200_399) / count * 100
p3 = len(between_400_599) / count * 100
p4 = len(between_600_799) / count * 100
p5 = len(above_800) / count * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")
