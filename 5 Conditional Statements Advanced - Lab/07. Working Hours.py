#чете час от денонощието(цяло число) и ден от седмицата(текст) - въведени от
# потребителя и проверява дали офисът на фирма е отворен, като работното време
# на офисът е от 10-18 часа, от понеделник до събота включително
from unittest import case

hour = int(input())
weekday = input()
if 10 <= hour <= 18:
    match weekday:
        case "Monday":
            print("open")
        case "Tuesday":
            print("open")
        case "Wednesday":
            print("open")
        case "Thursday":
            print("open")
        case "Friday":
            print("open")
        case "Saturday":
            print("open")
        case "Sunday":
            print("closed")
else:
    print("closed")