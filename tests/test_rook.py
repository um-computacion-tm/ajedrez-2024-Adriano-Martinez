import unittest
from game.pieces.rook import Rook
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestRook(unittest.TestCase):
    """
    Clase de prueba para la clase Rook (torre). Utiliza la biblioteca unittest 
    para verificar el comportamiento y la funcionalidad de las torres en el juego.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Inicializa un nuevo tablero 
        y coloca una torre blanca en la posición a1 (7, 0). Despeja el camino 
        para permitir movimientos ortogonales.
        """
        self.__board__ = Board()  # Crea un nuevo tablero
        self.__white_rook__ = Rook("WHITE", self.__board__)  # Crea una torre blanca
        self.__board__.set_piece(0, 0, self.__white_rook__)  # Coloca la torre en a1

        # Limpia el camino para los movimientos ortogonales
        for col in range(1, 8):  # Despeja la fila a
            self.__board__.set_piece(0, col, None)
        for row in range(1, 8):  # Despeja la columna 1
            self.__board__.set_piece(row, 0, None)

    def test_valid_vertical_move(self):
        """
        Prueba que la torre puede realizar un movimiento vertical permitido 
        """
        self.assertTrue(self.__white_rook__.mov_correcto(0, 0, 7, 0))

    def test_valid_horizontal_move(self):
        """
        Prueba que la torre puede realizar un movimiento horizontal permitido 
        """
        self.assertTrue(self.__white_rook__.mov_correcto(0, 0, 0, 7))

    def test_mov_with_obstacles(self):
        """
        Prueba que la torre no puede moverse a través de piezas enemigas o aliadas.
        """
        # Bloquear movimiento con una pieza enemiga
        self.__board__.set_piece(0, 3, Rook("BLACK", self.__board__))  # Coloca una torre enemiga en d1
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre a una posición bloqueada."):
            self.__white_rook__.mov_correcto(0, 0, 0, 7)  # a1 a h1 (bloqueado por d1)

        # Bloquear movimiento con una pieza amiga
        self.__board__.set_piece(3, 0, Rook("WHITE", self.__board__))  # Coloca una torre amiga en a4
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre a una posición ocupada por su propia pieza."):
            self.__white_rook__.mov_correcto(0, 0, 7, 0)  # a1 a a8 (bloqueado por a4)

    def test_invalid_move_no_piece(self):
        """
        Prueba que se lanza un InvalidPieceMove si se intenta mover una torre 
        que no está en el tablero (tablero vacío).
        """
        empty_board = Board()  # Crea un tablero vacío
        empty_rook = Rook("WHITE", empty_board)  
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover una torre que no está en el tablero."):
            empty_rook.mov_correcto(0, 0, 0, 7)  # Intentar mover sin la torre en el tablero

    def test_invalid_diagonal_move(self):
        """
        Prueba que se lanza un InvalidPieceMove al intentar mover la torre 
        en diagonal, lo cual no es un movimiento válido para la torre 
        """
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre en diagonal."):
            self.__white_rook__.mov_correcto(0, 0, 7, 7)

    def test_no_move(self):
        """
        Prueba que se lanza un InvalidPieceMove al intentar mover la torre 
        a la misma posición.
        """
        with self.assertRaises(InvalidPieceMove, msg="Se esperaba un error al intentar mover la torre a la misma posición."):
            self.__white_rook__.mov_correcto(0, 0, 0, 0)

if __name__ == "__main__":
    unittest.main()
