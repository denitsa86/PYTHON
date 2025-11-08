#Write a function that receives a string and a repeat count n. The function should return a
# new string (the old one repeated n times). abc
def repeat_string(string, number):
    for n in range(number):
        print(string, end='')

statement = input()
repeat = int(input())
repeat_string(statement, repeat)
