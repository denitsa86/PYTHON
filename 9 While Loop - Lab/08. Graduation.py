#На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни
# оценки. Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или
# равна на 4.00. Ако ученикът бъде скъсан повече от един път, то той бива изключен и
# програмата приключва, като се отпечатва името на ученика и в кой клас бива изключен.
# При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
student = input()
year = 1
fails = 0
total_grade = 0
while year <= 12:
    grade = float(input())
    if grade < 4.00:
        fails += 1
        if fails > 1:
            print(f"{student} has been excluded at {year} grade")
            break
        continue
    total_grade += grade
    year += 1

if year >= 12:
    average_grade = total_grade / 12
    print(f"{student} graduated. Average grade: {average_grade:.2f}")

