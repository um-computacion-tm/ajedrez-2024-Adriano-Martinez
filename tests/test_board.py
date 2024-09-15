import unittest
from board import Board
from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()

    def test_str_board(self):
        board = Board()
        self.assertEqual(str(board),
            "  a b c d e f g h\n"
            "8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ \n"  # Espacio después del último símbolo
            "7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ \n"
            "6 . . . . . . . . \n"
            "5 . . . . . . . . \n"
            "4 . . . . . . . . \n"
            "3 . . . . . . . . \n"
            "2 ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ \n"
            "1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ \n"  # Espacio después del último símbolo
        )

# Verifica las piezas negras en la fila 0
    def test_initialization(self):
        self.assertIsInstance(self.__board__.get_piece(0, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(0, 1), Knight)
        self.assertIsInstance(self.__board__.get_piece(0, 2), Bishop)
        self.assertIsInstance(self.__board__.get_piece(0, 3), Queen)
        self.assertIsInstance(self.__board__.get_piece(0, 4), King)
        self.assertIsInstance(self.__board__.get_piece(0, 5), Bishop)
        self.assertIsInstance(self.__board__.get_piece(0, 6), Knight)
        self.assertIsInstance(self.__board__.get_piece(0, 7), Rook)

# Verifica los peones negros en la fila 1
        for col in range(8):
            self.assertIsInstance(self.__board__.get_piece(1, col), Pawn)

# Verifica las piezas blancas en la fila 7
        self.assertIsInstance(self.__board__.get_piece(7, 0), Rook)
        self.assertIsInstance(self.__board__.get_piece(7, 1), Knight)
        self.assertIsInstance(self.__board__.get_piece(7, 2), Bishop)
        self.assertIsInstance(self.__board__.get_piece(7, 3), Queen)
        self.assertIsInstance(self.__board__.get_piece(7, 4), King)
        self.assertIsInstance(self.__board__.get_piece(7, 5), Bishop)
        self.assertIsInstance(self.__board__.get_piece(7, 6), Knight)
        self.assertIsInstance(self.__board__.get_piece(7, 7), Rook)

# Verifica los peones blancos en la fila 6
        for col in range(8):
            self.assertIsInstance(self.__board__.get_piece(6, col), Pawn)

# Verifica que las posiciones intermedias están vacías
        for row in range(2, 6):
            for col in range(8):
                self.assertIsNone(self.__board__.get_piece(row, col))


if __name__ == "__main__":
    unittest.main()
