import unittest
from game.board import Board
from game.pieces.queen import Queen
from game.exceptions import InvalidPieceMove

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()  # Inicializa un nuevo tablero
        self.__queen_white__ = Queen("WHITE", self.__board__)  # Crea una reina blanca
        self.__board__.set_piece(3, 3, self.__queen_white__)  # Coloca la reina en d4

    def test_valid_vertical_move(self):
        # Verifica que el camino esté despejado para un movimiento vertical
        for row in range(4, 8):  # Despeja las filas 4, 5, 6, 7 en la columna d (columna 3)
            self.__board__.set_piece(row, 3, None)
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 7, 3))  # d4 a d8

    def test_valid_horizontal_move(self):
        # Verifica que el camino esté despejado para un movimiento horizontal
        for col in range(4, 8):  # Despeja las columnas 4 a 7 en la fila d4 (fila 3)
            self.__board__.set_piece(3, col, None)
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 3, 7))  # d4 a h4

    def test_valid_diagonal_move(self):
        # Verifica que el camino esté despejado para un movimiento diagonal
        for i in range(1, 4):  # Despeja las posiciones diagonales d4 a g7
            self.__board__.set_piece(3 + i, 3 + i, None)
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 6, 6))  # d4 a g7

    def test_capture_move(self):
        # Coloca una pieza enemiga en la posición h4 (7, 3)
        enemy_piece = Queen("BLACK", self.__board__)
        self.__board__.set_piece(7, 3, enemy_piece)

        # Limpia cualquier otra pieza en el camino
        for row in range(4, 7):
            self.__board__.set_piece(row, 3, None)

        # Verifica que la reina blanca puede capturar la pieza enemiga
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 7, 3))  # d4 a h4, captura

    def test_no_capture_own_piece(self):
        # Coloca una pieza amiga (reina blanca) en h4 (7, 3)
        friendly_piece = Queen("WHITE", self.__board__)
        self.__board__.set_piece(7, 3, friendly_piece)

        # La reina blanca no debería poder moverse a la posición de su propia pieza
        with self.assertRaises(InvalidPieceMove):
            self.__queen_white__.mov_correcto(3, 3, 7, 3)  # d4 a h4, no debería permitir mover
    
    def test_out_of_bounds_move(self):
        # La Reina intenta moverse fuera de los límites del tablero
        with self.assertRaises(InvalidPieceMove):
            self.__queen_white__.mov_correcto(3, 3, 8, 3)  # Movimiento fuera del tablero (d4 a d9 no es válido)
    
    def test_blocked_move(self):
        # Coloca una pieza en el camino de la Reina en d5 (4, 3)
        blocking_piece = Queen("BLACK", self.__board__)
        self.__board__.set_piece(4, 3, blocking_piece)

        # La Reina no debería poder moverse a d6 (5, 3) porque está bloqueada en d5
        with self.assertRaises(InvalidPieceMove):
            self.__queen_white__.mov_correcto(3, 3, 5, 3)  # d4 a d6 está bloqueado


if __name__ == "__main__":
    unittest.main()
