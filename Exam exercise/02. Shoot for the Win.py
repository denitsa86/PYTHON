# track of your shot targets. You will receive a sequence with integers, separated by a single space,
# representing targets and their value. you will be receiving indices until the "End" command
# Every time you receive an index, you need to shoot the target on that index, if it is possible.
# Every time you shoot a target, its value becomes -1, and it is considered a shot. Along with that,
# you also need to:
# •	Reduce all the other targets, which have greater values than your current target, with its value.
# •	Increase all the other targets, which have less than or equal value to the shot target, with its
# value.
targets = list(map(int, input().split()))
command = input()
shot_targets = 0
while command != "End":
    index = int(command)
    if index < 0 or index >= len(targets):
        command = input()
        continue
    current_target = targets.pop(index)
    targets.insert(index, -1)
    # if targets[index] > -1:
    for i in range(0, len(targets)):
        if targets[i] > current_target and targets[i] > -1:
            targets[i] -= current_target
        elif current_target >= targets[i] > -1:
            targets[i] += current_target
    # targets[index] = -1
    shot_targets += 1
    command = input()
print(f"Shot targets: {shot_targets} -> {' '.join(map(str,targets))}")

