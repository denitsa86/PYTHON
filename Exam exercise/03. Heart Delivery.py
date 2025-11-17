#string with even integers, separated by a "@". After that, a series of Jump commands will follow
# until you receive "Love!".
#Cupid starts at the position of the first house (index 0) and must jump by a given length. The jump
# commands will be in this format: "Jump {length}".
#Every time he jumps from one house to another, the needed hearts for the house are decreased by 2:
# •	If the needed hearts for a certain house become equal to 0, print on the console
# "Place {house_index} has Valentine's day."
# •	If Cupid jumps to a house where the needed hearts are already 0, print on the console
# "Place {house_index} already had Valentine's day."
# •	Keep in mind that Cupid can have a larger jump length than the size of the neighborhood, and if
# he does jump outside of it, he should start from the first house again (index 0).
neighbourhood = list(map(int,input().split("@")))
command = input()
failed_houses = 0
last_index = 0
while command != "Love!":
    command = command.split()
    length = int(command[1])
    if 0 < length + last_index >= len(neighbourhood):
        length = 0
        last_index = 0
    if neighbourhood[length + last_index] == 0:
        print(f"Place {length + last_index} already had Valentine's day.") # !!!
    else:
        neighbourhood[length + last_index] -= 2
        if neighbourhood[length + last_index] <= 0:
            print(f"Place {length + last_index} has Valentine's day.")
    last_index += length

    command = input()
print(f"Cupid's last position was {last_index}.")
if sum(neighbourhood) == 0:
    print("Mission was successful.")
else:
    for item in neighbourhood:
        if item > 0:
            failed_houses += 1
    print(f"Cupid has failed {failed_houses} places.")
