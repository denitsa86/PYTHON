# •	Първи ред – начало на интервала – цяло число в интервала [1...999]
# •	Втори ред – край на интервала – цяло число в интервала [по-голямо от първото число...1000]
# •	Трети ред – магическото число – цяло число в интервала [1...10000]
#програма която проверява всички възможни комбинации от двойка числа в интервала от две дадени числа.
# На изхода се отпечатва, коя поред е комбинацията чиито сбор от числата е равен на дадено магическо число.
start_number = int(input())
end_number = int(input())
magic_number = int(input())
combinations = 0
magic_number_found = False
# •	Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o	"Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# •	Ако не е намерена комбинация отговаряща на условието
# o	"{броят на всички комбинации} combinations - neither equals {магическото число}"
for i in range(start_number, end_number + 1):
    for j in range(start_number, end_number + 1):
        combinations += 1
        if i + j == magic_number:
            print(f"Combination N:{combinations} ({i} + {j} = {magic_number})")
            magic_number_found = True
            break
    if magic_number_found:
        break
if not magic_number_found:
    print(f"{combinations} combinations - neither equals {magic_number}")



