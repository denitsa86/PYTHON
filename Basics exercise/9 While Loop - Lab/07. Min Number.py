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