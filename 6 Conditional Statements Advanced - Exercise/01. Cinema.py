#кинозала столовете са наредени в правоъгълна форма в r реда и c колони
# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
#Input: тип прожекция (текст), брой редове и брой колони в залата (цели числа
#общите приходи от билети при пълна зала формат 2 знака след десетичната точка.
projection = input()
rows = int(input())
columns = int(input())
capacity = rows * columns
profit = 0
if projection == "Premiere":
    profit = capacity * 12.00
elif projection == "Normal":
    profit = capacity * 7.50
else:
    profit = capacity * 5.00
print(f"{profit:.2f} leva")