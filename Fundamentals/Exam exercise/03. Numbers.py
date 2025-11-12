#Write a program to read a sequence of integers and find and print the top 5 numbers greater than the
# average value in the sequence, sorted in descending order.
#•	Print the above-described numbers on a single line, space-separated.
# •	If less than 5 numbers hold the property mentioned above, print less than 5 numbers.
# •	Print "No" if no numbers hold the above property.
#5 2 3 4 -10 30 40 50 20 50 60 60 51  #60 60 51 50 50
numbers = list(map(int, input().split()))
average = sum(numbers) / len(numbers)
average_max_numbers = sorted(([n for n in numbers if n > average]),key=int, reverse=True)  #sorted(ListB, key=int, reverse=True)
final_list = []
max_list_length = 5
for i in range(0,len(average_max_numbers)):
    if len(final_list) >= max_list_length:
        break
    final_list.append(average_max_numbers[i])
if len(final_list) > 0:
    print(" ".join(map(str,final_list)))
else:
    print("No")
