import unittest
from game.pieces.knight import Knight
from game.exceptions import InvalidPieceMove
from game.board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()
        self.__knight_white__ = Knight("WHITE", self.__board__)
        self.__knight_black__ = Knight("BLACK", self.__board__)
        self.__board__.set_piece(4, 4, self.__knight_white__)
        self.__board__.set_piece(6, 5, self.__knight_black__)

    def test_str(self):
        self.assertEqual(str(self.__knight_white__), "♘")
        self.assertEqual(str(self.__knight_black__), "♞")

    def test_valid_move(self):
        try:
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 6, 5))
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 5, 6))
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 3, 2))
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 2, 3))
        except InvalidPieceMove:
            self.fail("mov_correcto levantó InvalidPieceMove inesperadamente!")

    def test_invalid_move(self):
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(4, 4, 5, 5)
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(4, 4, 7, 8)

    def test_capture_opponent(self):
        self.__board__.set_piece(6, 5, self.__knight_black__)
        self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 6, 5))

    def test_capture_own_piece(self):
        self.__board__.set_piece(6, 5, self.__knight_white__)
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(4, 4, 6, 5)

    def test_get_possible_positions(self):
        expected_positions = [
            (6, 5), (6, 3), (5, 6), (5, 2),
            (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        possible_positions = self.__knight_white__.get_possible_positions(4, 4)
        self.assertCountEqual(possible_positions, expected_positions)

    def test_move_at_board_edges(self):
        # Prueba movimientos válidos en los bordes del tablero
        try:
            self.assertTrue(self.__knight_white__.mov_correcto(0, 0, 2, 1))
            self.assertTrue(self.__knight_white__.mov_correcto(7, 7, 5, 6))
        except InvalidPieceMove:
            self.fail("mov_correcto levantó InvalidPieceMove inesperadamente!")

        # Prueba movimientos inválidos en los bordes del tablero
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(0, 0, 0, 1)  # Movimiento no en forma de L

    def test_invalid_move_out_of_bounds(self):
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(0, 0, -1, -1)

if __name__ == '__main__':
    unittest.main()
