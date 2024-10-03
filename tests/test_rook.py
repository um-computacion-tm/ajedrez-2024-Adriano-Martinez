import unittest
from game.pieces.rook import Rook
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestRook(unittest.TestCase):
    def setUp(self):
        self.__board__ = Board()  # Crea un nuevo tablero
        self.__white_rook__ = Rook("WHITE", self.__board__)  # Crea una torre blanca
        self.__board__.set_piece(0, 0, self.__white_rook__)  # Coloca la torre en a1

        # Limpia el camino para los movimientos ortogonales
        for col in range(1, 8):  # Despeja la fila a
            self.__board__.set_piece(0, col, None)
        for row in range(1, 8):  # Despeja la columna 1
            self.__board__.set_piece(row, 0, None)

    def test_valid_vertical_move(self):
        # Movimiento vertical permitido (a1 a a8)
        self.assertTrue(self.__white_rook__.mov_correcto(0, 0, 7, 0))

    def test_valid_horizontal_move(self):
        # Movimiento horizontal permitido (a1 a h1)
        self.assertTrue(self.__white_rook__.mov_correcto(0, 0, 0, 7))

    def test_mov_with_obstacles(self):
        # Bloquear movimiento con una pieza enemiga
        self.__board__.set_piece(0, 3, Rook("BLACK", self.__board__))  # Coloca una torre enemiga en d1
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre a una posición bloqueada."):
            self.__white_rook__.mov_correcto(0, 0, 0, 7)  # a1 a h1 (bloqueado por d1)

        # Bloquear movimiento con una pieza amiga
        self.__board__.set_piece(3, 0, Rook("WHITE", self.__board__))  # Coloca una torre amiga en a4
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre a una posición ocupada por su propia pieza."):
            self.__white_rook__.mov_correcto(0, 0, 7, 0)  # a1 a a8 (bloqueado por a4)

    def test_invalid_move_no_piece(self):
        empty_board = Board()  # Crea un tablero vacío
        empty_rook = Rook("WHITE", empty_board)  
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover una torre que no está en el tablero."):
            empty_rook.mov_correcto(0, 0, 0, 7)  # Intentar mover sin la torre en el tablero

    def test_invalid_diagonal_move(self):
        # Movimiento diagonal no permitido (a1 a h8)
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre en diagonal."):
            self.__white_rook__.mov_correcto(0, 0, 7, 7)

    def test_no_move(self):
        # No se puede mover a la misma posición (a1 a a1)
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre a la misma posición."):
            self.__white_rook__.mov_correcto(0, 0, 0, 0)

if __name__ == "__main__":
    unittest.main()

