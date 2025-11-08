#create board
def create_board(rows,cols): # 3, 3
    game_board = []
    for _ in range(rows):
        game_board.append(['_'] * cols)
    return game_board

# Print the board
def print_board(game_board):
    print("  012")
    #print rows
    for i in range(rows):
        print(f"{i} {''.join(game_board[i])}")

#check for win
def check_winner(game_board):
# Rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]
# Diagonals
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    return None


rows = 3
columns = 3
#initiate players
board = create_board(rows,columns)
player = ""
playerX = "X"
playerO = "O"
player_turn = 0
while player_turn < 9:
    print_board(board)
    if player_turn % 2 == 0:
        player = playerX
    else:
        player = playerO
# player is selecting position on the board
    print(f"Hello, {player}! Please choose your move by selecting your position:")
    while True:
        try:
            player_row = int(input("Choose a row (from 0 to 2): "))
            if 0 <= player_row <= 2:
                break  # valid input, exit loop
            else:
                # number out of range
                print("Row must be between 0 and 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
    while True:
        try:
            player_col = int(input("Choose a column (from 0 to 2): "))
            if 0 <= player_col <= 2:
                break
            else:
                print("Column must be between 0 and 2. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
# position already occupied
    if board[player_row][player_col] != '_':
        print(f"This position is already occupied. Choose another position!")
        continue
# player`s move is documented on the board
    else:
        if player == playerX:
            board[player_row][player_col] = 'X'
        elif player == playerO:
            board[player_row][player_col] = 'O'

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"Player {winner} wins!")
        break
    player_turn += 1

if check_winner(board) is None:
    print_board(board)
    print("Nobody wins!")



