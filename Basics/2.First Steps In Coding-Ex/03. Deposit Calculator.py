#каква сума ще получите в края на депозитния период при определен лихвен процент.
# Използвайте следната формула:
#сума = депозирана сума  + срок на депозита *
# ((депозирана сума * годишен лихвен процент ) / 12) INPUT:
#1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]
#2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
#3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]
#OUTPUT: Да се отпечата на конзолата сумата в края на срока.
deposit = float(input())
months = int(input())
yearly_percentage = float(input())
converted_yearly_percentage = yearly_percentage * 0.01
interest = deposit * converted_yearly_percentage
monthly_interest = interest / 12
total_amount = deposit + months * monthly_interest
print(total_amount)

