#•	Пилешко меню –  10.35 лв.
#•	Меню с риба – 12.40 лв.
#•	Вегетарианско меню  – 8.15 лв.
#колко ще струва на група хора да си поръчат храна за вкъщи?
#+ десерт, чиято цена е равна на 20% от общата сметка (без доставката).
#Цената на доставка е 2.50 лв и се начислява най-накрая. INPUT:
#•	Брой пилешки менюта – цяло число в интервала [0 … 99]
#•	Брой менюта с риба – цяло число в интервала [0 … 99]
#•	Брой вегетариански менюта – цяло число в интервала [0 … 99]
#OUTPUT:Да се отпечата на конзолата един ред:  "{цена на поръчката}"
chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15
dessert_percentage = 20
delivery = 2.50
chicken_count = int(input())
fish_count = int(input())
veggie_count = int(input())
chicken_total = chicken_count * chicken_price
fish_total = fish_count * fish_price
veggie_total = veggie_count * veggie_price
menu_cost = chicken_total + fish_total + veggie_total
dessert_price = (dessert_percentage / 100) * menu_cost
total_cost = float(menu_cost + dessert_price + delivery)
print(f"{total_cost:.2f}")
