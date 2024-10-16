import unittest
from unittest.mock import patch, MagicMock
from game.cli import Cli
from game.chess import Chess
from game.exceptions import *

class TestCli(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['1', 'e2', 'e4'])
    @patch('game.chess.Chess.move')  # Mockea el método 'move' de Chess
    def test_iniciar_partida(self, mock_move, mock_input):
        cli = Cli()
        cli.__chess__ = Chess()  # Inicializa el objeto Chess
        cli.iniciar_partida()
        mock_move.assert_called_once_with('e2', 'e4')
        
    @patch('builtins.input')
    def test_mostrar_menu(self, mock_input):
     mock_input.side_effect = ['menu']  # Simula la entrada para volver al menú
    cli = Cli()
    cli.mostrar_menu()  # Llama a mostrar_menu y asegura que no falla


    @patch('builtins.input')
    def test_mostrar_instrucciones(self, mock_input):
     mock_input.side_effect = ['2', '']  # '2' para elegir mostrar instrucciones, luego '' para simular presionar "Enter"
    cli = Cli()
    cli.mostrar_menu()  # Ejecuta el menú


    @patch('builtins.input', side_effect=['4', 'test_id', '3'])  # Simula que el usuario guarda la partida y luego sale
    @patch('builtins.print')
    def test_guardar_partida(self, mock_print, mock_input):
        cli = Cli()
        cli.__chess__ = MagicMock()  # Simula el objeto Chess
        cli.mostrar_menu()
        # Verifica que la partida se haya guardado con el ID correcto
        cli.__chess__.save_game.assert_called_with('test_id')
        mock_print.assert_any_call("Partida guardada con ID test_id.")


    @patch('builtins.input', side_effect=['5', 'partida_guardada'])
    @patch('game.chess.Chess')  # Mockea la clase Chess completa
    def test_cargar_partida(self, mock_chess, mock_input):
     cli = Cli()
     cli.__chess__ = mock_chess.return_value  # Usa el mock de la clase Chess
     cli.mostrar_menu()  # Ejecuta el menú
    
    # Verifica que la partida fue cargada con el ID 'partida_guardada'
     cli.__chess__.load_game.assert_called_with('partida_guardada')


    @patch('builtins.input')
    @patch('game.chess.Chess')  # Mockea la clase Chess
    def test_play(self, mock_chess, mock_input):
     mock_input.side_effect = ['e2', 'e4', 'menu']  # Simula el input para mover e2 a e4 y luego volver al menú
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
    
    

if __name__ == '__main__':
    unittest.main()