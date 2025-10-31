# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
budget = int(input())
season = input()
fishermen_count = int(input())
price = 0
match season:
    case "Spring":
        price += 3000
    case "Summer":
        price += 4200
    case "Autumn":
        price += 4200
    case "Winter":
        price += 2600
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
if fishermen_count <= 6:
    price *= 0.90
elif 7 <= fishermen_count <= 11:
    price *= 0.85
elif fishermen_count > 12:
    price *= 0.75
if season != "Autumn" and fishermen_count % 2 == 0:
    price *= 0.95
if budget >= price:
    print(f"Yes! You have {(budget - price):.2f} leva left.")
elif budget < price:
    print(f"Not enough money! You need {(price - budget):.2f} leva.")



