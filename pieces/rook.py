from .piece import Piece
from exceptions import InvalidMoveNoPiece, InvalidMoveRookMove

class Rook(Piece):
    def __str__(self):
        return "♖" if self.__color__ == "WHITE" else "♜"
   
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verificar que el movimiento es horizontal o vertical
        if from_x != to_x and from_y != to_y:
            raise InvalidMoveRookMove

        # Verificar si el movimiento es a la misma posición
        if from_x == to_x and from_y == to_y:
            raise InvalidMoveRookMove

        # Verificar si el camino está bloqueado
        if from_x == to_x:  # Movimiento vertical
            step = 1 if to_y > from_y else -1
            for y in range(from_y + step, to_y, step):
                if self.__board__.get_piece(from_x, y) is not None:
                    raise InvalidMoveRookMove
        else:  # Movimiento horizontal
            step = 1 if to_x > from_x else -1
            for x in range(from_x + step, to_x, step):
                if self.__board__.get_piece(x, from_y) is not None:
                    raise InvalidMoveRookMove

        return True
   
    def _check_vertical_path(self, from_x, from_y, to_y):
     step = 1 if to_y > from_y else -1
     for y in range(from_y + step, to_y, step):
        piece = self.__board__.get_piece(from_x, y)
        if piece is not None:
            return False
     return True

    def _check_horizontal_path(self, from_x, from_y, to_x):
     step = 1 if to_x > from_x else -1
     for x in range(from_x + step, to_x, step):
        piece = self.__board__.get_piece(x, from_y)
        if piece is not None:
            return False
     return True

    def _check_path(self, from_x, from_y, to_x, to_y, vertical):
     if vertical:
        return self._check_vertical_path(from_x, from_y, to_y)
     else:
        return self._check_horizontal_path(from_x, from_y, to_x)

