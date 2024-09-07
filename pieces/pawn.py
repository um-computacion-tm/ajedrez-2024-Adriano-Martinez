from .piece import Piece
from exceptions import InvalidMovePawnMove

class Pawn(Piece):
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        direction = 1 if self.__color__ == "WHITE" else -1
        start_row = 1 if self.__color__ == "WHITE" else 6

        if self.is_forward_move(from_x, from_y, to_x, to_y):
            return True
        elif self.is_diagonal_capture(from_x, from_y, to_x, to_y, direction):
            return True

        raise InvalidMovePawnMove("Movimiento no válido para el peón.")

    def is_forward_move(self, from_x, from_y, to_x, to_y):
        direction = 1 if self.__color__ == "WHITE" else -1
        start_row = 1 if self.__color__ == "WHITE" else 6
        
        # Movimiento de una casilla hacia adelante
        if from_x == to_x:
            if to_y == from_y + direction:
                if self.__board__.get_piece(to_x, to_y) is None:
                    return True
                raise InvalidMovePawnMove("No puede capturar moviéndose hacia adelante.")
            # Movimiento de dos casillas desde la posición inicial
            if from_y == start_row and to_y == from_y + 2 * direction:
                if self.__board__.get_piece(to_x, to_y) is None and self.__board__.get_piece(to_x, from_y + direction) is None:
                    return True
                raise InvalidMovePawnMove("El camino está bloqueado.")
        return False

    def is_diagonal_capture(self, from_x, from_y, to_x, to_y, direction):
        if abs(from_x - to_x) == 1 and to_y == from_y + direction:
            target_piece = self.__board__.get_piece(to_x, to_y)
            if target_piece is not None and target_piece.get_color() != self.__color__:
                return True
            raise InvalidMovePawnMove("Solo puede capturar en diagonal.")
        return False
