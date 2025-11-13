import unittest

from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_create_board(self):
        game = TicTacToe()
        expected_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.assertEqual(game.board, expected_board)

    def test_check_winner(self):
        game = TicTacToe()
        game.board = [
            ['X', 'X', 'X'],
            ['_', 'O', '_'],
            ['_', '_', 'O']
        ]
        self.assertEqual(game.check_winner(), 'X')

    def test_check_winner_diagonal(self):
        game = TicTacToe()
        game.board = [
            ['O', 'X', 'X'],
            ['X', 'O', '_'],
            ['_', '_', 'O']
        ]
        self.assertEqual(game.check_winner(), 'O')

    def test_no_winner(self):
        game = TicTacToe()
        game.board = [
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O']
        ]
        self.assertIsNone(game.check_winner())

    def test_is_playerX(self):
        self.game.player_turn = 0
        self.assertEqual(self.game.get_current_player(), "X")

    def test_is_playerO(self):
        self.game.player_turn = 1
        self.assertEqual(self.game.get_current_player(), "O")

    def test_is_position_free(self):
        self.assertTrue(self.game.is_position_free(0, 0))

    def test_is_position_occupied(self):
        self.game.board[0][0] = 'X'
        self.assertFalse(self.game.is_position_free(0, 0))


if __name__ == "__main__":
    unittest.main()
