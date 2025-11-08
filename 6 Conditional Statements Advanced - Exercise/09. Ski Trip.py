# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка
# вид помещение	        по-малко от 10 дни	   между 10 и 15 дни	   повече от 15 дни
# room for one person	не ползва 	            не ползва 	            не ползва
# apartment	            30% от крайната цена	35% от крайната цена	50% от крайната цена
# president apartment	10% от крайната цена	15% от крайната цена	20% от крайната цена
#позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.
days = int(input())
room = input()
feedback = input()
nights = days - 1
room_cost = 0
match room:
    case "room for one person":
        room_cost = nights * 18.00
    case "apartment":
        if nights < 10:
            room_cost = (nights * 25.00) * 0.70
        elif  nights <= 15:
            room_cost = (nights * 25.00) * 0.65
        elif nights > 15:
            room_cost = (nights * 25.00) * 0.50
    case "president apartment":
        if nights < 10:
            room_cost = (nights * 35.00) * 0.90
        elif nights <= 15:
            room_cost = (nights * 35.00) * 0.85
        elif nights > 15:
            room_cost = (nights * 35.00) * 0.80
if feedback == "positive":
    room_cost *= 1.25
elif feedback == "negative":
    room_cost *= 0.90
print(f"{room_cost:.2f}")
