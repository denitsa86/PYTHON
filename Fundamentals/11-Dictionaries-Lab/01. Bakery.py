#You will receive a single line containing some food (keys) and quantities (values). They will
# be separated by a single space (the first element is the key, the second – is the value,
# and so on). Create a dictionary with all the keys and values and print it on the console.
# bread 10 butter 4 sugar 9 jam 12
elements = input().split()
products = {}

for index in range(0, len(elements), 2):
    current_product = elements[index]
    quantity = int(elements[index + 1])
    products[current_product] = quantity

print(products)