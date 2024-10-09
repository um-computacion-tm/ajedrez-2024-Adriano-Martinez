import unittest
from game.pieces.pawn import Pawn
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestPawn(unittest.TestCase):
    
    def setUp(self):
        self.__board__ = Board()
        self.__black_pawn__ = Pawn("BLACK", self.__board__)
        self.__white_pawn__ = Pawn("WHITE", self.__board__)

    def test_initial_black(self):
        possibles = self.__black_pawn__.get_possible_positions(1, 5)  # Peón negro en a2
        self.assertEqual(possibles, [(2, 5), (3, 5)])  # Puede moverse de a2 a a3 y a4

    def test_not_initial_black(self):
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5)])  # Puede moverse de a3 a a4

    def test_eat_left_black(self):
        self.__board__.set_piece(3, 6, Pawn("WHITE", self.__board__))  # Coloca un peón blanco en b4
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5), (3, 6)])  # Puede avanzar o capturar

    def test_eat_right_black(self):
        self.__board__.set_piece(3, 4, Pawn("WHITE", self.__board__))  # Coloca un peón blanco en c4
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5), (3, 4)])  # Puede avanzar o capturar

    def test_initial_white(self):
        possibles = self.__white_pawn__.get_possible_positions(6, 4)  # Peón blanco en b7
        self.assertEqual(possibles, [(5, 4), (4, 4)])  # Puede moverse de b7 a b6 y b5

    def test_not_initial_white(self):
        possibles = self.__white_pawn__.get_possible_positions(5, 4)  # Peón blanco en b6
        self.assertEqual(possibles, [(4, 4)])  # Puede moverse de b6 a b5

    def test_not_initial_white_block(self):
        self.__board__.set_piece(4, 4, Pawn("BLACK", self.__board__))  # Bloqueo por pieza propia en b5
        possibles = self.__white_pawn__.get_possible_positions(5, 4)  # Peón blanco en b6
        self.assertEqual(possibles, [])  # No puede moverse

    def test_not_initial_black_block(self):
        self.__board__.set_piece(5, 4, Pawn("BLACK", self.__board__))  # Bloqueo por pieza propia en b5
        possibles = self.__black_pawn__.get_possible_positions(4, 4)  # Peón negro en b5
        self.assertEqual(possibles, [])  # No puede moverse

    def test_invalid_moves(self):
        # Verificar movimientos hacia atrás
        with self.assertRaises(InvalidPieceMove):
            self.__black_pawn__.mov_correcto(4, 4, 3, 4)  # Movimiento hacia atrás no válido
            self.__white_pawn__.mov_correcto(4, 4, 5, 4)  # Movimiento hacia atrás no válido

        # Intentar capturar su propia pieza
        self.__board__.set_piece(3, 6, Pawn("BLACK", self.__board__))  # Coloca un peón negro en b4
        possibles = self.__black_pawn__.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5)])  # No puede capturar su propia pieza

    def test_invalid_move(self):
        # Intentar mover el peón a una posición fuera del tablero
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(0, 0, -1, -1)  # Movimiento fuera de los límites
            self.__white_pawn__.mov_correcto(0, 0, 8, 8)    # Movimiento fuera de los límites
            self.__white_pawn__.mov_correcto(6, 1, 6, 8)    # Movimiento a una posición inválida en la fila

    def test_diagonal_capture_valid(self):
        self.__board__.set_piece(5, 3, Pawn("BLACK", self.__board__))  # Coloca una pieza negra en c6
        self.assertTrue(self.__white_pawn__.mov_correcto(6, 4, 5, 3))  # Movimiento válido (captura diagonal)

    def test_diagonal_capture_invalid_friendly_piece(self):
        self.__board__.set_piece(5, 3, Pawn("WHITE", self.__board__))  # Coloca una pieza blanca en c6
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 4, 5, 3)  # Movimiento inválido (no puede capturar a su propia pieza)

    def test_invalid_vertical_move_with_piece_in_path(self):
        self.__board__.set_piece(5, 1, Pawn("BLACK", self.__board__))  # Coloca una pieza negra en b3
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 1, 5, 1)  # Movimiento inválido (no puede pasar por encima de otra pieza)

    def test_invalid_diagonal_move_without_capture(self):
        self.__board__.set_piece(5, 2, Pawn("WHITE", self.__board__))  # Coloca una pieza blanca en c3
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 1, 5, 2)  # Movimiento inválido (no puede capturar a su propia pieza)

    def test_move_out_of_bounds(self):
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(6, 1, 7, 1)  # Movimiento inválido (fuera de los límites)

    def test_invalid_move_to_non_capture_position(self):
        board = Board()
        pawn = Pawn("WHITE", board)

        # Intentar mover el peón de b2 a b4, que es un movimiento no permitido
        with self.assertRaises(InvalidPieceMove):
            pawn.mov_correcto(5, 1, 6, 1)  # Movimiento inválido de b2 a b4

    def test_white_pawn_move_forward(self):
        self.__board__.set_piece(6, 1, self.__white_pawn__)  # Coloca un peón blanco en b2
        self.assertTrue(self.__white_pawn__.mov_correcto(6, 1, 5, 1))  # Movimiento válido a b3
    
    def test_black_pawn_move_forward(self):
        self.__board__.set_piece(1, 0, self.__black_pawn__)  # Coloca un peón negro en a7
        self.assertTrue(self.__black_pawn__.mov_correcto(1, 0, 2, 0))  # Movimiento válido a a6

    def test_diagonal_capture_valid_again(self):
        self.__board__.set_piece(4, 1, self.__white_pawn__)  
        self.__board__.set_piece(3, 2, Pawn("BLACK", self.__board__))  # Coloca un peón negro en c5
        
        # Verifica que el peón blanco puede capturar al negro
        self.assertTrue(self.__white_pawn__.mov_correcto(4, 1, 3, 2))  # Movimiento válido (captura diagonal)

    def test_diagonal_capture_invalid_friendly_piece_again(self):
        self.__board__.set_piece(4, 1, Pawn("WHITE", self.__board__))  # Coloca una pieza blanca en b4
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(5, 2, 4, 1)  # Movimiento inválido (no puede capturar a su propia pieza) c5 a b4

    def test_diagonal_capture_invalid_empty_square(self):
        self.__board__.set_piece(4, 1, self.__white_pawn__)  
        # Intentar mover el peón de b4 a c5 (movimiento diagonal sin captura)
        with self.assertRaises(InvalidPieceMove):
            self.__white_pawn__.mov_correcto(4, 1, 3, 2)  # Debería lanzar excepción

if __name__ == "__main__":
    unittest.main()

