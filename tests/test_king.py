import unittest
from pieces.king import King
from board import Board


class TestKing(unittest.TestCase): 

    def setUp(self):
        self.board = Board()  
        self.white_king = King("WHITE", self.board)  
        self.black_king = King("BLACK", self.board)  

    def test_str(self):
        self.assertEqual(str(self.white_king), "♔")
        self.assertEqual(str(self.black_king), "♚")

    def test_mov_correcto(self):
        self.assertTrue(self.white_king.mov_correcto(4, 4, 4, 5))  # Movimiento vertical
        self.assertTrue(self.white_king.mov_correcto(4, 4, 5, 4))  # Movimiento horizontal
        self.assertTrue(self.white_king.mov_correcto(4, 4, 5, 5))  # Movimiento diagonal