from .piece import Piece
from exceptions import InvalidMoveQueenMove

class Queen(Piece):
    def __str__(self):
        return "♕" if self.__color__ == "WHITE" else "♛"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if not self.check(from_x, from_y, to_x, to_y):
            raise InvalidMoveQueenMove("Movimiento no válido para la Reina.")
        
        if not self._is_path_clear(from_x, from_y, to_x, to_y):
            raise InvalidMoveQueenMove("Camino bloqueado en el movimiento de la Reina.")
        
        return True

    def check(self, from_x, from_y, to_x, to_y):
        # Verifica si el movimiento es válido
        return (from_x == to_x or from_y == to_y or abs(from_x - to_x) == abs(from_y - to_y))

    def _is_path_clear(self, from_x, from_y, to_x, to_y):
        # Determinar dirección del movimiento
        step_x = 1 if to_x > from_x else -1 if to_x < from_x else 0
        step_y = 1 if to_y > from_y else -1 if to_y < from_y else 0
        
        x, y = from_x + step_x, from_y + step_y
        while x != to_x or y != to_y:
            if self.__board__.get_piece(x, y) is not None:
                return False
            x += step_x
            y += step_y
        return True