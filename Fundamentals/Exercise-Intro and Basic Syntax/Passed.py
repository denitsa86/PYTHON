#Create a program, that receives a single number as an input representing a grade.
#Print to the console:
#	"Passed!" if the grade is equal or more than 3.00.
#The input comes as a single floating-point number.
#The output is either "Passed!" if the grade is equal or more than 3.00, otherwise you should print nothing.

grade = float(input("What`s your garde?"))
if grade >= 3.00:
    print("Passed!")
