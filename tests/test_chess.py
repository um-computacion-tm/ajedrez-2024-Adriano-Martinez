import unittest
from game.chess import Chess
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        self.assertEqual(self.chess.get_turn(), "WHITE")  # Usa el método get_turn

    def test_change_turn(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.get_turn(), "BLACK")  # Usa el método get_turn
        self.chess.change_turn()
        self.assertEqual(self.chess.get_turn(), "WHITE")  # Usa el método get_turn
    
    def test_change_turn_after_move(self):
        self.chess.move("e2", "e4")  # Mueve el peón blanco
        self.assertEqual(self.chess.get_turn(), "BLACK")  # Verifica que el turno cambie a negro
        self.chess.move("e7", "e5")  # Mueve el peón negro
        self.assertEqual(self.chess.get_turn(), "WHITE")  # Verifica que el turno cambie a blanco

    def test_valid_move(self):
        self.chess.move("e2", "e4")  # Mueve el peón blanco
        board = str(self.chess.__board__)
        self.assertIn("e4", board)  # Verifica que la pieza esté en la nueva posición

    def test_invalid_move_out_of_turn(self):
        self.chess.move("e2", "e4")  # Mueve una pieza blanca
        with self.assertRaises(InvalidTurn):  # Aquí se lanza InvalidTurn
            self.chess.move("e7", "e5")  # Intenta mover una pieza negra

    def test_invalid_move_piece_not_found(self):
        with self.assertRaises(PieceNotFound):
            self.chess.move("a3", "a4")  # Posición vacía

    def test_parse_position_valid(self):
        row, col = self.chess.parse_position("e2")
        self.assertEqual((row, col), (6, 4)) 

    def test_parse_position_invalid(self):
        with self.assertRaises(ValueError):
            self.chess.parse_position("z9")  # Posición inválida

    def test_end_game_white_wins(self):
        self.chess.__board__.remove_all_pieces("BLACK")
        game_over = self.chess.end_game()
        self.assertTrue(game_over)

    def test_end_game_black_wins(self):
        self.chess.__board__.remove_all_pieces("WHITE")
        game_over = self.chess.end_game()
        self.assertTrue(game_over)

    def test_save_and_load_game(self):
        filename = "test_save_game.pkl"
        self.chess.save_game(filename)
        loaded_chess = Chess.load_game(filename)
        self.assertEqual(self.chess.show_board(), loaded_chess.show_board())
        self.assertEqual(self.chess.get_turn(), loaded_chess.get_turn())  # Usa el método get_turn

if __name__ == "__main__":
    unittest.main()
