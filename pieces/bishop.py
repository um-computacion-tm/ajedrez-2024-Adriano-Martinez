from .piece import Piece
from exceptions import InvalidMoveBishopMove

class Bishop(Piece):
    def __str__(self):
        return "♗" if self.__color__ == "WHITE" else "♝"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
    # Verifica si el movimiento es diagonal
     if abs(from_x - to_x) != abs(from_y - to_y):
        raise InvalidMoveBishopMove("Movimiento no válido para el alfil.")
    
    # Determina los pasos en las direcciones x e y
     x_step = 1 if to_x > from_x else -1
     y_step = 1 if to_y > from_y else -1
    
    # Verifica las casillas intermedias en la diagonal
     x, y = from_x + x_step, from_y + y_step
     while x != to_x and y != to_y:
        piece = self.__board__.get_piece(x, y)
        if piece is not None:
            raise InvalidMoveBishopMove("Movimiento bloqueado por otra pieza.")
        x += x_step
        y += y_step
    
    # Verifica la pieza en la posición destino
     piece = self.__board__.get_piece(to_x, to_y)
     if piece is not None and piece.get_color() == self.__color__:
        raise InvalidMoveBishopMove("Movimiento bloqueado por una pieza propia.")

     return True


