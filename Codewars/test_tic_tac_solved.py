import unittest
from tic_tac_solved import is_solved

class TestTicTacToe(unittest.TestCase):
    def test_not_finished_board(self):
        board = [
            [0, 0, 1],
            [0, 1, 2],
            [2, 1, 0]
        ]
        result = is_solved(board)
        self.assertEqual(result, -1)

    def test_player_x_wins(self):
        board = [
            [1, 0, 1],
            [0, 1, 2],
            [2, 1, 1]
        ]
        result = is_solved(board)
        self.assertEqual(result, 1)

    def test_player_o_wins(self):
        board = [
            [1, 2, 2],
            [0, 2, 0],
            [2, 1, 1]
        ]
        result = is_solved(board)
        self.assertEqual(result, 2)

    def test_cats_game(self):
        board = [
            [1, 2, 1],
            [2, 1, 1],
            [1, 1, 2]
        ]
        result = is_solved(board)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
