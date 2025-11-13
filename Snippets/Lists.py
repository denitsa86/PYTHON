# 1. You can remove two elements at different indexes in a Python list using either the del statement or
# the pop() method. Here's how to do it safely:
#  ✅ Using del (recommended when you know the indexes)
my_list = ['a', 'b', 'c', 'd', 'e']

# Remove elements at index 1 and 3 ('b' and 'd')
# Always delete the higher index first to avoid shifting
del my_list[3]
del my_list[1]

print(my_list)
# ✅ Using pop() (if you want to capture the removed items)
my_list = ['a', 'b', 'c', 'd', 'e']

# Remove and store the elements
removed1 = my_list.pop(3)  # 'd'
removed2 = my_list.pop(1)  # 'b'

print(my_list)
print("Removed:", removed1, removed2)
# Important Tip
# Always remove the higher index first, because removing an element shifts the positions of the
# remaining elements. If you remove the lower index first, the second index might no longer point to the
# intended item.
# 2. Covert string to a list
some_text = "a b c"
my_list = some_text.split()  # (delimeter)
print(my_list)
# convert list to string:
back_to_string = " ".join(my_list)  # " " - delimeter
print(back_to_string)
# 3. Looping trough list:
nums = [1, 2, 3]
for element in nums:
    print(element)
# Looping by index:
for index in range(0, len(nums)):
    print(nums[index])
#  Looping backwards:
# starting from -1!!!!
# 4. add items in a list / .append()/
nums = []
nums.append(1)
nums.append(2)
nums.append(20)
print(nums)
# 5. Remove an element from list /.remove()/:
# nums.remove(2)
# Remove element by index:
# .pop(index)
#   if there is no index specified it will remove the last element by default
# 6. Insert element in a list by index / .insert(index, value):
nums.insert(0, 100)
print(nums)
# 7. sum list of integers:
sum(list)
# 8. Searching in list:
# nums = [1,2,3]
#    if 2 in(not in) nums:
#    print("Yes")
# METHODS
# append() - добавяне на елемент към лист
# extend() - доб.на елементи от един лист в друг
# insert(index, value)
# pop() маха последния елемент в листа, pop(index) - маха по индекс може да се изкара като резултат
# el = list.pop()
# remove() маха определена стойност
# count()
# sort() - функция, която приема колекции, връща резултат без да модифицира
# reverse()
# copy()
# insert elements in the mid of a list:
my_list = [1, 2, 3, 4, 5]
middle_index = len(my_list) // 2
my_list[middle_index:middle_index] = ['a', 'b']
print(my_list)
# Slicing
'''stolen_items = loot[-count:] if count < len(loot) else loot[:]
This line determines which items are stolen from the treasure chest.
•	loot[-count:]: This slices the last count items from the list. For example, if 
loot = ['Gold', 'Silver', 'Bronze'] and count = 2, then loot[-2:] gives ['Silver', 'Bronze'].
•	loot[:]: This is a full copy of the list. It's used when count is greater than or equal to 
the number of items in the chest.
So this line means:
If the number of items to steal is less than the total loot, steal the last count items. Otherwise, 
steal everything.
🧠 Line 2:
loot = loot[:-count] if count < len(loot) else []
This line updates the treasure chest after the theft.
•	loot[:-count]: This removes the last count items. Using the same example, loot[:-2] gives ['Gold'].
•	[]: This clears the chest entirely if count is greater than or equal to the number of items.
So this line means:
If the number of items to steal is less than the total loot, remove the last count items. Otherwise, 
empty the chest.
'''
