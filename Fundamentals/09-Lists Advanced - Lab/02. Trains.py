# number representing the number of wagons a train has. Create a list (train) with the given
# length containing only zeros. Until you receive the command "End", you will receive some of the
# following commands:
# •	"add {people}" – you should add the number of people in the last wagon
# •	"insert {index} {people}" - you should add the number of people at the given wagon
# •	"leave {index} {people}" - you should remove the number of people from the wagon.
# There will be no case in which the people will be more than the count in the wagon.

wagons = int(input())
train = [0] * wagons
command = input()
while command != "End":
    action = command.split()
    if action[0] == "add":
        people = int(action[1])
        train[-1] += people
    elif action[0] == "insert":
        index = int(action[1])
        people = int(action[2])
        train[index] += people
    elif action[0] == "leave":
        index = int(action[1])
        people = int(action[2])
        train[index] -= people

    command = input()

print(train)
