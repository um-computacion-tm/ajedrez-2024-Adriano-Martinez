import unittest
from game.pieces.pawn import Pawn
from game.board import Board
from game.exceptions import InvalidPieceMove

class TestPawn(unittest.TestCase):

    def test_initial_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)  # Peón negro en a2
        self.assertEqual(possibles, [(2, 5), (3, 5)])  # Puede moverse de a2 a a3 y a4

    def test_not_initial_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5)])  # Puede moverse de a3 a a4

    def test_eat_left_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))  # Coloca un peón blanco en b4

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5), (3, 6)])  # Puede avanzar de a3 a a4 o capturar de a3 a b4

    def test_eat_right_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 4, Pawn("WHITE", board))  # Coloca un peón blanco en c4

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5), (3, 4)])  # Puede avanzar de a3 a a4 o capturar de a3 a c4

    def test_initial_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)  # Peón blanco en b7
        self.assertEqual(possibles, [(5, 4), (4, 4)])  # Puede moverse de b7 a b6 y b5

    def test_not_initial_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(5, 4)  # Peón blanco en b6
        self.assertEqual(possibles, [(4, 4)])  # Puede moverse de b6 a b5

    def test_not_initial_white_block(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, Pawn("BLACK", board))  # Bloqueo por pieza propia en b5

        possibles = pawn.get_possible_positions(5, 4)  # Peón blanco en b6
        self.assertEqual(possibles, [])  # No puede moverse

    def test_not_initial_black_block(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        board.set_piece(5, 4, Pawn("BLACK", board))  # Bloqueo por pieza propia en b5

        possibles = pawn.get_possible_positions(4, 4)  # Peón negro en b5
        self.assertEqual(possibles, [])  # No puede moverse

    def test_eat_left_black_no_piece(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5)])  # No puede capturar porque no hay pieza; puede moverse de a3 a a4

    def test_eat_right_black_no_piece(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro en a3
        self.assertEqual(possibles, [(3, 5)])  # No puede capturar porque no hay pieza; puede moverse de a3 a a4

    def test_move_backwards_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        with self.assertRaises(InvalidPieceMove):
            pawn.mov_correcto(4, 4, 3, 4)  # Movimiento hacia atrás no válido de a4 a a3

    def test_move_backwards_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)

        with self.assertRaises(InvalidPieceMove):
            pawn.mov_correcto(4, 4, 5, 4)  # Movimiento hacia atrás no válido de b6 a b5

    def test_cannot_capture_own_piece(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("BLACK", board))  # Coloc

