budget = float(input())   # Бюджет - реално число;
season = input()   # Един от двата възможни сезона - "summer” или "winter”.
destination = ""   #"Bulgaria", "Balkans" и "Europe"
holiday = ""       #"Camp" и "Hotel"
#Ако е лято ще почива на къмпинг,
# а зимата в хотел.
if budget <= 100:
    destination = "Bulgaria"
    match season:
        case "summer":
            holiday = "Camp"
            budget = budget -(budget * 0.70) #amount * (1 - discount_percent / 100)
        case "winter":
            holiday = "Hotel"
            budget = budget - (budget * 0.30)
elif budget <= 1000:
    destination = "Balkans"
    match season:
        case "summer":
            holiday = "Camp"
            budget = budget - (budget * 0.60)
        case "winter":
            holiday = "Hotel"
            budget = budget - (budget * 0.20)
elif budget > 1000:
#Ако е в Европа, независимо от сезона, ще почива в хотел
    destination = "Europe"
    holiday = "Hotel"
    budget = budget - (budget * 0.10)
print(f"Somewhere in {destination}")
print(f"{holiday} - {budget:.2f}")

