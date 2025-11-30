# win a legendary item. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials , and everything else is junk.
# input in the format: "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, and motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.
# 3 Motes 5 stones 5 Shards
# 6 leathers 255 fragments 7 Shards
key_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}
legendary_item_obtained = False
# iterate list to find the key and value
while not legendary_item_obtained:
    try:
        data = input().split()
    except EOFError:
        break
    for i in range(0, len(data), 2):
        if legendary_item_obtained:
            break
        value = int(data[i])
        item = data[i + 1].lower()
        # check if legendary or junk

        if item in key_items:
            key_items[item] += value
            for key, value in key_items.items():
                if key_items[key] >= 250:
                    key_items[key] -= 250
                    match key:
                        case "shards":
                            print(f"Shadowmourne obtained!")
                        case "fragments":
                            print(f"Valanyr obtained!")
                        case "motes":
                            print(f"Dragonwrath obtained!")
                    legendary_item_obtained = True
                    break
        else:
            if item in junk_items:
                junk_items[item] += value
            else:
                junk_items[item] = value

print(f"shards: {key_items['shards']}")
print(f"fragments: {key_items['fragments']}")
print(f"motes: {key_items['motes']}")
for key, value in junk_items.items():
    print(f"{key.lower()}: {value}")
