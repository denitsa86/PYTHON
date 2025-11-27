#Write a program that receives a list of characters separated by ", ". It should create
# a dictionary with each character as a key and its ASCII value as a value. Try solving that
# problem using comprehension.
# a, b, c, a	   {'a': 97, 'b': 98, 'c': 99}
#ascii_one = ord(x)
data = input().split(", ")
my_dict = {}

for i in range(0, len(data)):
    if data[i] not in my_dict:
        my_dict[data[i]] = ord(data[i])


print(my_dict)
