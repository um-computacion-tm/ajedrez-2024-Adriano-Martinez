from .piece import Piece
from game.exceptions import InvalidPieceMove

class Queen(Piece):

    def __init__(self, color, board):
        super().__init__(color, board)
        
    def __str__(self):
        return "♕" if self.get_color() == "WHITE" else "♛"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Combina las posibles posiciones ortogonales y diagonales
        possible_positions = (
            self.possible_orthogonal_positions(from_x, from_y) +
            self.possible_diagonal_positions(from_x, from_y)
        )

        # Verifica si el destino está dentro de las posiciones válidas
        if (to_x, to_y) not in possible_positions:
            raise InvalidPieceMove(piece_name="la Reina")

        return True

    def get_possible_positions(self, from_row, from_col):
        # Combina los movimientos ortogonales y diagonales posibles
        return self.possible_orthogonal_positions(from_row, from_col) + self.possible_diagonal_positions(from_row, from_col)
