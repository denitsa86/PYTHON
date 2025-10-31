import math
# 1.	Рекордът в секунди – реално число;
# 2.	Разстоянието в метри – реално число;
# 3.	Времето в секунди, за което плува разстояние от 1 м. - реално число
world_record = float(input())
distance = float(input())
time_per_meter = float(input())
#съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди.
#резултатът трябва да се закръгли надолу до най-близкото цяло число.
#Да се изчисли времето в сек и разликата спрямо Световния рекорд.
time = distance * time_per_meter
additional_time = math.floor((distance / 15) *12.5)
total_time = time + additional_time
if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")

