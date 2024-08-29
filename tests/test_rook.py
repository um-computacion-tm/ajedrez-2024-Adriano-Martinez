import unittest
from pieces.rook import Rook
from board import Board
from exceptions import InvalidMoveRookMove

class TestRook(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.white_rook = Rook("WHITE", self.board)
        self.board.set_piece(0, 0, self.white_rook)
        # Limpiar las posiciones a lo largo de la fila 0 y la columna 0 para el test
        for col in range(1, 8):
            self.board.set_piece(0, col, None)
        for row in range(1, 8):
            self.board.set_piece(row, 0, None)

    def test_mov_correcto(self):
        self.assertTrue(self.white_rook.mov_correcto(0, 0, 0, 7))  # Movimiento vertical permitido
        self.assertTrue(self.white_rook.mov_correcto(0, 0, 7, 0))  # Movimiento horizontal permitido

    def test_mov_correcto_with_obstacles(self):
        self.board.set_piece(0, 3, Rook("BLACK", self.board))  # Colocar una pieza negra en el camino
        with self.assertRaises(InvalidMoveRookMove):
            self.white_rook.mov_correcto(0, 0, 0, 7)  # Movimiento bloqueado por otra pieza

    def test_invalid_move_no_piece(self):
        empty_board = Board()  # Crear un tablero vacío
        empty_rook = Rook("WHITE", empty_board)  # Crear una torre blanca para un tablero vacío
        with self.assertRaises(InvalidMoveRookMove):
            empty_rook.mov_correcto(0, 0, 0, 7)  # Movimiento desde una posición sin pieza

if __name__ == "__main__":
    unittest.main()
     
        
    

