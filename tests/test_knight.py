import unittest
from pieces.knight import Knight
from exceptions import InvalidMoveKnightMove
from board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.knight_white = Knight("WHITE", self.board)
        self.knight_black = Knight("BLACK", self.board)
        self.board.set_piece(4, 4, self.knight_white)
        self.board.set_piece(6, 5, self.knight_black)

    def test_str(self):
        self.assertEqual(str(self.knight_white), "♘")
        self.assertEqual(str(self.knight_black), "♞")

    def test_valid_move(self):
        try:
            self.assertTrue(self.knight_white.mov_correcto(4, 4, 6, 5))
            self.assertTrue(self.knight_white.mov_correcto(4, 4, 5, 6))
            self.assertTrue(self.knight_white.mov_correcto(4, 4, 3, 2))
            self.assertTrue(self.knight_white.mov_correcto(4, 4, 2, 3))
        except InvalidMoveKnightMove:
            self.fail("mov_correcto levantó InvalidMoveKnightMove inesperadamente!")

    def test_invalid_move(self):
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 5, 5)
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 7, 8)

    def test_capture_opponent(self):
        self.board.set_piece(6, 5, self.knight_black)
        self.assertTrue(self.knight_white.mov_correcto(4, 4, 6, 5))

    def test_capture_own_piece(self):
        self.board.set_piece(6, 5, self.knight_white)
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 6, 5)

    def test_get_possible_positions(self):
        expected_positions = [
            (6, 5), (6, 3), (5, 6), (5, 2),
            (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        possible_positions = self.knight_white.get_possible_positions(4, 4)
        self.assertCountEqual(possible_positions, expected_positions)

    def test_move_at_board_edges(self):
        # Prueba movimientos válidos en los bordes del tablero
        try:
            self.assertTrue(self.knight_white.mov_correcto(0, 0, 2, 1))
            self.assertTrue(self.knight_white.mov_correcto(7, 7, 5, 6))
        except InvalidMoveKnightMove:
            self.fail("mov_correcto levantó InvalidMoveKnightMove inesperadamente!")

        # Prueba movimientos inválidos en los bordes del tablero
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(0, 0, 0, 1)  # Movimiento no en forma de L

    def test_invalid_move_out_of_bounds(self):
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(0, 0, -1, -1)

if __name__ == '__main__':
    unittest.main()