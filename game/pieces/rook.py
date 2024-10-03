from .piece import Piece
from game.exceptions import InvalidPieceMove

class Rook(Piece):
    
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        return "♖" if self.get_color() == "WHITE" else "♜"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verificar que el movimiento es horizontal o vertical
        if from_x != to_x and from_y != to_y:
            raise InvalidPieceMove("El movimiento debe ser horizontal o vertical.")

        # Verificar si el movimiento es a la misma posición
        if from_x == to_x and from_y == to_y:
            raise InvalidPieceMove("El movimiento no puede ser a la misma posición.")

        # Utilizar la lógica centralizada para calcular las posiciones posibles ortogonales
        possible_positions = self.possible_orthogonal_positions(from_x, from_y)
        
        if (to_x, to_y) not in possible_positions:
            raise InvalidPieceMove("Camino bloqueado o movimiento inválido.")

        return True
