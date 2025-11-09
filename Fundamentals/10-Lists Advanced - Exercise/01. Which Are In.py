#You will be given two sequences of strings, separated by ", ". Print a new list containing
# only the strings from the first input line, which are substrings of any string in the second
criteria = input().split(", ") # arp, live, strong
words = input().split(", ") # lively, alive, harp, sharp, armstrong
substrings = []

for i in range(len(criteria)):
    for word in words:
        if criteria[i] in word:
            substrings.append(criteria[i])

#[res.append(val) for val in a if val not in res]
result = []
[result.append(val) for val in substrings if val not in result]
print(result)
