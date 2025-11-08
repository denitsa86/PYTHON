#You will receive three integer numbers.
#Write a function sum_numbers() to get the sum of the first two integers and subtract()
# function that subtracts the third integer from the result. Wrap the two functions in a function
# called add_and_subtract() which will receive the three numbers
def sum_numbers(num1, num2):
    return  num1 + num2

def substract(result,num3):
    return result - num3

def add_and_subtract(num1,num2,num3):
    total = sum_numbers(num1,num2)
    result = substract(total,num3)
    return result

number_one = int(input())
number_two = int(input())
number_three = int(input())
print(add_and_subtract(number_one,number_two,number_three))