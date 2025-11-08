#You will receive a number n and a word. On the next n lines you will be given some strings. You have to
# add them in a list and print them. After that you have to filter out only the strings that include the
# given word and print that list too.
number = int(input())
word = input()
mylist = []
for i in range(number):
    entry = input()
    mylist.append(entry)
new_list = []
for x in mylist:
  if word in x:
     new_list.append(x)
print(mylist)
print(new_list)