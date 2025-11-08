#You are at the zoo and the meerkats look strange. You will receive 3 strings: (tail, body, head).
# You have to re-arrange the elements in a list, so that the animal looks normal again: (head, body, tail)
tail = input()
body = input()
head = input()
meerkats = [tail,body,head]
meerkats[0], meerkats[2] = meerkats[2], meerkats[0]
print(meerkats)

