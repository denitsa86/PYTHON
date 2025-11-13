#Create a program that receives an integer and prints the matching month.
# If the number is more than 12 or less than 1 print "Error!".
#You will receive a single integer on a single line.
#If the number is within the boundaries print the corresponding month,
# otherwise print "Error!".
number = int(input("Enter a number from 1 to 12: "))
if number == 1:
    print("January")
elif number == 2:
    print("February")
elif number == 3:
    print("March")
elif number == 4:
    print("April")
elif number == 5:
    print("May")
elif number == 6:
    print("June")
elif number == 7:
    print("July")
elif number == 8:
    print("August")
elif number == 9:
    print("September")
elif number == 10:
    print("October")
elif number == 11:
    print("November")
elif number == 12:
    print("December")
else:
    print("Error!")