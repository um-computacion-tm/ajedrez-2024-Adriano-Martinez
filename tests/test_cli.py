import unittest
from unittest.mock import patch
from cli import Cli

class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'e2', 'e4', '3'])
    def test_happy_path(self, mock_input):
        cli = Cli()
        cli.iniciar_partida()  # Inicia la partida
        self.assertEqual(mock_input.call_count, 4)  # Verifica que se llamaron las entradas esperadas

    @patch('builtins.input', side_effect=['2', '3'])
    def test_mostrar_menu(self, mock_input):
        cli = Cli()
        cli.mostrar_menu()
        self.assertEqual(mock_input.call_count, 2)  # Se deberían hacer 2 llamadas a input

    @patch('builtins.input', side_effect=['1', 'e2', 'e3', '3'])
    def test_not_happy_path(self, mock_input):
        cli = Cli()
        with self.assertRaises(SystemExit):  # Verifica que se lance un SystemExit al intentar moverse a una posición inválida
            cli.iniciar_partida()

    @patch('builtins.input', side_effect=['1', '2', '3'])
    def test_ver_instrucciones(self, mock_input):
        cli = Cli()
        cli.mostrar_instrucciones()
        self.assertEqual(mock_input.call_count, 1)  # Debe llamar a input una vez para volver al menú

if __name__ == '__main__':
    unittest.main()
