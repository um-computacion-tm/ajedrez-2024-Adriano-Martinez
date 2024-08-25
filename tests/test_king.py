import unittest
from pieces.king import King

class TestKing(unittest.TestCase):

     def setUp(self):
        self.white_king = King("WHITE")
        self.black_king = King("BLACK")

     def test_str(self):
        self.assertEqual(str(self.white_king), "♔")
        self.assertEqual(str(self.black_king), "♚")

     
     def test_mov_correcto(self):
        self.assertTrue(self.white_king.mov_correcto(4, 4, 4, 5))  # Mov vertical
        self.assertTrue(self.white_king.mov_correcto(4, 4, 5, 4))  # Mov horizontal
        self.assertTrue(self.white_king.mov_correcto(4, 4, 5, 5))  # Mov diagonal