import unittest
from pieces.bishop import Bishop
from board import Board
from exceptions import InvalidMoveBishopMove

class TestBishop(unittest.TestCase):

    def setUp(self):
        self.board = Board()  # Crea un tablero 
        self.white_bishop = Bishop("WHITE", self.board)
        self.black_bishop = Bishop("BLACK", self.board)

        
        self.board.set_piece(4, 4, self.white_bishop)
        self.board.set_piece(2, 2, None)
        self.board.set_piece(6, 6, None)
        self.board.set_piece(6, 2, None)
        self.board.set_piece(2, 6, None)

    def test_str(self):
        self.assertEqual(str(self.white_bishop), "♗")
        self.assertEqual(str(self.black_bishop), "♝")

    def test_mov_correcto(self):
        # Movimiento diagonal válido
        self.assertTrue(self.white_bishop.mov_correcto(4, 4, 6, 6))
        self.assertTrue(self.white_bishop.mov_correcto(4, 4, 2, 2))
        self.assertTrue(self.white_bishop.mov_correcto(4, 4, 6, 2))
        self.assertTrue(self.white_bishop.mov_correcto(4, 4, 2, 6))

        # Movimiento no válido 
        with self.assertRaises(InvalidMoveBishopMove):
            self.white_bishop.mov_correcto(4, 4, 4, 5)  # Movimiento vertical

        # Movimiento bloqueado por otra pieza
        self.board.set_piece(5, 5, Bishop("BLACK", self.board))  
        with self.assertRaises(InvalidMoveBishopMove):
            self.white_bishop.mov_correcto(4, 4, 6, 6)  



