import unittest

from pieces.piece import Piece

class TestPiece(unittest.TestCase):
    
    def setUp(self):
        self.piece = Piece("white")

    def test_get_color(self):
        self.assertEqual(self.piece.get_color(), "white")
    
    def test_str(self):
        self.assertEqual(str(self.piece), "")
    
    def test_mov_correcto(self):
        with self.assertRaises(NotImplementedError):
            self.piece.mov_correcto(0, 0, 1, 1)

if __name__ == "__main__":
    unittest.main()