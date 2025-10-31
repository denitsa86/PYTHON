# •	Видеокарта – 250 лв./бр.
# •	Процесор – 35% от цената на закупените видеокарти/бр.
# •	Рам памет – 10% от цената на закупените видеокарти/бр
#Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от
# крайната сметка.
budget = float(input(""))
video_count = int(input(""))
processors_count = int(input(""))
ram_count = int(input(""))
video_price = 250
total_video_price = video_price * video_count
processor_price = total_video_price * 0.35
ram_price = total_video_price * 0.10
expenses = total_video_price + processors_count * processor_price + ram_count * ram_price
if video_count > processors_count:
    expenses = expenses - (expenses * 0.15)
if budget >= expenses:
    print(f"You have {budget - expenses:.2f} leva left!")
else:
    print(f"Not enough money! You need {expenses - budget:.2f} leva more!")

