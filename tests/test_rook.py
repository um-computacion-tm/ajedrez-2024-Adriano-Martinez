import unittest
from game.pieces.rook import Rook
from game.board import Board
from game.exceptions import InvalidMoveRookMove

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_rook = Rook("WHITE", self.board)
        self.board.set_piece(0, 0, self.white_rook)
        
        # Limpia el camino para los movimientos
        for col in range(1, 8):
            self.board.set_piece(0, col, None)
        for row in range(1, 8):
            self.board.set_piece(row, 0, None)

    def test_mov_correcto(self):
        # Movimiento vertical permitido
        self.assertTrue(self.white_rook.mov_correcto(0, 0, 0, 7))
        # Movimiento horizontal permitido
        self.assertTrue(self.white_rook.mov_correcto(0, 0, 7, 0))

    def test_mov_correcto_with_obstacles(self):
        # Bloquear movimiento con otra pieza
        self.board.set_piece(0, 3, Rook("BLACK", self.board))  
        with self.assertRaises(InvalidMoveRookMove):
            self.white_rook.mov_correcto(0, 0, 0, 7)

        # Bloquear movimiento con una pieza propia
        self.board.set_piece(3, 0, Rook("WHITE", self.board))  
        with self.assertRaises(InvalidMoveRookMove):
            self.white_rook.mov_correcto(0, 0, 7, 0)

    def test_invalid_move_no_piece(self):  
        empty_board = Board()  # Crea un tablero vacío
        empty_rook = Rook("WHITE", empty_board)  
        with self.assertRaises(InvalidMoveRookMove):
            empty_rook.mov_correcto(0, 0, 0, 7)  # No hay pieza en el tablero vacío

    def test_invalid_diagonal_move(self):
        # Movimiento diagonal no permitido
        with self.assertRaises(InvalidMoveRookMove):
            self.white_rook.mov_correcto(0, 0, 7, 7)

    def test_no_move(self):
        # Verifica que no se permite mover a la misma posición
        with self.assertRaises(InvalidMoveRookMove):
            self.white_rook.mov_correcto(0, 0, 0, 0)

if __name__ == "__main__":
    unittest.main()

        
    

