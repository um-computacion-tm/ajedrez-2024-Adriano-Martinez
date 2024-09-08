import unittest
from pieces.queen import Queen
from board import Board
from exceptions import InvalidMoveQueenMove

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen_white = Queen("WHITE", self.board)
        self.queen_black = Queen("BLACK", self.board)

    def test_valid_horizontal_move(self):
        # Test movimiento horizontal válido
        self.assertTrue(self.queen_white.mov_correcto(4, 4, 4, 7))

    def test_valid_vertical_move(self):
        # Test movimiento vertical válido
        self.assertTrue(self.queen_white.mov_correcto(4, 4, 7, 4))

    def test_valid_diagonal_move(self):
        # Test movimiento diagonal válido
        self.assertTrue(self.queen_white.mov_correcto(4, 4, 7, 7))

    def test_invalid_move(self):
        # Test movimiento no válido
        with self.assertRaises(InvalidMoveQueenMove):
            self.queen_white.mov_correcto(4, 4, 5, 6)

    def test_path_blocked(self):
        # Test cuando el camino está bloqueado
        self.board.set_piece(5, 4, Queen("BLACK", self.board))
        with self.assertRaises(InvalidMoveQueenMove):
            self.queen_white.mov_correcto(4, 4, 7, 4)

    def test_path_clear(self):
        # Test cuando el camino está despejado
        self.assertTrue(self.queen_white.mov_correcto(4, 4, 7, 4))

if __name__ == "__main__":
    unittest.main()