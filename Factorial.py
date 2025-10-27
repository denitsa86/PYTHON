# write a function that calculates the factorial of a number
def find_factorial(number):
    result = 1
    for i in range(1,number+1):
        result *= i
    return result

start_number = int(input("Enter a number: "))
print(find_factorial(start_number))

