# буква	   a	e	i	o	u
# стойност	1	2	3	4	5
word = input()
sum = 0
for i in range(0, len(word)):
    letter = word[i]
    match letter:
        case 'a':
            sum += 1
        case "e":
            sum += 2
        case "i":
            sum += 3
        case "o":
            sum += 4
        case "u":
            sum += 5
print(sum)
