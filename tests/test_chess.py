import unittest
from unittest import mock
from game.chess import Chess
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn, InvalidFormat

class TestChess(unittest.TestCase):

    def setUp(self):
        """Inicializa una instancia de la clase Chess antes de cada prueba."""
        self.__chess__ = Chess()

    def test_initial_turn_is_white(self):
        """Verifica que el turno inicial sea de las blancas."""
        self.assertEqual(self.__chess__.turn, "WHITE")

    def test_move_valid_piece(self):
        """Prueba el movimiento de una pieza válida y asegura el cambio de turno."""
        self.__chess__.move("e2", "e4")  # Un peón blanco se mueve
        self.assertEqual(self.__chess__.turn, "BLACK")  # El turno debe ser de negras

    def test_invalid_move(self):
        """Verifica que se lanza InvalidMove para movimientos inválidos."""
        with self.assertRaises(InvalidMove):
            self.__chess__.move("e2", "e5")  # Movimiento inválido para un peón blanco

    def test_resign_white(self):
        """Prueba la función de rendición para las blancas."""
        self.__chess__.surrender()  # Las blancas se rinden
        self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_resign_black(self):
        """Prueba la función de rendición para las negras después de que las blancas mueven."""
        self.__chess__.move("e2", "e4")  # Las blancas mueven primero
        self.__chess__.surrender()  # Las negras se rinden
        self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_end_game_white_wins(self):
        """Verifica el final del juego cuando las negras no tienen piezas."""
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(10, 0)):
            self.assertTrue(self.__chess__.end_game())  # Las blancas ganan
            self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_end_game_black_wins(self):
        """Verifica el final del juego cuando las blancas no tienen piezas."""
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(0, 10)):
            self.assertTrue(self.__chess__.end_game())  # Las negras ganan
            self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado

    def test_move_piece_not_found(self):
        """Verifica que se lanza PieceNotFound al intentar mover una pieza que no existe."""
        with self.assertRaises(PieceNotFound):
            self.__chess__.move("a3", "a4")  # No hay una pieza en a3

    def test_invalid_format(self):
        """Verifica que se lanza InvalidFormat al usar un formato de movimiento inválido."""
        with self.assertRaises(InvalidFormat):
            self.__chess__.move("zz", "e4")  # Formato inválido

    def test_initial_board_setup(self):
        """Verifica que las piezas estén configuradas correctamente en el tablero inicial."""
        board = self.__chess__.__board__
        self.assertEqual(board.get_piece(0, 0).get_color(), "BLACK")  # Torre negra en la posición inicial
        self.assertEqual(board.get_piece(7, 4).get_color(), "WHITE")  # Rey blanco en la posición inicial

    def test_invalid_turn(self):
        """Verifica que se lanza InvalidTurn al intentar mover de nuevo cuando no es el turno del jugador."""
        self.__chess__.move("e2", "e4")  # Las blancas mueven primero
        with self.assertRaises(InvalidTurn):
            self.__chess__.move("d2", "d4")  # Intentan mover de nuevo las blancas en lugar de las negras


    def test_show_board(self):
        """Muestra el tablero inicial y verifica que ciertas piezas estén en las posiciones correctas."""
        initial_board = self.__chess__.show_board()
        # Verifica que algunas piezas clave estén en el tablero inicial
        self.assertIn("♖", initial_board)  # Torre blanca
        self.assertIn("♔", initial_board)  # Rey blanco
        self.assertIn("♙", initial_board)  # Peón blanco
        self.assertIn("♚", initial_board)  # Rey negro
        self.assertIn("♜", initial_board)  # Torre negra

        # Realiza un movimiento y verifica que el tablero se actualice
        self.__chess__.move("e2", "e4")  # Mueve un peón blanco
        updated_board = self.__chess__.show_board()

        # Verifica que el tablero actualizado refleje el cambio
        self.assertNotEqual(initial_board, updated_board)  # Deben ser diferentes tras el movimiento
        self.assertIn("♙", updated_board)  # El peón debe estar en la nueva posición

    def test_turn_property(self):
        """Verifica que la propiedad del turno cambie correctamente."""
        self.assertEqual(self.__chess__.turn, "WHITE")  # Verifica el turno inicial
        self.__chess__.move("e2", "e4")  # Realiza un movimiento
        self.assertEqual(self.__chess__.turn, "BLACK")  # Verifica que el turno cambie a "BLACK"

    def test_end_game_no_white_pieces(self):
        """Simula un estado donde no quedan piezas blancas y verifica el resultado del juego."""
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(0, 10)):
            self.assertTrue(self.__chess__.end_game())  # Las negras ganan
            self.assertTrue(self.__chess__.__game_over__)  # El juego está marcado como terminado

    def test_end_game_no_black_pieces(self):
        """Simula un estado donde no quedan piezas negras y verifica el resultado del juego."""
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(10, 0)):
            self.assertTrue(self.__chess__.end_game())  # Las blancas ganan
            self.assertTrue(self.__chess__.__game_over__)  # El juego está marcado como terminado


    def test_end_game_still_playing(self):
        """Simula un estado donde ambos jugadores aún tienen piezas y verifica que el juego continúe."""
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(10, 10)):
            with mock.patch.object(self.__chess__.__board__, 'is_king_alive', side_effect=lambda color: True):  # Simula que ambos reyes están vivos
                self.assertFalse(self.__chess__.end_game())  # El juego no debería terminar
                self.assertFalse(self.__chess__.__game_over__)  # El juego sigue en curso

    def test_white_king_captured(self):
        """Simula que el rey blanco ha sido capturado y verifica el final del juego."""
        with mock.patch.object(self.__chess__.__board__, 'is_king_alive', side_effect=lambda color: False if color == "WHITE" else True):
            result = self.__chess__.end_game()
            self.assertTrue(self.__chess__.__game_over__)  # El juego debe haber terminado
            self.assertTrue(result)  # El método debe retornar True

    def test_black_king_captured(self):
        """Simula que el rey negro ha sido capturado y verifica el final del juego."""
        with mock.patch.object(self.__chess__.__board__, 'is_king_alive', side_effect=lambda color: True if color == "WHITE" else False):
            result = self.__chess__.end_game()
            self.assertTrue(self.__chess__.__game_over__)  # El juego debe haber terminado
            self.assertTrue(result)  # El método debe retornar True

    def test_offer_draw_accepted(self):
        """Verifica que el juego termine en empate cuando ambos jugadores aceptan tablas."""
        result = self.__chess__.offer_draw(white_accepts=True, black_accepts=True)
        self.assertTrue(result)  # El juego debería terminar en empate
        self.assertFalse(self.__chess__.is_playing())  # El juego debe haber terminado
        self.assertTrue(self.__chess__.__game_over__)  # Verifica que el juego esté marcado como terminado

    def test_offer_draw_rejected_by_white(self):
        """Verifica que el juego continúe cuando las blancas rechazan el empate."""
        result = self.__chess__.offer_draw(white_accepts=False, black_accepts=True)
        self.assertFalse(result)  # No se debe aceptar el empate
        self.assertTrue(self.__chess__.is_playing())  # El juego debe continuar

    def test_offer_draw_rejected_by_black(self):
        """Verifica que el juego continúe cuando las negras rechazan el empate."""
        result = self.__chess__.offer_draw(white_accepts=True, black_accepts=False)
        self.assertFalse(result)  # No se debe aceptar el empate
        self.assertTrue(self.__chess__.is_playing())  # El juego debe continuar
    
    def test_move_after_game_ends(self):
        """Simula un estado donde no quedan piezas negras."""
        with mock.patch.object(self.__chess__.__board__, 'count_pieces', return_value=(0, 10)):
            self.__chess__.end_game()  # Se termina el juego
            result = self.__chess__.move("e2", "e4")  # Intenta hacer un movimiento
            self.assertIsNone(result)  # Verifica que el resultado sea None o el valor que has decidido retornar

if __name__ == "__main__":
    unittest.main()