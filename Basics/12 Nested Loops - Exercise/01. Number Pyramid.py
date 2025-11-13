n = int(input())

current = 1
row = 1

while current <= n:
    for i in range(row):
        if current > n:
            break
        print(current, end=' ')
        current += 1
    print()
    row += 1