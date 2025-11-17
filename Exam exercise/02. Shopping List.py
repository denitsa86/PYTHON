# initial list with groceries separated by an exclamation mark "!".
# 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists,
# skip this command.
groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item = command[1]
    if action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)

    # •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list.
    # Otherwise, skip this command.
    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    # •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name
    # with the new one. Otherwise, skip this command.
    elif action == "Correct":
        new_item = command[2]
        for i in range(0, len(groceries)):
            if groceries[i] == item:
                groceries[i] = new_item

    # •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position
    # and add it at the end of the list. Otherwise, skip this command
    elif action == "Rearrange":
        for i in range(0, len(groceries)):
            if groceries[i] == item:
                removed_item = groceries.pop(i)
                groceries.append(removed_item)

    command = input()

# •	Print the list with all the groceries, joined by ", ":
print(", ".join(groceries))
