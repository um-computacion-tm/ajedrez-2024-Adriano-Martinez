import unittest
from pieces.knight import Knight
from exceptions import InvalidMoveKnightMove
from board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.knight_white = Knight("WHITE", self.board)
        self.knight_black = Knight("BLACK", self.board)

        # Configurar la posición inicial de los caballos
        self.board.set_piece(4, 4, self.knight_white)
        self.board.set_piece(6, 5, self.knight_black)

    def test_valid_move(self):
        # Prueba movimientos válidos
        try:
            self.assertTrue(self.knight_white.mov_correcto(4, 4, 6, 5))
        except InvalidMoveKnightMove:
            self.fail("mov_correcto levantó InvalidMoveKnightMove inesperadamente!")

    def test_invalid_move(self):
        # Prueba movimientos inválidos
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 5, 5)

    def test_capture_opponent(self):
        # Configurar una pieza del oponente en la posición destino
        self.board.set_piece(6, 5, self.knight_black)
        self.assertTrue(self.knight_white.mov_correcto(4, 4, 6, 5))

    def test_capture_own_piece(self):
        # Configurar una pieza propia en la posición destino
        self.board.set_piece(6, 5, self.knight_white)
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 6, 5)

if __name__ == '__main__':
    unittest.main()