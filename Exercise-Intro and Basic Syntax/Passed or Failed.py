#Modify the program from the previous problem, so it will print "Failed!"
# if the grade is lower than 3.00.
#The output is either "Passed!" if the grade
# is more than 2.99, otherwise you should print "Failed!".
grade = float(input("What`s your garde?"))
if grade >= 3.00:
    print("Passed!")
else:
    print("Failed!")