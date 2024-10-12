'''import unittest
from unittest.mock import patch
from game.chess import Chess
from game.cli import Cli
from game.exceptions import InvalidMove

class TestCli(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', 's' , 'n', 'menu', 'rendirse', ''
    ])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_happy_path(self, mock_chess_move, mock_print, mock_input):
        cli = Cli()
        
        # Llamamos al método para iniciar una nueva partida
        cli.iniciar_partida()

        # Verifica que se llamaron los métodos esperados
        self.assertEqual(mock_input.call_count, 4)  # Asegúrate de contar todas las llamadas
        self.assertEqual(mock_print.call_count, 3)  # Ajusta según el número de prints esperados en el flujo
        self.assertEqual(mock_chess_move.call_count, 1)  # Asegúrate de contar los movimientos esperados

# Ejecutar pruebas

    @patch('builtins.input', side_effect=['hola', '1', '2', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        cli = Cli()
        cli.iniciar_partida()
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', '1', '2', 'hola'])
    @patch('builtins.print')
    @patch.object(Chess, 'move')
    def test_more_not_happy_path(self, mock_chess_move, mock_print, mock_input):
        cli = Cli()
        cli.iniciar_partida()
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(mock_chess_move.call_count, 0)

    @patch('builtins.input', side_effect=['1', 'n', '1'])
    @patch('builtins.print')
    def test_continue_active_game(self, mock_print, mock_input):
        cli = Cli()
        cli.iniciar_partida()  # Inicia la partida
        cli.iniciar_partida()  # Intenta iniciar otra vez
        self.assertEqual(mock_print.call_count, 3)  # Asegúrate de que se imprima el mensaje para continuar

    @patch('builtins.input', side_effect=['1', 's'])
    @patch('builtins.print')
    def test_restart_game(self, mock_print, mock_input):
        cli = Cli()
        cli.iniciar_partida()  # Inicia la partida
        cli.iniciar_partida()  # Intenta iniciar otra vez
        self.assertIsInstance(cli._Cli__chess__, Chess)  # Verifica que se reinicie
        self.assertEqual(mock_print.call_count, 3)  # Verifica el conteo de prints

    @patch('builtins.input', side_effect=['mi_partida'])
    @patch('builtins.print')
    @patch.object(Chess, 'save_game')
    def test_guardar_partida(self, mock_save_game, mock_print, mock_input):
        cli = Cli()
        cli.iniciar_partida()  # Inicia la partida
        cli.guardar_partida()  # Guarda la partida
        self.assertTrue(mock_save_game.called)  # Verifica que se llame a save_game
        self.assertEqual(mock_print.call_count, 2)  # Verifica el conteo de prints

    @patch('builtins.input', side_effect=['mi_partida'])
    @patch('builtins.print')
    @patch.object(Chess, 'load_game')
    def test_cargar_partida(self, mock_load_game, mock_print, mock_input):
        cli = Cli()
        cli.cargar_partida()  # Intenta cargar la partida
        self.assertTrue(mock_load_game.called)  # Verifica que se llame a load_game
        self.assertEqual(mock_print.call_count, 2)  # Verifica el conteo de prints

    @patch('builtins.print')
    def test_mostrar_instrucciones(self, mock_print):
        cli = Cli()
        cli.mostrar_instrucciones()  # Muestra las instrucciones
        self.assertEqual(mock_print.call_count, 6)  # Verifica el conteo de prints de instrucciones

    @patch('builtins.input', side_effect=['menu'])
    @patch('builtins.print')
    def test_wait_for_menu(self, mock_print, mock_input):
        cli = Cli()
        cli.wait_for_menu()  # Intenta esperar al menú
        self.assertEqual(mock_print.call_count, 1)  # Verifica el conteo de prints

    @patch('builtins.input', side_effect=['1', '2'])
    @patch('builtins.print')
    @patch.object(Chess, 'move', side_effect=InvalidMove())
    def test_attempt_move_invalid(self, mock_move, mock_print, mock_input):
        cli = Cli()
        cli.iniciar_partida()
        result = cli.attempt_move('e2', 'e4')
        self.assertEqual(mock_print.call_count, 1)  # Verifica que se imprima el error

    
    @patch('builtins.input', side_effect=['1', 'draw'])  # Inicia partida y solicita empate
    @patch('builtins.print')
    @patch.object(Chess, 'request_draw')
    def test_handle_draw(self, mock_request_draw, mock_print, mock_input):
        cli = Cli()
        
        # Simula iniciar la partida
        cli.iniciar_partida()

        # Simula la solicitud de empate
        cli.play()  # Llama a play() que procesará 'draw'

        # Verifica que se haya llamado al método para solicitar un empate
        self.assertTrue(mock_request_draw.called)  # Verifica que request_draw fue llamado
        
        # Verifica que se imprime el mensaje de empate
        mock_print.assert_called_with("\n¡Empate solicitado! Fin de la partida.")

        # Verifica que la entrada fue llamada dos veces
        self.assertEqual(mock_input.call_count, 2)  # 1 para iniciar partida, 1 para solicitar empate

if __name__ == '__main__':
    unittest.main()'''