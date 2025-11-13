# Град	0 ≤ s ≤ 500 	500 < s ≤ 1 000 	1 000 < s ≤ 10 000	 s > 10 000
# Sofia	  5%	            7%	                8%	                12%
# Varna	  4.5%	            7.5%	           10%	                13%
# Plovdiv	5.5%	       8%	                12%                	14.5%
#Input: име на град (текст) и обем на продажби (реално число),
#размера на търговската комисионна според горната таблица. Резултатът да се изведе
# форматиран до 2 цифри след десетичната точка. При невалиден град или обем на продажбите
# (отрицателно число) да се отпечата "error".
city = input()
sales = float(input())
commission = 0
isError = False
if 0 <= sales <= 500:
    match city:
        case "Sofia":
          commission = sales * 0.05
        case "Varna":
          commission = sales * 0.045
        case "Plovdiv":
          commission = sales * 0.055
        case _:
            isError = True
elif 500 < sales <= 1000:
    match city:
        case "Sofia":
          commission = sales * 0.07
        case "Varna":
          commission = sales * 0.075
        case "Plovdiv":
          commission = sales * 0.08
        case _:
            isError = True
elif 1000 < sales <= 10000:
    match city:
        case "Sofia":
          commission = sales * 0.08
        case "Varna":
          commission = sales * 0.10
        case "Plovdiv":
          commission = sales * 0.12
        case _:
            isError = True
elif sales > 10000:
    match city:
        case "Sofia":
            commission = sales * 0.12
        case "Varna":
            commission = sales * 0.13
        case "Plovdiv":
            commission = sales * 0.145
        case _:
            isError = True
if isError:
    print("error")
elif sales < 0:
    print("error")
else:
    print(f"{commission:.2f}")
