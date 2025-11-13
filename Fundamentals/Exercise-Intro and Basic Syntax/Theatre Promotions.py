#A theatre is sail tickets at discount, and a program is needed to calculate the
# price of a single ticket. If the given age does not fit one of the categories,
# you should print "Error!".
#Day / Age	0 <= age <= 18	18 < age <= 64	64 < age <= 122
#Weekday	 12$	             18$	             12$
#Weekend	 15$	             20$	             15$
#Holiday	  5$	             12$	             10$
#The input comes in two lines. On the first line,
# you will receive the type of day. On the second – the age of the person.
#Print the price of the ticket according to the table, or "Error!"
# if the age is not in the table.
#•	The age will be in the interval [-1000…1000].The type of day will always be valid.
day = input("Enter the day")
age =int(input("Enter the age"))
match day:
 case "Weekday":
     if 0 <= age <= 18:
      print("12$")
     elif 18 < age <= 64:
         print("18$")
     elif 64 < age <= 122:
         print("12$")
     else:
         print("Error")
 case "Weekend":
     if 0 <= age <= 18:
         print("15$")
     elif 18 < age <= 64:
         print("20$")
     elif 64 < age <= 122:
         print("15$")
     else:
         print("Error")
 case "Holiday":
     if 0 <= age <= 18:
         print("5$")
     elif 18 < age <= 64:
         print("12$")
     elif 64 < age <= 122:
         print("10$")
     else:
         print("Error")
