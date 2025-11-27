#receives info from the console about people and their phone numbers. Each entry should have
# a name and a number (both strings) separated by a "-". If you receive a name that already
# exists in the phonebook, update its number. you will receive a number – N.
# Your program should be able to perform a search of contact by name and print its details
# in the format: "{name} -> {number}". In case the contact isn't found, print:
# "Contact {name} does not exist."

data = input()   #Adam-0888080808
address_book = {}
while "-" in data:
    address_info = data.split("-")
    name = address_info[0]
    number = address_info[1]
    address_book[name] = number

    data = input()
calls = int(data)
for calls in range(calls):
    searched_name = input()
    if searched_name not in address_book:
        print(f"Contact {searched_name} does not exist.")
    else:
        print(f"{searched_name} -> {address_book[searched_name]}")

