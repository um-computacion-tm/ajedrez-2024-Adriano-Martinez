import unittest
from unittest import mock
from game.chess import Chess
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn, InvalidPieceMove, InvalidFormat

class TestChess(unittest.TestCase):

    def setUp(self):
     self.__chess__ = Chess()
    # Limpia cualquier estado anterior en Redis antes de iniciar el test
     self.__chess__.__redis__.delete("test_game")

    def test_initial_turn_is_white(self):
        # Comprueba que el turno inicial sea de las blancas.
        self.assertEqual(self.__chess__.get_turn(), "WHITE")

    def test_move_valid_piece(self):
        # Prueba mover una pieza válida y el cambio de turno.
        self.__chess__.move("e2", "e4")  # Un peón blanco se mueve
        self.assertEqual(self.__chess__.get_turn(), "BLACK")  # El turno debe ser de negras

    def test_invalid_move(self):
        # Verifica que se lanza InvalidMove para movimientos inválidos.
        with self.assertRaises(InvalidMove):
            self.__chess__.move("e2", "e5")  # Movimiento inválido para un peón blanco

    def test_resign_white(self):
        # Prueba la función de rendición para las blancas.
        self.__chess__.rendirse()  # Las blancas se rinden
        self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_resign_black(self):
        # Prueba la función de rendición para las negras.
        self.__chess__.move("e2", "e4")  # Las blancas mueven primero
        self.__chess__.rendirse()  # Ahora se rinden las negras
        self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    
    def test_end_game_white_wins(self):
        # Prueba el final del juego cuando las negras no tienen piezas.
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(10, 0)):
            self.assertTrue(self.__chess__.end_game())  # Las blancas ganan
            self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_end_game_black_wins(self):
        # Prueba el final del juego cuando las blancas no tienen piezas.
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(0, 10)):
            self.assertTrue(self.__chess__.end_game())  # Las negras ganan
            self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_save_and_load_game(self):
     self.__chess__.move("e2", "e4")  # Se hace un movimiento
     self.__chess__.save_game("test_game")  # Guarda el estado del juego en Redis

    # Crear un nuevo objeto Chess para cargar el juego
     loaded_chess = Chess()
     loaded_chess.load_game("test_game")  # Cargar el juego guardado

    # Verifica el turno y el historial
     self.assertEqual(loaded_chess.get_turn(), "BLACK")
     self.assertEqual(loaded_chess.__history__, [('e2', 'e4')])

    # Verifica el estado del tablero
     self.assertIsNotNone(loaded_chess.__board__.__positions__[4][4])  # Debe haber un peón blanco en e4
     self.assertIsNone(loaded_chess.__board__.__positions__[2][4])  # Debe estar vacío en e3

    # Verifica otras posiciones relevantes
     self.assertEqual(loaded_chess.__board__.__positions__[0][0].get_color(), "BLACK")  # Rook en a8
     self.assertEqual(loaded_chess.__board__.__positions__[0][1].get_color(), "BLACK")  # Knight en b8

    def tearDown(self):
        # Limpia el juego guardado en Redis
        self.__chess__.__redis__.delete("test_game")
    
    def test_move_piece_not_found(self):
     with self.assertRaises(PieceNotFound):
        self.__chess__.move("a3", "a4")  # No hay una pieza en a3
    
    def test_invalid_format(self):
     with self.assertRaises(InvalidFormat):
        self.__chess__.move("zz", "e4")  # Formato inválido
    
    def test_initial_board_setup(self):
     board = self.__chess__.__board__
     self.assertEqual(board.get_piece(0, 0).get_color(), "BLACK")  # Torre negra en a8
     self.assertEqual(board.get_piece(7, 4).get_color(), "WHITE")  # Rey blanco en e1
    
    def test_invalid_turn(self):
     self.__chess__.move("e2", "e4")  # Las blancas mueven primero
     with self.assertRaises(InvalidTurn):
        self.__chess__.move("d2", "d4")  # Intentan mover de nuevo las blancas en lugar de las negras
    
    def test_show_board(self):
    # Muestra el tablero inicial
     initial_board = self.__chess__.show_board()

    # Verifica que algunas piezas clave estén en las posiciones correctas
     self.assertIn("♖", initial_board)  # Torre blanca
     self.assertIn("♔", initial_board)  # Rey blanco
     self.assertIn("♙", initial_board)  # Peón blanco
     self.assertIn("♚", initial_board)  # Rey negro
     self.assertIn("♜", initial_board)  # Torre negra

    # Realiza un movimiento y vuelve a verificar el tablero
     self.__chess__.move("e2", "e4")  # Mueve un peón blanco
     updated_board = self.__chess__.show_board()

    # El tablero actualizado debe reflejar el cambio
     self.assertNotEqual(initial_board, updated_board)  # Deben ser diferentes tras el movimiento
     self.assertIn("♙", updated_board)  # El peón debe estar en la nueva posición

    def test_turn_property(self):
    # Verifica que el turno inicial sea "WHITE"
     self.assertEqual(self.__chess__.turn, "WHITE")

    # Realiza un movimiento y verifica que el turno cambie a "BLACK"
     self.__chess__.move("e2", "e4")
     self.assertEqual(self.__chess__.turn, "BLACK")

    # Realiza un movimiento de las negras y verifica que el turno cambie de nuevo a "WHITE"
     self.__chess__.move("e7", "e5")
     self.assertEqual(self.__chess__.turn, "WHITE")

    def test_end_game_no_white_pieces(self):
    # Simula un estado donde no quedan piezas blancas
     with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(0, 10)):
        self.assertTrue(self.__chess__.end_game())  # El juego debe terminar, negras ganan
        self.assertTrue(self.__chess__.__game_over__)  # El juego está marcado como terminado

    def test_end_game_no_black_pieces(self):
    # Simula un estado donde no quedan piezas negras
     with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(10, 0)):
        self.assertTrue(self.__chess__.end_game())  # El juego debe terminar, blancas ganan
        self.assertTrue(self.__chess__.__game_over__)  # El juego está marcado como terminado

    def test_end_game_still_playing(self):
    # Simula un estado donde ambos jugadores aún tienen piezas
     with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(10, 10)):
        self.assertFalse(self.__chess__.end_game())  # El juego no debería terminar
        self.assertFalse(self.__chess__.__game_over__)  # El juego sigue en curso
    
    def test_create_valid_piece(self):
    # Crea una pieza válida (por ejemplo, un peón blanco)
     piece = self.__chess__.create_piece("WHITE", "Pawn")
     self.assertEqual(type(piece).__name__, "Pawn")  # Verifica que se ha creado un peón
     self.assertEqual(piece.get_color(), "WHITE")  # Verifica que es blanco


    def test_create_invalid_piece(self):
    # Intenta crear una pieza con un tipo desconocido
     with self.assertRaises(ValueError) as context:
        self.__chess__.create_piece("WHITE", "UnknownPiece")
     self.assertEqual(str(context.exception), "Tipo de pieza desconocido: UnknownPiece")
    

if __name__ == "__main__":
    unittest.main()
