#You will receive a single number n. On the next n lines you will receive integers. After that you will
# be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). print the result.
number_count = int(input())
even_list = []
odd_list = []
positive_list = []
negative_list = []
for x in range(number_count):
    number = int(input())
    if number % 2 == 0:
        even_list.append(number)
    if number % 2 != 0:
        odd_list.append(number)
    if number >= 0:
        positive_list.append(number)
    if number < 0:
        negative_list.append(number)
criteria = input()
if criteria == "even":
    print(even_list)
elif criteria == "odd":
    print(odd_list)
elif criteria == "positive":
    print(positive_list)
elif criteria == "negative":
    print(negative_list)

