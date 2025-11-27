# sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the
# console represents a resource and every even - quantity. Your task is to collect the
# resources and print them each on a new line.
# "{resource} -> {quantity}"

# elements = input().split(" ")
# bakery = {}  # bakery = dict()
# for i in range(0, len(elements), 2):
#     key = elements[i]
#     value = elements[i + 1]
#     bakery[key] = int(value)
# print(bakery)

resources = {}
data = input()
count = 0
key_exists = False
while data != "stop":
    count += 1
    if count % 2 != 0:
        if data in resources:
            key_exists = True
            key = data
        else:
            key_exists = False
            key = data
    else:
        if key_exists:
            resources[key] += int(data)
        else:
            resources[key] = int(data)

    data = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
