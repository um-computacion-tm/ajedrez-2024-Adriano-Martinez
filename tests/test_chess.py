import unittest
from unittest import mock
from game.chess import Chess
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn, InvalidPieceMove

class TestChess(unittest.TestCase):

    def setUp(self):
        self.__chess__ = Chess()

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

    def test_draw_request(self):
        # Prueba la solicitud de empate mutuo.
        with mock.patch('builtins.input', side_effect=['s', 's']):
            self.__chess__.request_draw()
            self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado en empate

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

if __name__ == "__main__":
    unittest.main()
