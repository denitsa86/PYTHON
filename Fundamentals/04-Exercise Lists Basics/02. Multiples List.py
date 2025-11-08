#Write a program that receives two numbers (factor and count) and creates a list with length of the given
# count and contains only elements that are multiples of the given factor.
factor = int(input())
count = int(input())
multiples=[]
#multiples = [factor * i for i in range(1, count + 1)]
for i in range(1, count + 1):
    multiples.append(factor * i)
print(multiples)