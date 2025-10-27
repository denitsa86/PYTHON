#Напишете програма, която изчислява необходимате сума, които
# Божидара ще трябва да заплати
#Цената на един кв. м. е 7.61 лв със ДДС. Понеже нейният двор е доста голям,
# фирмата изпълнител предлага 18% отстъпка от крайната цена.
#Input:Кв. метри, които ще бъдат озеленени – реално число в интервала [0.00 … 10000.00]
#•	"The final price is: {крайна цена на услугата} lv."
#•	"The discount is: {отстъпка} lv."
square_meters = float(input())
full_price = square_meters * 7.61
discount = full_price * 0.18
total_price = full_price - discount
print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")