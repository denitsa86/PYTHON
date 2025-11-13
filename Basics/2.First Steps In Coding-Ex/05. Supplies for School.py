#опр брой пак с химикали, пакетчета с маркери и препарат за почистване на дъска
#има намаление за нея, което представлява някакъв процент от общата сума.
#Напишете програма, която изчислява колко пари ще трябва да събере Ани, за да плати сметката, като
#•	Пакет химикали - 5.80 лв.
#•	Пакет маркери - 7.20 лв.
#•	Препарат - 1.20 лв (за литър). INPUT:
#•	Брой пакети химикали - цяло число в интервала [0...100]
#•	Брой пакети маркери - цяло число в интервала [0...100]
#•	Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#•	Процент намаление - цяло число в интервала [0...100]
#Output: колко пари ще са нужни на Ани
pen_price = 5.80
marker_price = 7.20
cleaner_price = 1.20
pen_count = int(input())
marker_count = int(input())
cleaner_count = int(input())
discount = int(input())
discount_percent = discount * 0.01
total_cost = pen_count * pen_price + marker_count * marker_price + cleaner_count * cleaner_price
money_needed = total_cost - (total_cost * discount_percent)
print(money_needed)

