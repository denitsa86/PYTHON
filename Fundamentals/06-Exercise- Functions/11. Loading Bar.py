# 30	30% [%%%.......]
# Still loading...
# 100	100% Complete!
# [%%%%%%%%%%]
def return_loading_bar(num):
    percent_count = int(num / 10)
    total_count = 10
    loading_bar = []
    for i in range(percent_count):
        loading_bar.append("%")
    for j in range(len(loading_bar) + 1, total_count + 1):
        loading_bar.append(".")
    #loading_bar = "".join(loading_bar)
    return loading_bar

number = int(input())
bar = return_loading_bar(number)
ready_counter = 0
for i in bar:
    if i == "%":
        ready_counter += 1
if ready_counter == 10:
    print("100% Complete!")
    print(f"[{''.join(bar)}]")
else:
    print(f"{number}% [{''.join(bar)}]")
    print("Still loading...")



