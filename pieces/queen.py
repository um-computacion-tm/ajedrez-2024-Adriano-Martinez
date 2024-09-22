from .piece import Piece
from exceptions import InvalidMoveQueenMove

class Queen(Piece):
    def __str__(self):
        return "♕" if self.__color__ == "WHITE" else "♛"


    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if not (from_x == to_x or from_y == to_y or abs(from_x - to_x) == abs(from_y - to_y)):
            raise InvalidMoveQueenMove("Movimiento no válido para la reina.")
        
        if not self.is_path_clear(from_x, from_y, to_x, to_y):
            raise InvalidMoveQueenMove("Camino bloqueado por otra pieza.")

        return True

    def is_path_clear(self, from_x, from_y, to_x, to_y):
        step_x = (to_x - from_x) // max(1, abs(to_x - from_x)) if from_x != to_x else 0
        step_y = (to_y - from_y) // max(1, abs(to_y - from_y)) if from_y != to_y else 0
        
        x, y = from_x + step_x, from_y + step_y
        while (x, y) != (to_x, to_y):
            if self.__board__.get_piece(x, y) is not None:
                return False
            x += step_x
            y += step_y
        return True

    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(from_row, from_col) + self.possible_diagonal_positions(from_row, from_col)
