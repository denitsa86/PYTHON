#Each product has a name, a price, and a quantity:
#•	If the product doesn't exist yet, add it with its starting quantity.
# •	If you receive a product, that already exists, increase its quantity by the input quantity and
# if its price is different, replace the price as well.
#•	Until you receive "buy", the products will be coming in the format: "{name} {price} {quantity}".
#•	Print information about each product in the following format: "{product_name} -> {total_price}"
products = {}
data = input().split()

while data[0] != "buy":
    name = data[0]
    price = float(data[1])
    quantity = float(data[2])
    total_price = [price, quantity]
    if name not in products:
        products[name] = total_price
    else:
        products[name][1] += quantity
        if products[name][0] != price:
            products[name][0] = price

    data = input().split()

for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
