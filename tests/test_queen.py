import unittest
from board import Board
from pieces.queen import Queen
from exceptions import InvalidMoveQueenMove

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen_white = Queen("WHITE", self.board)
        self.queen_black = Queen("BLACK", self.board)
        self.board.set_piece(3, 3, self.queen_white)

    def test_valid_vertical_move(self):
        # Asegura que no haya piezas que bloqueen el movimiento
        self.board.set_piece(6, 3, None)  
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  #

    def test_valid_horizontal_move(self):
        self.board.set_piece(3, 6, None)  # Asegura de que no haya piezas en la fila 4
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 3, 7))  

    def test_valid_diagonal_move(self):
        self.board.set_piece(6, 6, None)  # Asegura de que no haya piezas en la diagonal
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 6, 6))  

    def test_capture_move(self):
    # Coloca una pieza enemiga en la posición 7, 3
     enemy_piece = Queen("BLACK", self.board)
     self.board.set_piece(7, 3, enemy_piece)

    # Asegura de que no haya piezas bloqueando el camino
     self.board.set_piece(4, 3, None)
     self.board.set_piece(5, 3, None)
     self.board.set_piece(6, 3, None)

    # Verifica que la reina puede moverse y capturar la pieza enemiga
     self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  


    def test_no_capture_own_piece(self):
        friendly_piece = Queen("WHITE", self.board)
        self.board.set_piece(7, 3, friendly_piece)
        with self.assertRaises(InvalidMoveQueenMove):
            self.queen_white.mov_correcto(3, 3, 7, 3)  

    def test_path_clear(self):
        # Asegura que el camino esté despejado para un movimiento vertical
        self.board.set_piece(5, 3, None)
        self.board.set_piece(6, 3, None)
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  

if __name__ == "__main__":
    unittest.main()
