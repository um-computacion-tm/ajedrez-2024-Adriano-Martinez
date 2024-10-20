import unittest
from game.pieces.knight import Knight
from game.exceptions import InvalidPieceMove
from game.board import Board

class TestKnight(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de prueba antes de cada método de prueba."""
        self.__board__ = Board()
        self.__knight_white__ = Knight("WHITE", self.__board__)
        self.__knight_black__ = Knight("BLACK", self.__board__)
        self.__board__.set_piece(4, 4, self.__knight_white__)  # Coloca el caballo blanco
        self.__board__.set_piece(6, 5, self.__knight_black__)  # Coloca el caballo negro

    def test_str(self):
        """Verifica que la representación en cadena del caballo blanco y negro sea correcta."""
        self.assertEqual(str(self.__knight_white__), "♘")
        self.assertEqual(str(self.__knight_black__), "♞")

    def test_valid_move(self):
        """Verifica que los movimientos válidos en forma de L del caballo sean aceptados."""
        try:
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 6, 5))  # Movimiento válido
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 5, 6))  # Movimiento válido
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 3, 2))  # Movimiento válido
            self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 2, 3))  # Movimiento válido
        except InvalidPieceMove:
            self.fail("mov_correcto levantó InvalidPieceMove inesperadamente!")

    def test_invalid_move(self):
        """Verifica que se levante InvalidPieceMove para movimientos no válidos."""
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(4, 4, 5, 5)  # Movimiento no en forma de L
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(4, 4, 7, 8)  # Movimiento fuera de rango

    def test_capture_opponent(self):
        """Verifica que el caballo pueda capturar a una pieza del oponente."""
        self.__board__.set_piece(6, 5, self.__knight_black__)  # Coloca el caballo negro
        self.assertTrue(self.__knight_white__.mov_correcto(4, 4, 6, 5))  # Movimiento válido para capturar

    def test_capture_own_piece(self):
        """Verifica que el caballo no pueda moverse a una posición ocupada por su propia pieza."""
        self.__board__.set_piece(6, 5, self.__knight_white__)  # Coloca otra pieza blanca
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(4, 4, 6, 5)  # Movimiento no válido

    def test_invalid_move_shape(self):
        """Verifica que un movimiento en forma de L hacia una posición ocupada por una pieza del mismo color sea rechazado."""
        self.__board__.set_piece(3, 3, self.__knight_white__)  # Coloca otra pieza blanca
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(5, 2, 3, 3)  # Movimiento no válido

    def test_get_possible_positions(self):
        """Verifica que las posiciones posibles de movimiento del caballo sean correctas."""
        expected_positions = [
            (6, 5), (6, 3), (5, 6), (5, 2),
            (3, 6), (3, 2), (2, 5), (2, 3)
        ]
        possible_positions = self.__knight_white__.get_possible_positions(4, 4)
        self.assertCountEqual(possible_positions, expected_positions)

    def test_move_at_board_edges(self):
        """Prueba movimientos válidos e inválidos en los bordes del tablero."""
        try:
            self.assertTrue(self.__knight_white__.mov_correcto(0, 0, 2, 1))  # Movimiento válido
            self.assertTrue(self.__knight_white__.mov_correcto(7, 7, 5, 6))  # Movimiento válido
        except InvalidPieceMove:
            self.fail("mov_correcto levantó InvalidPieceMove inesperadamente!")

        # Prueba movimientos inválidos en los bordes del tablero
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(0, 0, 0, 1)  # Movimiento no en forma de L

    def test_invalid_move_out_of_bounds(self):
        """Verifica que se levante InvalidPieceMove para movimientos fuera de los límites del tablero."""
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(0, 0, -1, -1)

    def test_invalid_move_shape_not_l(self):
        """Prueba un movimiento que no sigue el patrón en forma de L."""
        with self.assertRaises(InvalidPieceMove):
            self.__knight_white__.mov_correcto(5, 2, 4, 2)  # Movimiento no válido (una posición hacia adelante)

if __name__ == "__main__":
    unittest.main()
