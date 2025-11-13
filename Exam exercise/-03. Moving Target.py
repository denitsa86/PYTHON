# sequence of targets with their integer values, split by a single space
targets = list(map(int, input().split()))
command = input().split()
while command[0] != "End":  # 52 74 23 44 96 110
    index = int(command[1])
    if command[0] == "Shoot":
        power = int(command[2])
        if 0 <= index <= len(targets) - 1:
            targets[index] -= power
            if targets[index] < 0:
                targets.pop(index)
    # •	"Add {index} {value}"
    # o	Insert a target with the received value at the received index if it exists.
    # o	If not, print: "Invalid placement!"
    elif command[0] == "Add":
        value = int(command[2])
        if 0 <= index <= len(targets) - 1:
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    # •	"Strike {index} {radius}"  #1 2 3 4 5
    # o	Remove the target at the given index and the ones before and after it depending on the radius.
    # o	If any of the indices in the range is invalid, print: "Strike missed!" and skip this command.
    elif command[0] == "Strike":
        radius = int(command[2])
        if index - radius >= 0 and index + radius < len(targets):
            for i in range(index + radius, (index - radius) - 1, -1):
                targets.pop(i)
        else:
            print("Strike missed!")

    command = input().split()

print("|".join(map(str, targets)))
