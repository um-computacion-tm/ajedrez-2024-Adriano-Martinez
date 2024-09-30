import unittest
from game.chess import Chess
from game.exceptions import PieceNotFound, InvalidMove

class TestChess(unittest.TestCase):
    
    def setUp(self):
        self.chess = Chess()

    def test_initial_turn(self):
        #Verifica que el turno inicial sea de las blancas
        self.assertEqual(self.chess.turn, "WHITE")

    def test_change_turn(self):
        #Prueba que el turno cambie correctamente después de cada movimiento
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.turn, "WHITE")

    def test_valid_move(self):
     self.chess.move("e2", "e4")  # Mueve el peón blanco
     board = str(self.chess.__board__)  # Obtiene la representación del tablero
     self.assertIn("e4", board)  # Verifica que la pieza esté en la nueva posición

    def test_invalid_move_out_of_turn(self):
     self.chess.__turn__ = "BLACK"  # Configurar turno incorrecto
     with self.assertRaises(InvalidMove):
        self.chess.move("e2", "e4")  # Intentar mover una pieza blanca en turno negro

    def test_invalid_move_piece_not_found(self):
     with self.assertRaises(PieceNotFound):
        self.chess.move("a3", "a4")  # Posición vacía, debería lanzar PieceNotFound

    def test_parse_position_valid(self):
        #Prueba que el método parse_position convierta correctamente a coordenadas válidas
        row, col = self.chess.parse_position("e2")
        self.assertEqual((row, col), (6, 4)) 

    def test_parse_position_invalid(self):
        #Prueba que el método parse_position arroje ValueError para coordenadas inválidas
        with self.assertRaises(ValueError):
            self.chess.parse_position("z9")  # Posición inválida

    def test_end_game_white_wins(self):
        #Prueba que el juego termine cuando las piezas negras son eliminadas
        self.chess.__board__.remove_all_pieces("BLACK")
        game_over = self.chess.end_game()
        self.assertTrue(game_over)

    def test_end_game_black_wins(self):
        #Prueba que el juego termine cuando las piezas blancas son eliminadas
        self.chess.__board__.remove_all_pieces("WHITE")
        game_over = self.chess.end_game()
        self.assertTrue(game_over)

    def test_save_and_load_game(self):
        #Prueba guardar y cargar una partida
        filename = "test_save_game.pkl"
        self.chess.save_game(filename)
        loaded_chess = Chess.load_game(filename)
        self.assertEqual(self.chess.show_board(), loaded_chess.show_board())  # Compara el estado del tablero
        self.assertEqual(self.chess.turn, loaded_chess.turn)  # Compara el turno

if __name__ == "__main__":
    unittest.main()
