# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва
# ден от седмицата (на английски език), в граници [1...7] или отпечатва "Error" в
# случай, че въведеното число е невалидно.
from unittest import case

number = int(input())
if 1 <= number <= 7:
 match number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
else:
    print("Error")

