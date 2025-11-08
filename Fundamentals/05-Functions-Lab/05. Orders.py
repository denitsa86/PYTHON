#Write a function that calculates the total price of an order and prints it on the console. The function
# should receive one of the following products: coffee, coke, water, snacks; and a quantity of the product.
# The prices for a single piece of each product are:
# •	coffee - 1.50
# •	water - 1.00
# •	coke - 1.40
# •	snacks - 2.00
# Print the result formatted to the second decimal place.
def calculate_price(item,qty):
    price = 0
    if item == "coffee":
        price = qty * 1.50
    elif item == "coke":
        price = qty * 1.40
    elif item == "water":
        price = qty * 1.00
    elif item == "snacks":
        price = qty * 2.00
    print(f"{price:.2f}")

product = input()
quantity = int(input())
calculate_price(product, quantity)