import unittest
from game.pieces.piece import Piece
from game.board import Board  

class TestPiece(unittest.TestCase):
    
    def setUp(self):
        self.__board__ = Board()  
        self.__piece__ = Piece("white", self.__board__)  

    def test_get_color(self):
        self.assertEqual(self.__piece__.get_color(), "white")
    
    def test_str(self):
        self.assertEqual(str(self.__piece__), "")
    
    def test_mov_correcto(self):
        # Probar que se lanza NotImplementedError para movimientos no implementados
        with self.assertRaises(NotImplementedError):
            self.__piece__.mov_correcto(0, 0, 1, 1)

    def test_mov_correcto_invalid_position(self):
        # Probar movimiento inválido por posiciones fuera de rango
        self.assertFalse(self.__piece__.mov_correcto(-1, 0, 1, 1))  # from_x es inválido
        self.assertFalse(self.__piece__.mov_correcto(0, 0, 8, 1))  # to_x es inválido

    def test_mov_correcto_same_position(self):
        # Probar que si el origen y destino son iguales, devuelve False
        self.assertFalse(self.__piece__.mov_correcto(0, 0, 0, 0))

    def test_is_position_valid(self):
        self.assertTrue(Piece.is_position_valid(0, 0))
        self.assertTrue(Piece.is_position_valid(7, 7))
        self.assertFalse(Piece.is_position_valid(-1, 0))
        self.assertFalse(Piece.is_position_valid(8, 8))
    
    def test_valid_positions(self):
        self.__board__.set_piece(0, 1, None)
        self.assertTrue(self.__piece__.valid_positions(0, 0, 0, 1))
        self.assertFalse(self.__piece__.valid_positions(0, 0, 7, 7))

    def test_scan_direction(self):
        self.__board__.set_piece(1, 0, None)
        possibles = self.__piece__.scan_direction(0, 0, 1, 0)
        self.assertIn((1, 0), possibles)

        enemy_piece = Piece("black", self.__board__)
        self.__board__.set_piece(2, 0, enemy_piece)
        possibles = self.__piece__.scan_direction(0, 0, 1, 0)
        self.assertIn((2, 0), possibles)

        ally_piece = Piece("white", self.__board__)
        self.__board__.set_piece(3, 0, ally_piece)
        possibles = self.__piece__.scan_direction(0, 0, 1, 0)
        self.assertNotIn((3, 0), possibles)

if __name__ == "__main__":
    unittest.main()