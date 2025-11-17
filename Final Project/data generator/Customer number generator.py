import os

count = 11500
start = 4_000_000_000  # smallest 10-digit number starting with 4

numbers = [str(start + i) for i in range(count)]

# Save to a text file, one per line
with open("../numbers.txt", "w") as f:
    f.write("\n".join(numbers))
print(os.getcwd())
