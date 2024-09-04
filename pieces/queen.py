from .piece import Piece
from exceptions import InvalidMoveQueenMove

class Queen(Piece):
    def __str__(self):
        return "♕" if self.__color__ == "WHITE" else "♛"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if from_x == to_x or from_y == to_y:
            return self._check_rook_move(from_x, from_y, to_x, to_y)

        # Movimiento diagonal 
        elif abs(from_x - to_x) == abs(from_y - to_y):
            return self._check_bishop_move(from_x, from_y, to_x, to_y)

        else:
            raise InvalidMoveQueenMove("Movimiento no válido para la Reina.")
    
    def _check_rook_move(self, from_x, from_y, to_x, to_y):
        step = 1 if to_y > from_y else -1 if from_x == to_x else 1 if to_x > from_x else -1
        if from_x == to_x:  # Movimiento vertical
            for y in range(from_y + step, to_y, step):
                if self.__board__.get_piece(from_x, y) is not None:
                    raise InvalidMoveQueenMove("Camino bloqueado en movimiento vertical.")
        else:  # Movimiento horizontal
            for x in range(from_x + step, to_x, step):
                if self.__board__.get_piece(x, from_y) is not None:
                    raise InvalidMoveQueenMove("Camino bloqueado en movimiento horizontal.")
        return True
    
    def _check_bishop_move(self, from_x, from_y, to_x, to_y):
        step_x = 1 if to_x > from_x else -1
        step_y = 1 if to_y > from_y else -1

        x, y = from_x + step_x, from_y + step_y
        while x != to_x and y != to_y:
            if self.__board__.get_piece(x, y) is not None:
                raise InvalidMoveQueenMove("Camino bloqueado en movimiento diagonal.")
            x += step_x
            y += step_y

        return True