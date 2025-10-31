# •	N1 - цяло число;
# •	N2 - цяло число;
# •	Оператор - един символ измежду: "+", "-", "*", "/", "%".
number1 = int(input())
number2 = int(input())
operator = input()
result = 0
even_or_odd = ""
#При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултатът и
# дали той е четен или нечетен
#"{N1} {оператор} {N2} = {резултат} - {even/odd}"
if operator == "+" or operator == "-" or operator == "*":
    match operator:
        case "+":
            result = number1 + number2
        case "-":
            result = number1 - number2
        case "*":
            result = number1 * number2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print (f"{number1} {operator} {number2} = {result} - {even_or_odd}")
elif operator == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 / number2
        print(f"{number1} / {number2} = {result:.2f}")
#	"{N1} % {N2} = {остатък}"
#	"Cannot divide {N1} by zero"
elif operator == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        result = number1 % number2
        print(f"{number1} % {number2} = {result}")


