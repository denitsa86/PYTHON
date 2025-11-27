#You will be given key-value pairs of products and quantities (on a single line separated by
# space). On the following line, you will be given products to search for. Check for each
# product. You have 2 possibilities:
# •	If you have the product, print "We have {quantity} of {product} left".
# •	Otherwise, print "Sorry, we don't have {product}".
# cheese 10 bread 5 ham 10 chocolate 3
# jam cheese ham tomatoes
data = input().split()
searched = input().split()
products = {}
for index in range(0, len(data), 2):
    current_product = data[index]
    quantity = int(data[index + 1])
    products[current_product] = quantity

for s_pr in searched:
    if s_pr not in products:
        print(f"Sorry, we don't have {s_pr}")
    else:
        print(f"We have {products[s_pr]} of {s_pr} left")
