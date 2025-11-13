# чете от конзолата цели числа, докато не се получи команда "stop". Да се намери сумата на всички въведени
# прости и сумата на всички въведени непрости числа. Тъй като по дефиниция от математиката отрицателните
# числа не могат да бъдат прости, ако на входа се подаде отрицателно число, да се изведе следното съобщение
# "Number is negative.". В този случай въведено число се игнорира и не се прибавя към нито една от двете
# суми, а програмата продължава своето изпълнение, очаквайки въвеждане на следващо число.
# На изхода да се отпечатат на два реда двете намерени суми в следния формат:
# •	"Sum of all prime numbers is: {prime numbers sum}"
# •	"Sum of all non prime numbers is: {nonprime numbers sum}"
from sympy import isprime
sum_prime = 0
sum_non_prime = 0

while True:
    number = input()
    if number == "stop":
        break
    num = int(number)
    if num < 0:
        print("Number is negative.")
        continue
    if isprime(num):
        sum_prime += num
    else:
        sum_non_prime += num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
