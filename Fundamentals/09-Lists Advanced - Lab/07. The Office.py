#Receive Two Lines of Input: a List of Employee's Happiness As String with Numbers Separated
# by a Single Space and a Happiness Improvement Factor (Single Number).
# Your Task is to Find Out If the Employees Are Generally Happy in Their Office.
#You Have to Increase Their Happiness by Multiplying the All the Employee's Happiness
#by the Factor, Filter the Employees Which Happiness is Greater Than or Equal to the Average
# in the New List and Print the Result
# •	If the half or more of the employees have happiness >= than the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# •	Otherwise: "Score: {happy_count}/{total_count}. Employees are not happy!"
happy_employees = list(map(int,input().split()))
factor = int(input())
multiplied_happiness = [h * factor for h in happy_employees]
average_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
result = list(filter(lambda n: n >= average_happiness, multiplied_happiness))
half = len(happy_employees) / 2
if len(result) >= half:
    print(f"Score: {len(result)}/{len(happy_employees)}. Employees are happy!")
else:
    print(f"Score: {len(result)}/{len(happy_employees)}. Employees are not happy!")
