#определен брой турнири, като за всеки турнир получава точки, които зависят от
# позицията, на която е завършил в турнира
# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
#колко ще са точките след изиграване на всички турнири, като знаете с колко точки стартира
#изчислете колко точки средно печели от всички изиграни турнири и колко процента от
# турнирите е спечелил.
import math
tournament_count = int(input())
start_points = int(input())
total_points = 0
wins = 0
#За всеки турнир се прочита отделен ред: Достигнат етап–текст– "W", "F" или "SF"
for i in range(tournament_count):
    position = input()
    if position == 'W':
        total_points += 2000
        wins += 1
    elif position == "F":
        total_points += 1200
    elif position == "SF":
        total_points += 720

average_points = total_points / tournament_count
final_points = total_points + start_points
won_percentage = wins / tournament_count * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{won_percentage:.2f}%")