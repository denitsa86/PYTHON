# да изчисли колко  ще им струва, за да засадят определен брой цветя и дали
# наличният бюджет ще им е достатъчен. Различните цветя са с различни цени:
# цвете	               Роза	Далия	Лале	Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	     2.50
# отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# •	Вид цветя -възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
flower = input()
count_flowers = int(input())
budget = int(input())
price = 0
if flower == "Roses":
    price = count_flowers * 5
    if count_flowers > 80:
        price *= 0.90
elif flower == "Dahlias":
    price = count_flowers * 3.80
    if count_flowers > 90:
        price *= 0.85
elif flower == "Tulips":
    price = count_flowers * 2.80
    if count_flowers > 80:
        price *= 0.85
elif flower == "Narcissus":
    price = count_flowers * 3
    if count_flowers < 120:
        price *= 1.15
elif flower == "Gladiolus":
    price = count_flowers * 2.50
    if count_flowers < 80:
        price *= 1.20
if budget >= price:
    print(f"Hey, you have a great garden with {count_flowers} {flower} and {(budget - price):.2f} leva left.")
else:
    print(f"Not enough money, you need {(price - budget):.2f} leva more.")




