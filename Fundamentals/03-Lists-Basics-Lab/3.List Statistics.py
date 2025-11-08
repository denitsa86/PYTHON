#You will be given a number n. On the next n lines you will receive integers. You have to create and print
# two lists:
# •	One with all the positives (including 0) numbers
# •	One with all the negatives numbers
# Finally print the following message:
# "Count of positives: {count_positives}. Sum of negatives: {sum_of_negatives}"
number_count = int(input())
positive_list = []
negative_list = []

for n in range(number_count):
    number = int(input())
    if number >= 0:
        positive_list.append(number)
    elif number < 0:
        negative_list.append(number)

print(positive_list)
print(negative_list)
print(f"Count of positives: {len(positive_list)}. Sum of negatives: {sum(negative_list)}")

