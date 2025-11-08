entry = input()
total_sum = 0

while entry != "NoMoreMoney":
    if float(entry) < 0:
        print("Invalid operation!")
        break
    total_sum += float(entry)
    print(f"Increase: {float(entry):.2f}")
    entry = input()
print(f"Total: {total_sum:.2f}")