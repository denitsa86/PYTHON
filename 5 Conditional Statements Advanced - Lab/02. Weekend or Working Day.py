#Напишете програма която, чете ден от седмицата (текст), на английски език -
# въведен от потребителя.Ако денят е работен отпечатва на конзолата - "Working day",
# ако е почивен - "Weekend". Ако се въведе текст различен от ден от седмицата да се
# отпечата - "Error".
from unittest import case

day = input()

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Working day")
    case "Sunday" | "Saturday" :
        print("Weekend")
    case _:
        print("Error")