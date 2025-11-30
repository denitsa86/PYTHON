# 1. Creating a dictionary
my_dict = {'name':'Jack', 'age': 26}
print(my_dict['name'])    # Output: Jack
print(my_dict.get('age')) # Output: 26
print(my_dict.keys())  # --> дава dict_keys
print(my_dict.values())  # -- all values
# my_dict.get('address') -> None
# my_dict['address']     -> KeyError
# Key can be used either inside square brackets or with the get() method
# The difference while using get() is that it returns None instead of KeyError, if the key is
# not found
# !!!! for by default is iterating trough the keys

# 2. Iterating Through Dictionaries
  # a. iterating using keys:
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(key, end="") # 1 2 3
  # changing the values:
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    squares[key] *= 2 # {1: 2, 2: 8, 3: 18}
  #b. iterating trough values:
     # using values() method
squares = {1: 1, 2: 4, 3: 9}
for value in squares.values():
    print(value, end="") # 1 4 9
     # using the key to get the value
squares = {1: 1, 2: 4, 3: 9}
for key in squares.keys():
    print(squares[key], end="") # 1 4 9
    # c. Iterating using items()
squares = {1: 1, 2: 4, 3: 9}
for key, value in squares.items():
    print(f"key: {key}, value: {value}")
# 3. Existence in dictionary = by default in is searching trough the keys
my_dict = {'name':'Jack', 'age': 26}
if "name" in my_dict:
    print(my_dict['name'])  # Jack
 # check in values:
my_dict = {'name':'Jack', 'age': 26}
if 26 in my_dict.values():
    print("22 is a value in my dictionary")
# 4. sorted() method
#sorted(iterable[,key][reversed])
dict = {"a": 1, "b": 2, "c": 3}

#key--стартегия за сортиране
print(sorted(dict.items(),key=lambda kvp: kvp[1], reverse = True )) #sort values ascending/ = reverse descending


elements = input().split(" ")
bakery = {}  # bakery = dict()
for i in range(0, len(elements), 2):
    key = elements[i]
    value = elements[i + 1]
    bakery[key] = int(value)
print(bakery)

"""
 Dictionary Methods
.items() = tuple
clear() – removes all the elements from the dictionary
copy() – returns a copy of the dictionary
pop() – removes the specific item from the dictionary; key.pop() -> returns the value
popitem() – removes the item that was last inserted
The sorted() method sorts the elements of a given iterable - Ascending or Descending
   The syntax of sorted() method is:
   iterable - sequence or collection or any iterator
   reverse (Optional) - If true, the sorted list is reversed (or sorted in Descending order)
   key (Optional) - function that serves as a key for the sort comparison
   You can use lambda functions in the sorted() function as in the filter() and map() functions
   With the sorted() function you pass the lambda function as key
The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)  # {'brand': 'Ford', 'year': 1964}
"""
"""
Dictionary is an unordered collection of items! It has key-value pairs. (hashmap)
-mutable-can be changed
my_dict = {}
my_dict = {'fruit : apple', 'vegetable : cucumber'} --> 2 elements
Values: can repeat
Keys: immutable; can`t repeat
To access value in a dict use key
print(my_dict.get['fruit']) --> with get you receive None if the key is not existing
without get you will receive KeyError
"""
# zip () method -- zip to tuples and turn into dict
countries = input().split(", ")
capitals = input().split(", ")
report = zip(countries, capitals)
my_dict = dict(report)
for key, value in my_dict.items():
    print(f"{key} -> {value}")

"""
# Dictionary with lists of numbers as values
my_dict = {
    "scores": [10, 20, 30],
    "ages": [25, 30, 35],
    "prices": [100, 200, 300]
}

# ✅ Increase each number in the list by 5
my_dict["scores"] = [num + 5 for num in my_dict["scores"]]
print(my_dict["scores"])   # Output: [15, 25, 35]

# ✅ Substitute a specific number (e.g., replace 30 with 99 in 'ages')
my_dict["ages"] = [99 if num == 30 else num for num in my_dict["ages"]]
print(my_dict["ages"])     # Output: [25, 99, 35]

# ✅ Directly update by index (e.g., change the first price to 150)
my_dict["prices"][0] = 150
print(my_dict["prices"])   # Output: [150, 200, 300]

"""

# The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)   # dict_keys(['brand', 'model', 'year'])