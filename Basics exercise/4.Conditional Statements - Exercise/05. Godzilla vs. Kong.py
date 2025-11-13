#дали предвидените средства са достатъчни
#определен брой статисти, облекло за всеки един статист и декор
#•	Декорът за филма е на стойност 10% от бюджета.
#•	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.
# Ред 1.Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
budget = float(input())
statist_count = int(input())
single_clothing_price = float(input())
decor = budget * 0.10
clothing_price = statist_count * single_clothing_price
if statist_count > 150:
    clothing_price = clothing_price - (clothing_price * 0.10)
expenses = clothing_price + decor
if expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {expenses - budget:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {budget - expenses:.2f} leva left.")


