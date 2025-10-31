# Магазин за плодове през работните дни работи на следните цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.50	1.20	 0.85	 1.45	    2.70	  5.50	    3.85
# През събота и неделя магазинът работи на по-високи цени:
# плод	banana	apple	orange	grapefruit	kiwi	pineapple	grapes
# цена	2.70	 1.25	 0.90	 1.60	    3.00	 5.60	    4.20
# •	плод  - banana / apple / orange / grapefruit / kiwi / pineapple / grapes;
# •	ден от седмицата  - Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday;
# •	количество (реално число).
# Резултатът да се отпечата закръглен с 2 цифри след десетичната точка.
# При невалиден ден от седмицата или невалидно име на плод да се отпечата "error".
from unittest import case
fruit = input()
day = input()
quantity = float(input())

cost = 0
valid = True

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        cost = quantity * 2.50
    elif fruit == "apple":
        cost = quantity * 1.20
    elif fruit == "orange":
        cost = quantity * 0.85
    elif fruit == "grapefruit":
        cost = quantity * 1.45
    elif fruit == "kiwi":
        cost = quantity * 2.70
    elif fruit == "pineapple":
        cost = quantity * 5.50
    elif fruit == "grapes":
        cost = quantity * 3.85
    else:
        valid = False
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        cost = quantity * 2.70
    elif fruit == "apple":
        cost = quantity * 1.25
    elif fruit == "orange":
        cost = quantity * 0.90
    elif fruit == "grapefruit":
        cost = quantity * 1.60
    elif fruit == "kiwi":
        cost = quantity * 3.00
    elif fruit == "pineapple":
        cost = quantity * 5.60
    elif fruit == "grapes":
        cost = quantity * 4.20
    else:
        valid = False
else:
    valid = False

if valid:
    print(f"{cost:.2f}")
else:
    print("error")





