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
        with self.assertRaises(NotImplementedError):
            self.__piece__.mov_correcto(0, 0, 1, 1)

if __name__ == "__main__":
    unittest.main()