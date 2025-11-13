# град / продукт	coffee	water	beer	sweets	peanuts
# Sofia	            0.50	0.80	1.20	1.45	1.60
# Plovdiv	        0.40	0.70	1.15	1.30	1.50
# Varna	            0.45	0.70	1.10	1.35	1.55
#Input: продукт (текст), град (текст) и количество (десетично число)
# oтпечатва колко струва съответното количество от избрания продукт в посочения град.
product = input()
city = input()
quantity = float(input())
cost = 0
if city == "Sofia":
    match product:
        case "coffee":
            cost = quantity * 0.50
        case "water":
            cost = quantity * 0.80
        case "beer":
            cost = quantity * 1.20
        case "sweets":
            cost = quantity * 1.45
        case "peanuts":
            cost = quantity * 1.60
elif city == "Plovdiv":
    match product:
        case "coffee":
            cost = quantity * 0.40
        case "water":
            cost = quantity * 0.70
        case "beer":
            cost = quantity * 1.15
        case "sweets":
            cost = quantity * 1.30
        case "peanuts":
            cost = quantity * 1.50
else:
    match product:
        case "coffee":
            cost = quantity * 0.45
        case "water":
            cost = quantity * 0.70
        case "beer":
            cost = quantity * 1.10
        case "sweets":
            cost = quantity * 1.35
        case "peanuts":
            cost = quantity * 1.55
print(cost)
