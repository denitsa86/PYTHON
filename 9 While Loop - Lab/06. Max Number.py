#Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени
# от потребителя,  намира най-голямото измежду тях и го принтира. Въвежда се по едно
# число на ред.
import sys
entry = input()
max_num = -sys.maxsize

while entry != "Stop":
    if int(entry) > max_num:
        max_num = int(entry)
        entry = input()
    else:
        entry = input()
print(max_num)