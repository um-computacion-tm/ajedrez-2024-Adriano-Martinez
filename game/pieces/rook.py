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
            raise InvalidPieceMove(piece_name="la Torre")
        
        # Usar la lógica para calcular las posiciones ortogonales válidas
        if (to_x, to_y) not in self.possible_orthogonal_positions(from_x, from_y):
            raise InvalidPieceMove(piece_name="la Torre")

        return True
