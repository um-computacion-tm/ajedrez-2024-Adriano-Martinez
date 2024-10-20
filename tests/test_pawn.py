import unittest
from game.pieces.pawn import Pawn
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestPawn(unittest.TestCase):
    
    def setUp(self):
        """Configura el tablero y los peones negro y blanco antes de cada prueba."""
        self.__board__ = Board()
        self.__black_pawn__ = Pawn("BLACK", self.__board__)
        self.__white_pawn__ = Pawn("WHITE", self.__board__)

    def test_initial_black(self):
        """Verifica las posiciones posibles de un peón negro en su posición inicial (f7)."""
        possibles = self.__black_pawn__.get_possible_positions(1, 5)  # Peón negro en f7
        self.assertEqual(possibles, [(2, 5), (3, 5)])  # Puede moverse de f7 a af6 y f5

    def test_not_initial_black(self):
        """Verifica las posiciones posibles de un peón negro que no está en su posición inicial (f6)."""
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en f6
        self.assertEqual(possibles, [(3, 5)])  # Puede moverse de f6 a f7

    def test_eat_left_black(self):
        """Verifica que un peón negro puede capturar una pieza blanca en la izquierda."""
        self.__board__.set_piece(3, 6, Pawn("WHITE", self.__board__))  # Coloca un peón blanco en g5
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en f6
        self.assertEqual(possibles, [(3, 5), (3, 6)])  # Puede avanzar o capturar

    def test_eat_right_black(self):
        """Verifica que un peón negro puede capturar una pieza blanca en la derecha."""
        self.__board__.set_piece(3, 4, Pawn("WHITE", self.__board__))  # Coloca un peón blanco en c4
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5), (3, 4)])  # Puede avanzar o capturar

    def test_initial_white(self):
        """Verifica las posiciones posibles de un peón blanco en su posición inicial (b7)."""
        possibles = self.__white_pawn__.get_possible_positions(6, 4)  # Peón blanco en b7
        self.assertEqual(possibles, [(5, 4), (4, 4)])  # Puede moverse de b7 a b6 y b5

    def test_not_initial_white(self):
        """Verifica las posiciones posibles de un peón blanco que no está en su posición inicial (b6)."""
        possibles = self.__white_pawn__.get_possible_positions(5, 4)  # Peón blanco en b6
        self.assertEqual(possibles, [(4, 4)])  # Puede moverse de b6 a b5

    def test_not_initial_white_block(self):
        """Verifica que un peón blanco no puede moverse si hay una pieza propia bloqueando su camino."""
        self.__board__.set_piece(4, 4, Pawn("BLACK", self.__board__))  # Bloqueo por pieza propia en b5
        possibles = self.__white_pawn__.get_possible_positions(5, 4)  # Peón blanco en b6
        self.assertEqual(possibles, [])  # No puede moverse

    def test_not_initial_black_block(self):
        """Verifica que un peón negro no puede moverse si hay una pieza propia bloqueando su camino."""
        self.__board__.set_piece(5, 4, Pawn("BLACK", self.__board__))  # Bloqueo por pieza propia en b5
        possibles = self.__black_pawn__.get_possible_positions(4, 4)  # Peón negro en b5
        self.assertEqual(possibles, [])  # No puede moverse

    def test_invalid_moves(self):
        """Verifica que un peón no puede moverse hacia atrás ni capturar su propia pieza."""
        # Verificar movimientos hacia atrás
        with self.assertRaises(InvalidPieceMove):
            self.__black_pawn__.mov_correcto(4, 4, 3, 4)  # Movimiento hacia atrás no válido
            self.__white_pawn__.mov_correcto(4, 4, 5, 4)  # Movimiento hacia atrás no válido

        # Intentar capturar su propia pieza
        self.__board__.set_piece(3, 6, Pawn("BLACK", self.__board__))  # Coloca un peón negro en b4
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5)])  # No puede capturar su propia pieza

    def test_invalid_move(self):
        """Verifica que un peón no puede moverse fuera de los límites del tablero."""
        # Intentar mover el peón a una posición fuera del tablero
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(0, 0, -1, -1)  # Movimiento fuera de los límites
            self.__white_pawn__.mov_correcto(0, 0, 8, 8)    # Movimiento fuera de los límites
            self.__white_pawn__.mov_correcto(6, 1, 6, 8)    # Movimiento a una posición inválida en la fila

    def test_diagonal_capture_valid(self):
        """Verifica que un peón blanco puede capturar diagonalmente a un peón negro."""
        self.__board__.set_piece(5, 3, Pawn("BLACK", self.__board__))  # Coloca una pieza negra 
        self.assertTrue(self.__white_pawn__.mov_correcto(6, 4, 5, 3))  # Movimiento válido (captura diagonal)

    def test_diagonal_capture_invalid_friendly_piece(self):
        """Verifica que un peón blanco no puede capturar a su propia pieza."""
        self.__board__.set_piece(5, 3, Pawn("WHITE", self.__board__))  # Coloca una pieza blanca 
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 4, 5, 3)  # Movimiento inválido (no puede capturar a su propia pieza)

    def test_invalid_vertical_move_with_piece_in_path(self):
        """Verifica que un peón blanco no puede moverse verticalmente si hay una pieza en su camino."""
        self.__board__.set_piece(5, 1, Pawn("BLACK", self.__board__))  # Coloca una pieza negra en b3
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 1, 5, 1)  # Movimiento inválido (no puede pasar por encima de otra pieza)

    def test_invalid_diagonal_move_without_capture(self):
        """Verifica que un peón blanco no puede moverse diagonalmente sin capturar una pieza."""
        self.__board__.set_piece(5, 2, Pawn("WHITE", self.__board__))  # Coloca una pieza blanca 
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 1, 5, 2)  # Movimiento inválido (no puede capturar a su propia pieza)

    def test_move_out_of_bounds(self):
        """Verifica que un peón blanco no puede moverse a una posición fuera de los límites del tablero."""
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 1, 7, 1)  # Movimiento inválido (fuera de los límites)

    def test_invalid_move_to_non_capture_position(self):
        """Verifica que un peón blanco no puede moverse a una posición no válida sin captura."""
        board = Board()
        pawn = Pawn("WHITE", board)

        # Intentar hacer un movimiento no válido para el peon.
        with self.assertRaises(InvalidPieceMove):
            pawn.mov_correcto(5, 1, 6, 1)  # Movimiento inválido 

    def test_white_pawn_move_forward(self):
        """Verifica que un peón blanco puede moverse hacia adelante."""
        self.__board__.set_piece(6, 1, self.__white_pawn__)  # Coloca un peón blanco 
        self.assertTrue(self.__white_pawn__.mov_correcto(6, 1, 5, 1))  # Movimiento válido 
    
    def test_black_pawn_move_forward(self):
        """Verifica que un peón negro puede moverse hacia adelante."""
        self.__board__.set_piece(1, 0, self.__black_pawn__)  # Coloca un peón negro 
        self.assertTrue(self.__black_pawn__.mov_correcto(1, 0, 2, 0))  # Movimiento válido 

if __name__ == "__main__":
    unittest.main()
