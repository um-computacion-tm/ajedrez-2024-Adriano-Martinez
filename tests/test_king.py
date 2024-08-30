import unittest
from pieces.king import King
from board import Board
from exceptions import InvalidMoveKingMove

class TestKing(unittest.TestCase): 

    def setUp(self):
        self.board = Board()  
        self.white_king = King("WHITE", self.board)  
        self.black_king = King("BLACK", self.board)  
        self.board.set_piece(4, 4, self.white_king)  

    def test_str(self):
        self.assertEqual(str(self.white_king), "♔")
        self.assertEqual(str(self.black_king), "♚")

    def test_valid_moves(self):
        # Verificar movimientos válidos
        self.assertTrue(self.white_king.mov_correcto(4, 4, 4, 5))  # Movimiento vertical hacia arriba
        self.assertTrue(self.white_king.mov_correcto(4, 4, 4, 3))  # Movimiento vertical hacia abajo
        self.assertTrue(self.white_king.mov_correcto(4, 4, 5, 4))  # Movimiento horizontal hacia la derecha
        self.assertTrue(self.white_king.mov_correcto(4, 4, 3, 4))  # Movimiento horizontal hacia la izquierda
        self.assertTrue(self.white_king.mov_correcto(4, 4, 5, 5))  # Movimiento diagonal hacia abajo derecha
        self.assertTrue(self.white_king.mov_correcto(4, 4, 3, 3))  # Movimiento diagonal hacia arriba izquierda

    def test_invalid_moves(self):
     
        with self.assertRaises(InvalidMoveKingMove):
            self.white_king.mov_correcto(4, 4, 6, 4)  # Movimiento vertical de dos casillas
        
        with self.assertRaises(InvalidMoveKingMove):
            self.white_king.mov_correcto(4, 4, 4, 6)  # Movimiento horizontal de dos casillas
        
        with self.assertRaises(InvalidMoveKingMove):
            self.white_king.mov_correcto(4, 4, 6, 6)  # Movimiento diagonal de dos casillas

    def test_blocked_by_own_piece(self):
        
        self.board.set_piece(5, 4, King("WHITE", self.board))  
        with self.assertRaises(InvalidMoveKingMove):
            self.white_king.mov_correcto(4, 4, 5, 4)  

    

if __name__ == "__main__":
    unittest.main()