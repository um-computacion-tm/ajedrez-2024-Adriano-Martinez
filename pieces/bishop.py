from .piece import Piece
from exceptions import InvalidMoveBishopMove

class Bishop(Piece):
    def __str__(self):
        return "♗" if self.__color__ == "WHITE" else "♝"

    def __is_path_clear(self, from_x, from_y, to_x, to_y):
        step_x = 1 if to_x > from_x else -1
        step_y = 1 if to_y > from_y else -1
        
        x, y = from_x + step_x, from_y + step_y
        while x != to_x and y != to_y:
            piece = self.__board__.get_piece(x, y)
            if piece is not None:
                if piece.get_color() == self.__color__:
                    return False  # Movimiento bloqueado por una pieza propia
                else:
                    return False  # Movimiento bloqueado por una pieza rival
            x += step_x
            y += step_y
        
        return True  

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if from_x == to_x or from_y == to_y:
            raise InvalidMoveBishopMove("Movimiento no válido para el alfil.")
        
        if not self.__is_path_clear(from_x, from_y, to_x, to_y):
            raise InvalidMoveBishopMove("Movimiento bloqueado por otra pieza.")
        
        return True
