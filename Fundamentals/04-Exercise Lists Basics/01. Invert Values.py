#Write a program that receives a single string containing numbers separated by a single space. Print a
# list containing the opposite of each number.
#1 2 -3 -3 5	[-1, -2, 3, 3, -5]
entry = input()
entry_string = entry.split(" ")
opposite_list = []
for num in entry_string:
    opposite_list.append(-int(num))
print(opposite_list)

