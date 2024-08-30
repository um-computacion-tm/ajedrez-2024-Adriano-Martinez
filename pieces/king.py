from .piece import Piece
from exceptions import InvalidMoveKingMove

class King(Piece):
    def __init__(self, color, board):
        super().__init__(color, board)

    def __str__(self):
        return "♔" if self.__color__ == "WHITE" else "♚"
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if max(abs(from_x - to_x), abs(from_y - to_y)) != 1:
            raise InvalidMoveKingMove("Movimiento no válido para el rey.")
        
        piece = self.__board__.get_piece(to_x, to_y)
        if piece is not None and piece.get_color() == self.__color__:
            raise InvalidMoveKingMove("Movimiento bloqueado por una pieza propia.")
        
        return True