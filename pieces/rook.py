from .piece import Piece
from exceptions import InvalidMoveNoPiece, InvalidMoveRookMove

class Rook(Piece):
    def __str__(self):
        return "♖" if self.__color__ == "WHITE" else "♜"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verificar que el movimiento es horizontal o vertical
        if from_x != to_x and from_y != to_y:
            raise InvalidMoveRookMove("El movimiento debe ser horizontal o vertical.")

        # Verificar si el movimiento es a la misma posición
        if from_x == to_x and from_y == to_y:
            raise InvalidMoveRookMove("El movimiento no puede ser a la misma posición.")

        # Verificar si el camino está bloqueado
        if from_x == to_x:  # Movimiento vertical
            if not self._check_path(from_x, from_y, to_y, vertical=True):
                raise InvalidMoveRookMove("Camino bloqueado en movimiento vertical.")
        else:  # Movimiento horizontal
            if not self._check_path(from_x, from_y, to_x, vertical=False):
                raise InvalidMoveRookMove("Camino bloqueado en movimiento horizontal.")

        return True

    def _check_path(self, from_x, from_y, to, vertical):
        step = 1 if to > (from_y if vertical else from_x) else -1
        for coord in range(from_y + step if vertical else from_x + step, to, step):
            if vertical:
                if not self._is_path_clear(from_x, coord):
                    return False
            else:
                if not self._is_path_clear(coord, from_y):
                    return False
        return True

    def _is_path_clear(self, x, y):
        piece = self.__board__.get_piece(x, y)
        return piece is None
