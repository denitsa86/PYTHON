#Трима спортни състезатели финишират за някакъв брой секунди (между 1 и 50).
# Да се напише програма, която чете времената на състезателите в секунди,
# въведени от потребителя и пресмята сумарното им време във формат
# "минути:секунди". Секундите да се изведат с водеща нула
# (2  "02", 7  "07", 35  "35").
import math
first_player = int(input())
second_player = int(input())
third_player = int(input())
sum_seconds = first_player + second_player + third_player
minutes = math.floor(sum_seconds // 60)
seconds = sum_seconds % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")