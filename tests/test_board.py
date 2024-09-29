import unittest
from game.board import Board
from game.pieces.rook import Rook
from game.pieces.pawn import Pawn
from game.exceptions import PieceNotFound, InvalidMove, OutOfBoard

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()

    def test_str_board(self):
        expected_str = (
            "  a b c d e f g h\n"
            "8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"
            "7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . . . . . \n"
            "3 . . . . . . . . \n"
            "2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
            "1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"
        )
        self.assertEqual(str(self.__board__), expected_str)

    def test_initialization(self):
        # Verifica las piezas en las filas iniciales
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(1, 0), Pawn)
        # Verifica que las posiciones intermedias estén vacías
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.__board__.get_piece(row, col))

    def test_out_of_board(self):
        with self.assertRaises(OutOfBoard):
            self.__board__.get_piece(8, 0)

    def test_move_piece_out_of_board(self):
        with self.assertRaises(OutOfBoard):
            self.__board__.mover_pieza(8, 0, 3, 0)  # Origen fuera del tablero
        with self.assertRaises(OutOfBoard):
            self.__board__.mover_pieza(0, 8, 3, 0)  # Origen fuera del tablero

    def test_move_piece(self):
        self.__board__.mover_pieza(1, 0, 3, 0)
        self.assertIsInstance(self.__board__.get_piece(3, 0), Pawn)
        self.assertIsNone(self.__board__.get_piece(1, 0))

        with self.assertRaises(PieceNotFound):
            self.__board__.mover_pieza(1, 0, 3, 0)  # Intenta mover un peón que no existe

        self.__board__.set_piece(2, 0, Pawn("WHITE", self.__board__))  # Coloca un peón blanco en (2, 0)
        with self.assertRaises(InvalidMove):
            self.__board__.mover_pieza(3, 0, 2, 0)  # Intenta capturar su propio peón

    def test_get_piece(self):
        piece = self.__board__.get_piece(0, 0)  # Debe ser una torre negra
        self.assertIsInstance(piece, Rook)
        self.assertEqual(piece.get_color(), "BLACK")

        with self.assertRaises(OutOfBoard):
            self.__board__.get_piece(-1, 0)  # Fila fuera de rango
        with self.assertRaises(OutOfBoard):
            self.__board__.get_piece(8, 0)  # Fila fuera de rango

if __name__ == "__main__":
    unittest.main()
