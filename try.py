mylist = [1,2,3]
mylist2 = [2,3,4]
my_set = set(mylist)
my_set2 = set(mylist2)
set3 = my_set.symmetric_difference(my_set2)
#print(set3)
for item in set3:
    print(item)