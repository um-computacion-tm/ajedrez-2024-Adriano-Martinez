from .piece import Piece
from exceptions import InvalidMoveQueenMove

class Queen(Piece):
    def __str__(self):
        return "♕" if self.__color__ == "WHITE" else "♛"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if from_x == to_x or from_y == to_y or abs(from_x - to_x) == abs(from_y - to_y):
            if self._check_path(from_x, from_y, to_x, to_y):
                return True
        raise InvalidMoveQueenMove("Movimiento inválido para la Reina.")

    def _check_path(self, from_x, from_y, to_x, to_y):
        if from_x == to_x:  # Movimiento vertical
            return self._check_vertical_path(from_x, from_y, to_y)
        elif from_y == to_y:  # Movimiento horizontal
            return self._check_horizontal_path(from_x, from_y, to_x)
        elif abs(from_x - to_x) == abs(from_y - to_y):  # Movimiento diagonal
            return self._check_diagonal_path(from_x, from_y, to_x, to_y)
        return False

    def _check_vertical_path(self, from_x, from_y, to_y):
        step = 1 if to_y > from_y else -1
        for y in range(from_y + step, to_y, step):
            if not self._is_path_clear(from_x, y):
                return False
        return True

    def _check_horizontal_path(self, from_x, from_y, to_x):
        step = 1 if to_x > from_x else -1
        for x in range(from_x + step, to_x, step):
            if not self._is_path_clear(x, from_y):
                return False
        return True

    def _check_diagonal_path(self, from_x, from_y, to_x, to_y):
        step_x = 1 if to_x > from_x else -1
        step_y = 1 if to_y > from_y else -1
        x, y = from_x + step_x, from_y + step_y
        while x != to_x and y != to_y:
            if not self._is_path_clear(x, y):
                return False
            x += step_x
            y += step_y
        return True

    def _is_path_clear(self, x, y):
        piece = self.__board__.get_piece(x, y)
        return piece is None
