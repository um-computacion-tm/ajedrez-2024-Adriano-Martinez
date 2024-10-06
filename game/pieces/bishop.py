from .piece import Piece
from game.exceptions import InvalidPieceMove

class Bishop(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)
        
    def __str__(self):
        return "♗" if self.get_color() == "WHITE" else "♝"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verificar que el movimiento sea diagonal
        if not self.valid_positions(from_x, from_y, to_x, to_y):
            raise InvalidPieceMove(piece_name="Alfil")
        
        return True  # Movimiento válido

    def get_possible_positions(self, from_row, from_col):
        # Reutiliza el método de posiciones diagonales de la clase base
        return self.possible_diagonal_positions(from_row, from_col)



