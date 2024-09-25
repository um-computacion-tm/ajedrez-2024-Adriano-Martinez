import unittest
from unittest.mock import patch
from game.cli import Cli

class TestCli(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'e2', 'e4'])
    def test_happy_path(self, mock_input):
     cli = Cli()
     cli.mostrar_menu()  # Llama al menú
     self.assertEqual(mock_input.call_count, 3)  # Se esperan 3 llamadas a input


    @patch('builtins.input', side_effect=['1', 'e2', 'e9', 'e4', '3'])  # Menú (1), Movimiento inválido (e9), Movimiento válido (e4), Salir (3)
    @patch('builtins.print')
    def test_not_happy_path(self, mock_print, mock_input):
        cli = Cli()  # Instancia de Cli
        cli.mostrar_menu()  # Inicia el menú
        # Verifica que se imprimió el error por movimiento inválido
        self.assertTrue(any("Por favor, ingresa una posición válida." in call[0][0] for call in mock_print.call_args_list))
        self.assertEqual(mock_input.call_count, 5)  # Se esperan 5 llamadas a input

    @patch('builtins.input', side_effect=['1', 'e2', 'e9', 'e3', '3'])  # Menú (1), Movimiento inválido (e9), Movimiento válido (e3), Salir (3)
    @patch('builtins.print')
    def test_more_not_happy_path(self, mock_print, mock_input):
        cli = Cli()  # Instancia de Cli
        cli.mostrar_menu()  # Inicia el menú
        # Verifica que se imprimió el error de posición inválida
        self.assertTrue(any("Por favor, ingresa una posición válida." in call[0][0] for call in mock_print.call_args_list))
        self.assertEqual(mock_input.call_count, 5)  # Se esperan 5 llamadas a input

if __name__ == '__main__':
    unittest.main()
