my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])    # Output: Jack
print(my_dict.get('age')) # Output: 26
# my_dict.get('address') -> None
# my_dict['address']     -> KeyError
# Key can be used either inside square brackets or with the get() method
# The difference while using get() is that it returns None instead of KeyError, if the key is not found

# Iterating Through Dictionaries

elements = input().split(" ")
bakery = {}  # bakery = dict()
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
print(bakery)

#  Dictionary Methods
# clear() – removes all the elements from the dictionary
# copy() – returns a copy of the dictionary
# pop() – removes the specific item from the dictionary
# popitem() – removes the item that was last inserted
# The sorted() method sorts the elements of a given iterable - Ascending or Descending
#    The syntax of sorted() method is:
#    iterable - sequence or collection or any iterator
#    reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
#    key (Optional) - function that serves as a key for the sort comparison
#    You can use lambda functions in the sorted() function as in the filter() and map() functions
#    With the sorted() function you pass the lambda function as key