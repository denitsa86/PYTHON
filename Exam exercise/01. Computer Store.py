# You will receive the parts' prices (without tax) until you receive what type of customer this is -
# special or regular.
# The taxes are 20% of each part's price you receive.
# If the customer is special, he has a 10% discount on the total price with taxes.
# If a given price is not a positive number, you should print "Invalid price!" on the console and
# continue with the next price.
# If the total price is equal to zero, you should print "Invalid order!" on the console.
command = input()
total_price = 0
while command != "special" and command != "regular":
    part_price = float(command)
    if part_price < 0:
        print("Invalid price!")
    else:
        total_price += part_price

    command = input()
if total_price <= 0:
    print("Invalid order!")
else:
    taxes = total_price * 20 / 100
    total_price_with_taxes = total_price + taxes
    if command == "special":
        total_price_with_taxes = total_price_with_taxes * 0.90
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
