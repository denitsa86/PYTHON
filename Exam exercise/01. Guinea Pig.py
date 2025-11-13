food = float(input()) * 1000
hay = float(input()) * 1000
cover = float(input()) * 1000
weight = float(input()) * 1000
for day in range(1, 30 + 1):
    if food <= 0 or hay <= 0 or cover <= 0 or weight <= 0:
        break
    food -= 300
    if day % 2 == 0 and day > 0:
        hay -= food * 0.05
    if day % 3 == 0:
        cover -= weight / 3
if food <= 0 or hay <= 0 or cover <= 0 or weight <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food / 1000:.2f}, Hay: {hay / 1000:.2f}, Cover: {cover / 1000:.2f}.")
