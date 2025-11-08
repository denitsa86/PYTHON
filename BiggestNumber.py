def biggest_number(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(biggest_number(1,2,3))

mylist = [1,2,3]
mylist2 = [2,3,4]
my_set = set(mylist)
my_set2 = set(mylist2)
set3 = my_set.symmetric_difference(my_set2)
print(set3)