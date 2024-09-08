import unittest
from board import Board
from pieces.queen import Queen
from exceptions import InvalidMoveQueenMove

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen_white = Queen("WHITE", self.board)
        self.queen_black = Queen("BLACK", self.board)
        # Colocar la reina blanca en D4 (posición 3, 3)
        self.board.set_piece(3, 3, self.queen_white)

    def test_valid_vertical_move(self):
        # Asegurar que no haya piezas que bloqueen el movimiento
        self.board.set_piece(6, 3, None)  # Asegurarse de que no haya piezas en la columna D
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  # Movimiento de D4 a D8

    def test_valid_horizontal_move(self):
        self.board.set_piece(3, 6, None)  # Asegurarse de que no haya piezas en la fila 4
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 3, 7))  # Movimiento de D4 a H4

    def test_valid_diagonal_move(self):
        self.board.set_piece(6, 6, None)  # Asegurarse de que no haya piezas en la diagonal
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 6, 6))  # Movimiento de D4 a G7

    def test_capture_move(self):
    # Colocar una pieza enemiga en D8 (posición 7, 3)
     enemy_piece = Queen("BLACK", self.board)
     self.board.set_piece(7, 3, enemy_piece)

    # Asegurarse de que no haya piezas bloqueando el camino de D4 a D8
     self.board.set_piece(4, 3, None)
     self.board.set_piece(5, 3, None)
     self.board.set_piece(6, 3, None)

    # Verificar que la reina puede moverse y capturar la pieza enemiga
     self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  # Movimiento de captura de D4 a D8


    def test_no_capture_own_piece(self):
        # Colocar una pieza propia en D8 (posición 7, 3)
        friendly_piece = Queen("WHITE", self.board)
        self.board.set_piece(7, 3, friendly_piece)
        with self.assertRaises(InvalidMoveQueenMove):
            self.queen_white.mov_correcto(3, 3, 7, 3)  # Intento de capturar una pieza propia

    def test_path_clear(self):
        # Asegurar que el camino esté despejado para un movimiento vertical
        self.board.set_piece(5, 3, None)
        self.board.set_piece(6, 3, None)
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  # Movimiento de D4 a D8

if __name__ == "__main__":
    unittest.main()
