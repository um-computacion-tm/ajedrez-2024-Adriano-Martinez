import unittest
from game.pieces.bishop import Bishop
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.__board__ = Board()  # Crea un tablero 
        self.__white_bishop__ = Bishop("WHITE", self.__board__)
        self.__black_bishop__ = Bishop("BLACK", self.__board__)

        # Posiciona los obispos y vacia algunas casillas
        self.__board__.set_piece(4, 4, self.__white_bishop__)
        self.__board__.set_piece(2, 2, None)
        self.__board__.set_piece(6, 6, None)
        self.__board__.set_piece(6, 2, None)
        self.__board__.set_piece(2, 6, None)

    def test_str(self):
        self.assertEqual(str(self.__white_bishop__), "♗")
        self.assertEqual(str(self.__black_bishop__), "♝")

    def test_mov_correcto(self):
        # Movimiento diagonal válido
        self.assertTrue(self.__white_bishop__.mov_correcto(4, 4, 6, 6))
        self.assertTrue(self.__white_bishop__.mov_correcto(4, 4, 2, 2))
        self.assertTrue(self.__white_bishop__.mov_correcto(4, 4, 6, 2))
        self.assertTrue(self.__white_bishop__.mov_correcto(4, 4, 2, 6))

        # Movimiento no válido 
        with self.assertRaises(InvalidPieceMove):
            self.__white_bishop__.mov_correcto(4, 4, 4, 5)  # Movimiento no diagonal

        # Movimiento bloqueado por pieza rival
        self.__board__.set_piece(5, 5, Bishop("BLACK", self.__board__))  
        with self.assertRaises(InvalidPieceMove):
            self.__white_bishop__.mov_correcto(4, 4, 6, 6)

        # Movimiento bloqueado por pieza propia
        self.__board__.set_piece(5, 5, Bishop("WHITE", self.__board__))  
        with self.assertRaises(InvalidPieceMove):
            self.__white_bishop__.mov_correcto(4, 4, 6, 6)

    def test_get_possible_positions(self):
        expected_positions = [
            (3, 3), (2, 2), (1, 1), 
            (3, 5), (2, 6), (1, 7),
            (5, 3), (6, 2), (5, 5), (6, 6)
        ]
        possible_positions = self.__white_bishop__.get_possible_positions(4, 4)
        self.assertCountEqual(possible_positions, expected_positions)

    def test_invalid_moves(self):
        # Intenta moverce a posiciones no válidas
        with self.assertRaises(InvalidPieceMove):
            self.__white_bishop__.mov_correcto(4, 4, 5, 4)  # Movimiento no diagonal
        with self.assertRaises(InvalidPieceMove):
            self.__white_bishop__.mov_correcto(4, 4, 4, 5)  # Movimiento no diagonal

if __name__ == "__main__":
    unittest.main()
