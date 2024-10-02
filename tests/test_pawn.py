import unittest
from game.pieces.pawn import Pawn
from game.board import Board

class TestPawn(unittest.TestCase):

    def test_initial_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(1, 5)  # Peón negro en la posición inicial
        self.assertEqual(possibles, [(2, 5), (3, 5)])  # Puede moverse a 2,5 y 3,5

    def test_not_initial_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro no en posición inicial
        self.assertEqual(possibles, [(3, 5)])  # Puede moverse a 3,5

    def test_eat_left_black(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 6, Pawn("WHITE", board))  # Coloca un peón blanco en 3,6

        possibles = pawn.get_possible_positions(2, 5)  # Peón negro en 2,5
        self.assertEqual(possibles, [(3, 5), (3, 6)])  # Puede avanzar o capturar

    def test_initial_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(6, 4)  # Peón blanco en la posición inicial
        self.assertEqual(possibles, [(5, 4), (4, 4)])  # Puede moverse a 5,4 y 4,4

    def test_not_initial_white(self):
        board = Board()
        pawn = Pawn("WHITE", board)

        possibles = pawn.get_possible_positions(5, 4)  # Peón blanco no en posición inicial
        self.assertEqual(possibles, [(4, 4)])  # Puede moverse a 4,4

    def test_not_initial_white_block(self):
        board = Board()
        pawn = Pawn("WHITE", board)
        board.set_piece(4, 4, Pawn("BLACK", board))  # Bloqueo por pieza propia

        possibles = pawn.get_possible_positions(5, 4)
        self.assertEqual(possibles, [])  # No puede moverse

    def test_not_initial_black_block(self):
        board = Board()
        pawn = Pawn("BLACK", board)
        board.set_piece(5, 4, Pawn("BLACK", board))  # Bloqueo por pieza propia

        possibles = pawn.get_possible_positions(4, 4)
        self.assertEqual(possibles, [])  # No puede moverse

if __name__ == '__main__':
    unittest.main()
