# N години. За всеки свой рожден ден тя получава подарък.
# •	За нечетните рождени дни (1, 3, 5...n) получава играчки.
# •	За четните рождени дни (2, 4, 6...n) получава пари.
#втория рожден ден получава 10.00 лв, като сумата се увеличава с 10.00 лв.,
# за всеки следващ четен
#Братът на Лили, в годините, които тя получава пари, взима по 1.00 лев
#Лили продала играчките получени през годините, всяка за P лева и добавила сумата
#иска да си купи пералня за X лева.
#колко пари е събрала и дали ѝ стигат да си купи пералня?
age = int(input())                    # Възрастта на Лили - цяло число в интервала [1...77]
price_washing_machine = float(input()) # •Цената на пералнята - число в интервала [1.00...10 000.00]
price_per_toy = int(input())
sum_money = 10
toy_count = 0
birthday_money = 10
saved_money = 0

for year in range(1,age + 1):
    if year % 2 ==0:
        saved_money += birthday_money
        birthday_money += 10
        saved_money -= 1
    else:
        toy_count += 1
saved_money += toy_count * price_per_toy
# •	Ако парите на Лили са достатъчни:
# o	"Yes! {N}" - където N е остатъка пари след покупката
# •	Ако парите не са достатъчни:
# o	"No! {М}" - където M е сумата, която не достига
if saved_money >= price_washing_machine:
    print(f"Yes! {(saved_money - price_washing_machine):.2f}")
else:
    print(f"No! {(price_washing_machine-saved_money):.2f}")


