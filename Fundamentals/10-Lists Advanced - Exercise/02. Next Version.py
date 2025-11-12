# You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}".
# Your task is to print the next version.
# The only rule is that the numbers cannot be greater than 9. If it happens, set the current number
# to 0 and increase the previous number.
# Note: there will be no case in which the first number will become greater than 9.
# Input	Output
# 1.2.3	1.2.4
# 1.3.9	1.4.0
# 3.9.9	4.0.0
current_version = input().split(".") # 1.2.3
current_version = list(map(int, current_version))
current_version[2] += 1
# Handle overflow from right to left
for i in range(len(current_version)-1, 0, -1):
    if current_version[i] > 9:
        current_version[i] = 0
        current_version[i - 1] += 1

print('.'.join(map(str, current_version)))





