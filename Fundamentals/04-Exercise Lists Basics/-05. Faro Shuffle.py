#split exactly in half and then the cards in the two halves are perfectly interwoven, such that the original bottom card is still on the bottom and the original top card is still on top.
# For example, faro shuffling the list
# ['ace', 'two', 'three', 'four', 'five', 'six'] once, gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a
# number of faro shuffles that have to be made. Print the state of the deck after the shuffle.
# a b c d| e f g h
#['a', 'c', 'e', 'g',| 'b', 'd', 'f', 'h']
# 5
start_deck =input().split()
shuffles = int(input())
left_half = []
right_half = []
for shuffles in range(shuffles):
    shuffled_deck = []
    slicing_index = int(len(start_deck) / 2)
    left_half = start_deck[0 : slicing_index]
    right_half = start_deck[slicing_index::]
    for i in range(len(left_half)):
        shuffled_deck.append(left_half[i])
        shuffled_deck.append(right_half[i])
    start_deck = shuffled_deck
print(start_deck)

