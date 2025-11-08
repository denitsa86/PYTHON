#Write a program that receives a single string (integers separated by a comma and space ", "), finds
# all the zeros and moves them to the back without messing up the other elements. Print the
# resulting integer list
#1, 0, 1, 2, 0, 1, 3	[1, 1, 2, 1, 3, 0, 0]
numbers = input().split(", ")
length = len(numbers)
zeros = []
for num in range(0, len(numbers)-1):
    if num > len(numbers)-1:
        break
    if numbers[num] == "0":
        zeros.append(numbers[num])
        numbers.remove(numbers[num])
print(', '.join(numbers + zeros))