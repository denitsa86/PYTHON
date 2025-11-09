# You will be receiving to-do notes until you get the command "End". The notes will be in the
# format: "{importance}-{note}".
# Return a list containing all to-do notes sorted by importance in ascending order.
# The importance value will always be an integer between 1 and 10 (inclusive).
# Hint
# # •	Use the insert() method.
# # Example
# # Input	Output
# # 2-Walk the dog
# 1-Drink coffee
# 6-Dinner
# 5-Work
# End	['Drink coffee', 'Walk the dog', 'Work', 'Dinner']
command = input()
to_do_list = [0] * 10
while command != "End":
    priority, task = command.split("-")
    priority = int(priority) - 1
    to_do_list[priority] = task
    command = input()
result = []
for item in to_do_list:
    if item != 0:
        result.append(item)
print(result)