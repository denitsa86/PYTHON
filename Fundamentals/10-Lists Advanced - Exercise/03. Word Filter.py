#Using comprehension, write a program that receives some text, separated by space, and takes only
# those words whose length is even. Print each word on a new line.
#kiwi orange banana apple
words = input().split()
even_words = [word for word in words if len(word) % 2 == 0]
print("\n".join(even_words))