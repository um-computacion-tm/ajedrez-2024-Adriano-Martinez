import unittest
from game.pieces.piece import Piece
from game.board import Board  

class TestPiece(unittest.TestCase):
    
    def setUp(self):
        self.board = Board()  
        self.piece = Piece("white", self.board)  

    def test_get_color(self):
        self.assertEqual(self.piece.get_color(), "white")
    
    def test_str(self):
        self.assertEqual(str(self.piece), "")
    
    def test_mov_correcto(self):
        with self.assertRaises(NotImplementedError):
            self.piece.mov_correcto(0, 0, 1, 1)

if __name__ == "__main__":
    unittest.main()