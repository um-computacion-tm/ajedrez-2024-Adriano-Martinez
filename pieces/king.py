from .piece import Piece
from exceptions import InvalidMoveKingMove

class King(Piece):
    def __str__(self):
        return "♔" if self.__color__ == "WHITE" else "♚"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if abs(from_x - to_x) > 1 or abs(from_y - to_y) > 1:
            raise InvalidMoveKingMove("Movimiento no válido para el rey.")
        
        if self.__is_blocked_by_own_piece(to_x, to_y):
            raise InvalidMoveKingMove("Movimiento bloqueado por una pieza propia.")
        
        return True

    def __is_blocked_by_own_piece(self, x, y):
        piece = self.__board__.get_piece(x, y)
        return piece is not None and piece.get_color() == self.__color__