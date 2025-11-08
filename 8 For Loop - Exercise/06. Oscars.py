#първоначални точки за актьора. След това всеки оценяващ ще дава своята оценка. Точките,
# които актьора получава се формират от: дължината на името на оценяващия умножено по
# точките, които дава делено на две.
#Ако резултатът в някой момент надхвърли 1250.5 програмата трябва да прекъсне
# На следващите n-на брой реда:
# o	Име на оценяващия - текст
# o	Точки от оценяващия - реално число в интервала [1.0... 50.0]
actor_name = input()
academy_points = float(input())
judges = int(input())
total_points = academy_points

for i in range(judges):
    judge_name = input()
    judge_points = float(input())
    total_points += (len(judge_name) * judge_points) / 2
    if total_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    print(f"Sorry, {actor_name} you need {(1250.5 - total_points):.1f} more!")

