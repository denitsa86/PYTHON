class TicTacToe:
    def __init__(self, rows=3, cols=3):
        self.rows = rows
        self.cols = cols
        self.board = self.create_board()
        self.playerX = "X"
        self.playerO = "O"
        self.player_turn = 0


# create board
    def create_board(self):  # 3, 3
        game_board = []
        for _ in range(self.rows):
            game_board.append(['_'] * self.cols)
        return game_board


# Print the board
    def print_board(self):
        print("  012")
        # print rows
        for i in range(self.rows):
            print(f"{i} {''.join(self.board[i])}")


# check for win
    def check_winner(self):
        # Rows and columns
        board = self.board
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


    def validate_input(self, prompt, min_value=0, max_value=2):
        while True:
            try:
                value = int(input(prompt))
                if min_value <= value <= max_value:
                    return value
                else:
                    print(f"Value must be between {min_value} and {max_value}. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def play_game(self):
        for turn in range(9):
            self.print_board()
            # player = self.playerX if self.player_turn % 2 == 0 else self.playerO
            if self.player_turn % 2 == 0:
                player = self.playerX
            else:
                player = self.playerO
            # player is selecting position on the board
            print(f"Hello, {player}! Please choose your move by selecting your position:")
            player_row = self.validate_input("Choose a row (from 0 to 2): ")
            player_col = self.validate_input("Choose a column (from 0 to 2): ")

            if self.board[player_row][player_col] != '_':
                print(f"This position is already occupied. Choose another position!")
                continue
            # player`s move is documented on the board
            else:
                if player == self.playerX:
                    self.board[player_row][player_col] = 'X'
                elif player == self.playerO:
                    self.board[player_row][player_col] = 'O'
            winner = self.check_winner()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                return
            self.player_turn += 1

        self.print_board()
        print("Nobody wins!")

if __name__ == "__main__":
    TicTacToe().play_game()
