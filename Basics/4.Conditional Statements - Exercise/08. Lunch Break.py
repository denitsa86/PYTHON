#Времето за обяд ще бъде 1/8 от времето за почивка, а времето за отдих ще бъде
# 1/4 от времето за почивка.
# 1.	Име на сериал – текст
# 2.	Продължителност на епизод  – цяло число в диапазона [10… 90]
# 3.	Продължителност на почивката  – цяло число в диапазона [10… 120]
import math
series = input()
episode_time = int(input())
break_time = int(input())
lunch_time = break_time / 8
relax_time = break_time / 4
break_time -= (lunch_time + relax_time)
# •	Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
# •	Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
if break_time >= episode_time:
    print (f"You have enough time to watch {series} and left with {math.ceil(break_time - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {math.ceil(episode_time - break_time)} more minutes.")
