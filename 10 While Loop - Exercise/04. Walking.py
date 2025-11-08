#цел да върви 10 000 стъпки всеки ден. Някои дни обаче е много уморена от работа и ще иска да се прибере
# преди да постигне целта си. Напишете програма, която чете от конзолата по колко стъпки изминава тя
# всеки път като излиза през деня и когато постигне целта си да се изписва "Goal reached! Good job!" и
# колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките, които
# е извървяла докато се прибира. След което, ако не е успяла да постигне целта си, на конзолата трябва
# да се изпише: "{разликата между стъпките} more steps to reach goal."
goal = 10000
total_steps = 0
current_steps = input()
while current_steps.isdigit():
    total_steps += int(current_steps)
    if total_steps >= goal:
        break
    else:
        current_steps = input()
if current_steps == "Going home":
        current_steps = input()
        total_steps += int(current_steps)
if total_steps >= goal:
    print("Goal reached! Good job!")
    print(f"{total_steps - goal} steps over the goal!")
else:
    print(f"{goal - total_steps} more steps to reach goal.")


