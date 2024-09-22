import unittest
from board import Board
from pieces.queen import Queen
from exceptions import InvalidMoveQueenMove

class TestQueen(unittest.TestCase):
    def setUp(self):
     self.board = Board()  # Inicializa un nuevo tablero
     self.queen_white = Queen("WHITE", self.board)  # Crea una reina blanca
     self.board.set_piece(3, 3, self.queen_white)  # Coloca la reina en d4

    def test_valid_vertical_move(self):
     for row in range(4, 7):  # Verifica filas 4, 5, 6
        self.board.set_piece(row, 3, None)  
     self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  # d4 a d8

    def test_valid_horizontal_move(self):
        # Asegura que el camino esté despejado para un movimiento horizontal
        self.board.set_piece(3, 7, None)  # Limpia cualquier pieza en d8 (3, 7)
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 3, 7))  # Verifica el movimiento horizontal (d4 a d8)

    def test_valid_diagonal_move(self):
        # Asegura que el camino esté despejado para un movimiento diagonal
        self.board.set_piece(6, 6, None)  # Limpia cualquier pieza en g7 (6, 6)
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 6, 6))  # Verifica el movimiento diagonal (d4 a g7)

    def test_capture_move(self):
        # Coloca una pieza enemiga en la posición 7, 3 (h4)
        enemy_piece = Queen("BLACK", self.board)
        self.board.set_piece(7, 3, enemy_piece)

        # Limpia cualquier otra pieza en el camino
        self.board.set_piece(4, 3, None)
        self.board.set_piece(5, 3, None)
        self.board.set_piece(6, 3, None)

        # Verifica que la reina blanca puede capturar la pieza enemiga
        self.assertTrue(self.queen_white.mov_correcto(3, 3, 7, 3))  

    def test_no_capture_own_piece(self):
    # Coloca una pieza amiga (reina blanca) en h4 (7, 3)
     friendly_piece = Queen("WHITE", self.board)
     self.board.set_piece(7, 3, friendly_piece)

    # La reina blanca no debería poder moverse a la posición de su propia pieza
     with self.assertRaises(InvalidMoveQueenMove):
        self.queen_white.mov_correcto(3, 3, 7, 3)  

if __name__ == "__main__":
    unittest.main()
