#write a function that checks if a number falls between two other numbers
#1,2,3  #3,4,5
def find_middle_number(number_to_check,num1,num2):
    if number_to_check > num1 and number_to_check < num2:
        is_middle = True
    elif num1 > number_to_check > num2:
        is_middle = True
    else:
        is_middle = False
    return is_middle

#numbers_to_check = input("Enter 3 numbers to check without any character or space between them: ")
number = int(input())
number1 = int(input())
number2 = int(input())
print(find_middle_number(int(number),int(number1),int(number2)))