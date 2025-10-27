#която изчислява разходите за ремонта, предвид следните цени:
#•	Предпазен найлон - 1.50 лв. за кв. метър
#•	Боя - 14.50 лв. за литър
#•	Разредител за боя - 5.00 лв. за литър
#1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]
#2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]
#3.	Количество разредител (в литри) - цяло число в интервала [1…30]
#4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]
# още 10% от количеството боя и 2 кв.м. найлон и 0.40 лв. за торбички.
# Сумата, която се заплаща на майсторите за 1 час е равна на 30% от сбора
# на всички разходи за материали.
nylon_price = 1.50
paint_price = 14.50
diluent_price = 5.00
nylon_needed = int(input()) #10
paint_needed = int(input()) #11
diluent_needed = int(input()) #4
hours_to_finish = int(input())#8
nylon_addition = 2
paint_addition = paint_needed * (10*0.01)
bags_price = 0.40
total_nylon = (nylon_needed + nylon_addition)* nylon_price
total_paint = (paint_needed + paint_addition)* paint_price
diluent_total = diluent_needed * diluent_price
cost_total = total_nylon + total_paint + diluent_total + bags_price
work_price_per_hour = (30 / 100) * cost_total
total_work_price = work_price_per_hour * hours_to_finish
#Output: •	"{сумата на всички разходи}"
print(f"{total_work_price + cost_total}")
