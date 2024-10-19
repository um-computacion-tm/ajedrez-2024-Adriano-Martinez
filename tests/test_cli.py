import unittest
from unittest.mock import patch, MagicMock
from game.cli import Cli
from game.chess import Chess
from game.exceptions import *

class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['s' ,'1', 'e2', 'e4', '4', 's'])  # Simula el input para mover e2 a e4 y luego volver al menú
    @patch('game.chess.Chess.move')  # Mockea el método 'move' de Chess
    def test_iniciar_partida_continuar(self, mock_move, mock_input):
        cli = Cli()
        cli.__chess__ = Chess()  # Inicializa el objeto Chess
        cli.iniciar_partida()
        mock_move.assert_called_once_with('e2', 'e4')

    @patch('builtins.input', side_effect=['1','1', 'e2', 'e4', '4', 's', '3'])  # Simula el input para mover e2 a e4 y luego volver al menú
    @patch('game.chess.Chess.move')  # Mockea el método 'move' de Chess
    def test_iniciar_partida_nueva(self, mock_move, mock_input):
        cli = Cli()
        cli.__chess__ = None  # Inicializa el objeto Chess
        cli.mostrar_menu()
        mock_move.assert_called_once_with('e2', 'e4')
    
    @patch('builtins.input', side_effect=['n' ,'1', 'e2', 'e4', '4', 's'])  # Simula el input para mover e2 a e4 y luego volver al menú
    @patch('game.chess.Chess.move')  # Mockea el método 'move' de Chess
    def test_iniciar_partida_reiniciar(self, mock_move, mock_input):
        cli = Cli()
        cli.__chess__ = Chess()  # Inicializa el objeto Chess
        cli.iniciar_partida()
        mock_move.assert_called_once_with('e2', 'e4')

    @patch('builtins.input')
    def test_mostrar_menu(self, mock_input):
     mock_input.side_effect = ['menu']  # Simula la entrada para volver al menú
    cli = Cli()
    cli.mostrar_menu()  # Llama a mostrar_menu y asegura que no falla

    @patch('builtins.print')
    @patch('builtins.input', side_effect=[''])
    def test_ver_instrucciones(self, mock_input, mock_print):
     cli = Cli()
     cli.mostrar_instrucciones()  # Llama a la función a probar
    
    # Verifica que los mensajes correctos fueron impresos
     mock_print.assert_any_call("\nInstrucciones del Juego:")
     mock_print.assert_any_call("1. El juego de ajedrez se juega en un tablero de 8x8.")
     mock_print.assert_any_call("2. Cada jugador mueve una pieza por turno.")
     mock_print.assert_any_call("3. El objetivo es capturar todas las piezas del oponente para ganar.")
     mock_print.assert_any_call("4. Para mover una pieza, selecciona primero la posición de origen y luego la de destino esto en forma algebraica(a2 a a4).")
    # Verifica que se haya llamado a `input` para esperar que el usuario presione Enter
     mock_input.assert_called_once_with("\nPresiona Enter para volver al menú...")
    
    @patch('builtins.input', side_effect=['s', 's'])  # Ambos jugadores aceptan el empate
    @patch('builtins.print')
    @patch.object(Cli, 'request_draw', return_value=True)  # Simula que el empate es aceptado
    def test_aplicar_accion_solicitud_empate(self, mock_request_draw, mock_print, mock_input):
     cli = Cli()
     cli.__chess__ = Chess()  # Usamos una instancia real de Chess
     error_message, should_return, should_break = cli.aplicar_accion('2')
    # Verificamos que la solicitud de empate fue llamada
     mock_request_draw.assert_called_once()
    # Verificamos que `should_break` es True ya que el juego termina en empate
     self.assertTrue(should_break)
     self.assertFalse(should_return)
     self.assertIsNone(error_message)
    
    @patch('builtins.input', side_effect=['s'])  # El jugador confirma la rendición
    @patch('builtins.print')
    @patch.object(Cli, 'confirmar_accion', return_value=True)  # Simula que el jugador confirma la rendición
    def test_aplicar_accion_rendirse(self, mock_confirmar_accion, mock_print, mock_input):
     cli = Cli()
     cli.__chess__ = MagicMock()  # Mockea el objeto Chess

     error_message, should_return, should_break = cli.aplicar_accion('3')
    # Verificamos que se pidió confirmación
     mock_confirmar_accion.assert_called_once_with("¿Estás seguro de que quieres rendirte? (s/n): ")
    # Verificamos que el método surrender fue llamado
     cli.__chess__.surrender.assert_called_once()
    # Verificamos que se imprimió el mensaje de rendición
     mock_print.assert_any_call("\n¡Te has rendido! Fin de la partida.")
    # Verificamos que `should_break` es True ya que la partida termina con la rendición
     self.assertTrue(should_break)
     self.assertFalse(should_return)
     self.assertIsNone(error_message)
    
    @patch('builtins.input', side_effect=['1', 'e2', 'e4', 's'])  # Elige mover una pieza y luego salir del juego
    @patch('builtins.print')
    def test_play_end_game(self, mock_print, mock_input):
     cli = Cli()
     cli.__chess__ = MagicMock()  # Usa un mock de Chess
     cli.__chess__.is_playing.return_value = False  # Simula que el juego ha terminado
    # Ejecuta el ciclo de juego
     cli.play()
    # Verifica que se reinició el objeto Chess
     self.assertIsNone(cli.__chess__)
    # Verifica que se imprimió el mensaje de retorno al menú
     mock_print.assert_any_call("\nVolviendo al menú principal...")
    # Verifica que se pidió al usuario que presione Enter para volver al menú
     mock_input.assert_called_with("\nPresiona Enter para volver al menu principal...")
    
    @patch('builtins.input', side_effect=['e2', 'e9', 'e4', 'e5'])  # Simula un movimiento inválido y luego un movimiento válido
    @patch('builtins.print')
    def test_get_move_input_invalid_move(self, mock_print, mock_input):
     cli = Cli()
     cli.__chess__ = MagicMock()
    # Simula que `parse_position` lanza una excepción `InvalidMove`
     cli.__chess__.parse_position.side_effect = [InvalidMove("Posición no válida"), None, None]
    # Ejecuta el método
     from_input, to_input = cli.get_move_input()
    # Verifica que se imprimió el mensaje de error correcto
     mock_print.assert_any_call('\nError en la entrada: Posición no válida\nPor favor, ingresa una posición válida.')
    # Verifica que finalmente se obtuvo un movimiento válido
     self.assertEqual(from_input, 'e4')
     self.assertEqual(to_input, 'e5')
    
    # Método para probar EOFError
    @patch('builtins.input', side_effect=EOFError)  # Simula un EOFError en la entrada
    @patch('builtins.print')  # Mockea print para capturar salidas
    def test_mostrar_menu_eof_error(self, mock_print, mock_input):
        cli = Cli()
        cli.mostrar_menu()  # Llama al método
        # Verifica que se imprimió el mensaje de error
        mock_print.assert_called_with("Error: No se recibió entrada. Finalizando.")
    
    @patch('builtins.input', side_effect=['back', ''])
    def test_get_move_input_regresa_al_menu_desde(self, mock_input):
        cli = Cli()
        result = cli.get_move_input()
        # Verificamos que el resultado sea ('back', None)
        self.assertEqual(result, ('back', None))
        mock_input.assert_called_once_with('Desde (e.g. e2, escribe "back" para cancelar accion): ')

    @patch('builtins.input', side_effect=['e2', 'back'])
    def test_get_move_input_regresa_al_menu_hasta(self, mock_input):
        cli = Cli()
        result = cli.get_move_input()
        # Verificamos que el resultado sea ('back', None)
        self.assertEqual(result, ('back', None))
        # Verificamos que se llamaron las entradas correctas
        mock_input.assert_any_call('Desde (e.g. e2, escribe "back" para cancelar accion): ')
        mock_input.assert_any_call('Hasta (e.g. e4 o back para regresar): ')

    @patch.object(Cli, 'get_move_input', return_value=('back', ''))  # Simula que el usuario ingresa 'back'
    def test_handle_move_regresa_al_menu(self, mock_get_move_input):
     cli = Cli()
     cli.__chess__ = Chess()  # Asegúrate de que hay una partida activa
    # Llamamos al método handle_move
     result = cli.handle_move()
    # Verificamos que el resultado sea None, indicando que se regresó al menú
     self.assertIsNone(result)
    # Verificamos que get_move_input fue llamado una vez
     mock_get_move_input.assert_called_once()

    # Método para probar KeyboardInterrupt
    @patch('builtins.input', side_effect=KeyboardInterrupt)  # Simula un KeyboardInterrupt en la entrada
    @patch('builtins.print')  # Mockea print para capturar salidas
    def test_mostrar_menu_keyboard_interrupt(self, mock_print, mock_input):
        cli = Cli()
        cli.mostrar_menu()  # Llama al método
        # Verifica que se imprimió el mensaje de interrupción
        mock_print.assert_called_with("\nInterrupción detectada, saliendo del menú.")
    
    @patch('game.chess.Chess.move')
    def test_attempt_move_unexpected_error(self, mock_move):
        cli = Cli()
        cli.__chess__ = Chess()  # Inicializa el objeto Chess
        # Simula un error inesperado al mover
        mock_move.side_effect = Exception("Error inesperado")
        # Llama al método attempt_move con entradas válidas
        result = cli.attempt_move("e2", "e4")
        # Verifica que el mensaje de error inesperado sea devuelto
        self.assertEqual(result, "Ocurrió un error inesperado: Error inesperado")

    @patch('builtins.input', side_effect=['2', '3'])  # Simula seleccionar la opción 2 para mostrar instrucciones y luego salir
    @patch.object(Cli, 'mostrar_instrucciones')
    def test_mostrar_menu_opcion_instrucciones(self, mock_mostrar_instrucciones, mock_input):
        cli = Cli()
        cli.mostrar_menu()  # Llama al método que estamos probando
        # Verifica que se llamó a mostrar_instrucciones
        mock_mostrar_instrucciones.assert_called_once()
    
    @patch('builtins.input')
    @patch('game.chess.Chess')  # Mockea la clase Chess
    def test_play(self, mock_chess, mock_input):
     mock_input.side_effect = ['1', 'e2', 'e4', '4', 's']  # Simula el input para mover e2 a e4 y luego volver al menú
     cli = Cli()
     cli.__chess__ = mock_chess.return_value  # Asegura que __chess__ no es None
     cli.__chess__.is_playing.return_value = True  # Simula que el juego está activo
     cli.__chess__.end_game.return_value = False  # Simula que no ha terminado el juego
     cli.play()  # Ejecuta la partida
    # Verifica que se llamó al método 'move' con las posiciones correctas
     cli.__chess__.move.assert_called_with('e2', 'e4')

    @patch('builtins.input', side_effect=['1', 'e2', 'e5', '4', 's'])
    @patch('builtins.print')
    def test_attempt_invalid_move(self, mock_print, mock_input):
        cli = Cli()
        cli.__chess__ = MagicMock()
        cli.__chess__.move.side_effect = InvalidMove("Movimiento inválido")
        cli.play()
        # Verifica que el error de movimiento inválido se haya manejado correctamente
        mock_print.assert_any_call("\nError: Movimiento inválido")

    @patch('builtins.input', side_effect=['s', 's'])  # Ambos jugadores aceptan el empate
    @patch('builtins.print')
    def test_request_draw(self, mock_print, mock_input):
        cli = Cli()
        cli.__chess__ = Chess()  # Usamos una instancia real de Chess
        cli.request_draw()
        # Verificamos que se imprimió el mensaje de empate
        mock_print.assert_any_call("La partida ha terminado en empate por mutuo acuerdo.")
        # Verificamos que el juego ha terminado
        self.assertFalse(cli.__chess__.is_playing())
    
    @patch('os.system')
    def test_clear_terminal_exception(self, mock_system):
        cli = Cli()
        # Simula que os.system lanza una excepción
        mock_system.side_effect = Exception("Error inesperado al limpiar la terminal")
        with patch('builtins.print') as mock_print:
            cli.clear_terminal()  # Llama al método que estamos probando
            # Verifica que se haya llamado a print con el mensaje de error
            mock_print.assert_called_once_with("Error al limpiar la terminal: Error inesperado al limpiar la terminal")
    
if __name__ == "__main__":
    unittest.main()