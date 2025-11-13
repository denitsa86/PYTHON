
# •	"Loot {item1} {item2}…{itemn}":
# o	Pick up treasure loot along the way. Insert the items at the beginning of the chest.
# o	If an item is already contained, don't insert it.
# •	"Drop {index}":
# o	Remove the loot at the given position and add it at the end of the treasure chest.
# o	If the index is invalid, skip the command.
# •	"Steal {count}":
# o	Someone steals the last count loot items. If there are fewer items than the given count, remove
# as much as there are.
# o	Print the stolen items separated by ", ":
loot = input().split("|")
command = input().split()
while command[0] != "Yohoho!":
    if command[0] == "Loot":
        #loot = [loot.insert(0,command[i]) for i in range(1,len(command)) if command[i] not in loot]
         for i in range(1,len(command)):
             if command[i] not in loot:
                 loot.insert(0, command[i])

    elif command[0] == "Drop":
        index = int(command[1])
        if 0 <= index < len(loot):
             dropped_item = loot.pop(int(index))
             loot.append(dropped_item)

    elif command[0] == "Steal": #3
        count = int(command[1])
        stolen_items = []
        stolen_items = loot[-count:] if count < len(loot) else loot [:]
        loot = loot[:-count] if count < len(loot) else []
        print(", ".join(stolen_items))

    command = input().split()

if len(loot) > 0:
    length = sum(len(i) for i in loot)
    print(f"Average treasure gain: {length / len(loot):.2f} pirate credits.")
elif len(loot) <= 0:
    print("Failed treasure hunt.")




