#спрямо времето от денонощието и градусите да препоръча дрехи
#има различни планове за всеки етап от деня, които изискват и различен външен вид
# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
#Като изход : "It's {градуси} degrees, get your {облекло} and {обувки}."
degrees = int(input())
daytime = input() #"Morning", "Afternoon" или "Evening"
outfit = ""
shoes = ""
if 10 <= degrees <= 18:
    match daytime:
        case "Morning":
            outfit = "Sweatshirt"
            shoes = "Sneakers"
        case "Afternoon":
            outfit = "Shirt"
            shoes = "Moccasins"
        case "Evening":
            outfit = "Shirt"
            shoes = "Moccasins"
elif 18 < degrees <= 24:
    match daytime:
        case "Morning":
            outfit = "Shirt"
            shoes = "Moccasins"
        case "Afternoon":
            outfit = "T-Shirt"
            shoes = "Sandals"
        case "Evening":
            outfit = "Shirt"
            shoes = "Moccasins"
else:
    match daytime:
        case "Morning":
            outfit = "T-Shirt"
            shoes = "Sandals"
        case "Afternoon":
            outfit = "Swim Suit"
            shoes = "Barefoot"
        case "Evening":
            outfit = "Shirt"
            shoes = "Moccasins"
print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")