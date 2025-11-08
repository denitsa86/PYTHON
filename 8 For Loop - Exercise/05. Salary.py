# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [500...1500]
# След това n – на брой пъти се чете име на уебсайт – текст
open_tabs = int(input())
salary = int(input())
final_salary = 0

for tab in range(open_tabs):
    site = input()
    if salary <= 0: break
    match site:
        case "Facebook":
            salary -= 150
        case "Instagram":
            salary -= 100
        case "Reddit":
            salary -= 50
        case _:
            salary = salary
if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))