import unittest
from pieces.knight import Knight
from board import Board
from exceptions import InvalidMoveKnightMove

class TestKnight(unittest.TestCase):

    def setUp(self):
        # Inicializa el tablero y las piezas
        self.board = Board()
        self.knight_white = Knight("WHITE", self.board)
        self.knight_black = Knight("BLACK", self.board)
        self.board.set_piece(4, 4, self.knight_white)  
        self.board.set_piece(6, 5, self.knight_black)  

    def test_valid_move(self):
        # Movimiento en 'L' válido del caballo blanco 
        self.assertTrue(self.knight_white.mov_correcto(4, 4, 6, 5))

        # movimiento en 'L' válido del caballo negro
        self.assertTrue(self.knight_black.mov_correcto(6, 5, 4, 4))

    def test_invalid_move(self):
        # Intenta un movimiento inválido 
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 5, 5)  

    def test_capture_opponent(self):
        # Verifica que el caballo puede capturar una pieza del otro color
        self.board.set_piece(6, 5, self.knight_black)  
        self.assertTrue(self.knight_white.mov_correcto(4, 4, 6, 5))  

    def test_capture_own_piece(self):
        # Intenta capturar una pieza del mismo color 
        another_knight_white = Knight("WHITE", self.board)
        self.board.set_piece(6, 5, another_knight_white)  
        with self.assertRaises(InvalidMoveKnightMove):
            self.knight_white.mov_correcto(4, 4, 6, 5)  

if __name__ == '__main__':
    unittest.main()
