import unittest
from game.exceptions import (
    InvalidMove,
    PieceNotFound,
    OutOfBoard,
    InvalidTurn,
    InvalidPieceMove,
    InvalidFormat
)

class TestChessExceptions(unittest.TestCase):

    def test_invalid_move(self):
        """Verifica que se lance InvalidMove con el mensaje correcto."""
        with self.assertRaises(InvalidMove) as context:
            raise InvalidMove("Movimiento inválido personalizado")
        self.assertEqual(str(context.exception), "Movimiento inválido personalizado")

    def test_piece_not_found(self):
        """Verifica que se lance PieceNotFound con el mensaje por defecto."""
        with self.assertRaises(PieceNotFound) as context:
            raise PieceNotFound()
        self.assertEqual(str(context.exception), "No hay pieza en la posición de origen.")

    def test_out_of_board(self):
        """Verifica que se lance OutOfBoard con el mensaje por defecto."""
        with self.assertRaises(OutOfBoard) as context:
            raise OutOfBoard()
        self.assertEqual(str(context.exception), "La posición indicada se encuentra fuera del tablero")

    def test_invalid_turn(self):
        """Verifica que se lance InvalidTurn con el mensaje por defecto."""
        with self.assertRaises(InvalidTurn) as context:
            raise InvalidTurn()
        self.assertEqual(str(context.exception), "No es tu turno para mover esta pieza.")
    
    def test_invalid_format(self):
        """Verifica que se lance InvalidFormat con el mensaje por defecto."""
        with self.assertRaises(InvalidFormat) as context:
            raise InvalidFormat()
        self.assertEqual(str(context.exception), "Formato de entrada inválido o fuera del tablero, Usa el formato 'e2'.")

    def test_invalid_piece_move(self):
        """Verifica que se lance InvalidPieceMove con el mensaje correcto."""
        piece_name = "Reina"
        with self.assertRaises(InvalidPieceMove) as context:
            raise InvalidPieceMove(piece_name)
        self.assertEqual(str(context.exception), f"Movimiento no válido para {piece_name}.")

if __name__ == "__main__":
    unittest.main()
