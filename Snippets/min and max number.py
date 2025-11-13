import sys
entry = input()
max_num = -sys.maxsize

while entry != "Stop":
    if int(entry) > max_num:
        max_num = int(entry)
        entry = input()
    else:
        entry = input()
print(max_num)

#-----------
import sys
entry = input()
min_num = sys.maxsize

while entry != "Stop":
    if int(entry) < min_num:
        min_num = int(entry)
        entry = input()
    else:
        entry = input()
print(min_num)