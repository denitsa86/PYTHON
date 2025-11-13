import unittest

from tictactoe import TicTacToe
from unittest.mock import patch

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_create_board(self):
        game = TicTacToe()
        expected_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        self.assertEqual(game.board, expected_board)

    def test_check_winner_row(self):
        game = TicTacToe()
        game.board = [
            ['X', 'X', 'X'],
            ['_', 'O', '_'],
            ['_', '_', 'O']
        ]
        self.assertEqual(game.check_winner(), 'X')

if __name__ == "__main__":
    unittest.main()
