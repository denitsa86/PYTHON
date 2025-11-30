#validates a parking place - users can register to enter the park and unregister to leave.
# The program receives 2 types of commands:
# •	"register {username} {license_plate_number}":
# o	The system only supports one car per user at the moment, so if a user tries to register another
# license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
# o	If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# •	"unregister {username}":
# o	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# o	If the check above passes successfully, the system should print:
# "{username} unregistered successfully"
# After you execute all of the commands, print all the currently registered users and their license
# plates in the format:
# •	"{username} => {license_plate_number}"

count = int(input())
visitors = {}
for _ in range(count):
    data = input().split()
    action = data[0]
    username = data[1]
    if action == "register":
        plate_number = data[2]
        if username not in visitors:
            visitors[username] = plate_number
            print(f"{username} registered {plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {plate_number}")
    elif action == "unregister":
        if username not in visitors:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del visitors[username]

#•	"{username} => {license_plate_number}"
for username, plate_number in visitors.items():
    print(f"{username} => {plate_number}")