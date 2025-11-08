#Create a function that receives three parameters and calculates a result depending on operator.
# The operator can be  'multiply', 'divide', 'add', 'subtract' . The input comes as three parameters –
# two integers and an operator as a string
def calculate_result(act,num1,num2):
    if act == "multiply":
        return num1 * num2
    elif act == "divide":
        return num1 / num2
    elif act == "add":
        return num1 + num2
    elif act == "subtract":
        return num1 - num2

operator = input()
number_one = int(input())
number_two = int(input())
print(int(calculate_result(operator,number_one,number_two)))