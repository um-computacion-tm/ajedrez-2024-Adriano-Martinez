from .piece import Piece
from game.exceptions import InvalidPieceMove

class Bishop(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        return "♗" if self.get_color() == "WHITE" else "♝"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verificar que el movimiento sea diagonal y dentro de las posiciones posibles
        if (to_x, to_y) not in self.possible_diagonal_positions(from_x, from_y):
            raise InvalidPieceMove(piece_name="el Alfil")

        return True

    def get_possible_positions(self, from_row, from_col):
        # Retorna directamente las posiciones diagonales válidas
        return self.possible_diagonal_positions(from_row, from_col)
