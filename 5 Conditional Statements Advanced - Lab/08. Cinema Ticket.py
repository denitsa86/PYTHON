# Да се напише програма която чете ден от седмицата (текст) – въведен от потребителя
# и принтира на конзолата цената на билет за кино според деня от седмицата:
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	      12	 14	          14	      12	  16	      16
from unittest import case

day = input()
match day:
    case "Monday":
        print("12")
    case "Tuesday":
        print("12")
    case "Wednesday":
        print("14")
    case "Thursday":
        print("14")
    case "Friday":
        print("12")
    case "Saturday":
        print("16")
    case "Sunday":
        print("16")
