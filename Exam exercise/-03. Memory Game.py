# On the first line, you will receive a sequence of elements. Each element in the sequence will have a
# twin. Until the player receives "end" from the console, you will receive strings with two integers
# separated by a space, representing the indexes of elements. If the player enters two equal indexes
# or indexes which are out of bounds of the sequence, you should add two matching elements at the middle
# of the sequence in the following format:  "-{number of moves until now}a"
# Then print this message on the console:
# "Invalid input! Adding additional elements to the board"
elements = list(input().split())
command = input().split()
moves = 0
while command[0] != "end":
    if len(elements) <= 0:  # WIN
        break
    first_index = int(command[0])
    second_index = int(command[1])
    moves += 1
    if first_index == second_index or \
            first_index < 0 or second_index < 0 or \
            first_index >= len(elements) or second_index >= len(
        elements):  # 0 > first_index or 0 > second_index or first_index > len(elements) - 1 or second_index > len(elements) - 1:
        middle_index = len(elements) // 2
        elements.insert(middle_index, f"-{moves}a")
        elements.insert(middle_index + 1, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    # •	Every time the player hit two matching elements, you should remove them from the sequence and print on the console the following message:
    # "Congrats! You have found matching elements - {element}!"
    elif elements[first_index] == elements[second_index]:
        if first_index > second_index:
            removed_element = elements.pop(first_index)
            elements.pop(second_index)
        else:
            removed_element = elements.pop(second_index)
            elements.pop(first_index)
        print(f"Congrats! You have found matching elements - {removed_element}!")
        # •	If the player hit two different elements, you should print on the console the following message:
        # "Try again!"
    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    command = input().split()
if len(elements) <= 0:
    print(f"You have won in {moves} turns!")
elif len(elements) > 0:
    print("Sorry you lose :(")
    print(" ".join(map(str, elements)))
