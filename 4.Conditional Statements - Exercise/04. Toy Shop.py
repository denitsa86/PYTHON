# Ако поръчаните играчки са 50 или повече-отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина.
# Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# 1.	Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2.	Брой пъзели - цяло число в интервала [0… 1000]
# 3.	Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4.	Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5.	Брой миньони - цяло число в интервала [0 … 1000]
# 6.	Брой камиончета - цяло число в интервала [0 … 1000]
trip = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
puzzle_price = 2.60 # •	Пъзел - 2.60 лв.
doll_price = 3 # •	Говореща кукла - 3 лв.
bear_price = 4.10 # •	Плюшено мече - 4.10 лв.
minion_price = 8.20 # •	Миньон - 8.20 лв.
truck_price = 2 # •	Камионче - 2 лв.
order = puzzles * puzzle_price + dolls * doll_price + bears * bear_price + minions * minion_price + trucks * truck_price
ordered_toys = puzzles + dolls + bears + minions + trucks
if ordered_toys >= 50:
    order = order - (order * 0.25)
final_profit = float(order - (order * 0.10))

if final_profit >= trip:
    print(f"Yes! {final_profit - trip:.2f} lv left.")
else:
    print(f"Not enough money! {trip - final_profit:.2f} lv needed.")
