#Тя спестява или харчи част от парите си всеки ден. Ако иска да похарчи повече от наличните си пари, то
# тя ще похарчи колкото има и ще ѝ останат 0 лева.
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.
# •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o	"You can't save the money."
# o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# o	"You saved the money for {общ брой изминали дни} days."
needed_money = float(input())
current_money = float(input())
days_counter = 0
spending_counter = 0
while spending_counter < 5 and current_money < needed_money:
    action = input()
    amount = float(input())
    days_counter += 1
    match action:
        case "spend":
            current_money -= amount
            spending_counter += 1
            if current_money <= 0:
                current_money = 0
        case "save":
            current_money += amount
            spending_counter = 0
if spending_counter >= 5:
    print("You can't save the money.")
    print(f"{days_counter}")
else:
    print(f"You saved the money for {days_counter} days.")



