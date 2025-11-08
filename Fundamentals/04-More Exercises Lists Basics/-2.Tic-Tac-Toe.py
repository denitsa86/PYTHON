#You will receive a field of a tic-tac-toe game in three lines containing numbers separated by a single space.
# •	0 - empty space
# •	1 - first player move
# •	2 - second player move
# Find out who the winner is. If the first player wins print "First player won",
# # otherwise if the second player wins print "Second player won", otherwise print "Draw!"
# 2 0 1
# 0 1 0
# 1 0 2
row_one = input().split()
row_two = input().split()
row_three = input().split()
has_winner = False
if row_one[0] == row_one[1] == row_one[2] == 1 or row_two[0] == row_two[1] == row_two[2] == 1 or row_three[0] == row_three[1] == row_three[2] == 1:
        print("First player won")

#     elif row_one[i] == row_one[i] == row_one[i] == 2:
#         print("Second player won")
#         break
# for i in range(len(row_two)):
#     if row_two[i] == row_two[i] == row_two[i] == 1:
#         print("First player won")
#         break
#     elif row_two[i] == row_two[i] == row_two[i] == 2:
#         print("Second player won")
#         break
# for i in range(len(row_three)):
#     if row_three[i] == row_three[i] == row_three[i] == 1:
#         print("First player won")
#         break
#     elif row_three[i] == row_three[i] == row_three[i] == 2:
#         print("Second player won")
#         break



