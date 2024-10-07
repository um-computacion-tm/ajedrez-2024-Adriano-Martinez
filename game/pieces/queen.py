from .piece import Piece
from game.exceptions import InvalidPieceMove

class Queen(Piece):

    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♕" if self.get_color() == "WHITE" else "♛"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # La Reina puede moverse en cualquier dirección: horizontal, vertical o diagonal.
        if not (from_x == to_x or from_y == to_y or abs(from_x - to_x) == abs(from_y - to_y)):
            raise InvalidPieceMove(piece_name="Reina")
        
        # Verificar si la posición de destino está en las posiciones posibles.
        possible_positions = (
            self.possible_orthogonal_positions(from_x, from_y) +
            self.possible_diagonal_positions(from_x, from_y)
        )
        
        if (to_x, to_y) not in possible_positions:
            raise InvalidPieceMove(piece_name="Reina")
        
        return True

    def get_possible_positions(self, from_row, from_col):
        # Combina movimientos ortogonales y diagonales
        return self.possible_orthogonal_positions(from_row, from_col) + self.possible_diagonal_positions(from_row, from_col)
