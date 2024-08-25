import unittest
from pieces.rook import Rook

class TestRook(unittest.TestCase):

     def setUp(self):
        # Inicializa dos instancias de Rook, una blanca y una negra
        self.white_rook = Rook("WHITE")
        self.black_rook = Rook("BLACK")

     def test_str(self):
        # Verifica que el método __str__ devuelva el símbolo correcto
        self.assertEqual(str(self.white_rook), "♖")
        self.assertEqual(str(self.black_rook), "♜")
    
     def test_mov_correcto(self):
        self.assertTrue(self.white_rook.mov_correcto(0, 0, 0, 7))  # Mov vertical
        self.assertTrue(self.white_rook.mov_correcto(0, 0, 7, 0))  # Mov horizontal
        
    


     
        
    

