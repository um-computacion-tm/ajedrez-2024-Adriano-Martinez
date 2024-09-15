from .piece import Piece
from exceptions import InvalidMovePawnMove

class Pawn(Piece):
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        direction = -1 if self.get_color() == "WHITE" else 1
        start_row = 6 if self.get_color() == "WHITE" else 1

        if self.is_forward_move(from_x, from_y, to_x, to_y, direction, start_row):
            return True
        elif self.is_diagonal_capture(from_x, from_y, to_x, to_y, direction):
            return True

        raise InvalidMovePawnMove("Movimiento no válido para el peón.")

    def is_forward_move(self, from_x, from_y, to_x, to_y, direction, start_row):
        # Movimiento hacia adelante
        if to_y == from_y and self.__board__.get_piece(to_x, to_y) is None:
            if from_x + direction == to_x:
                return True
            if from_x == start_row and from_x + 2 * direction == to_x and self.__board__.get_piece(from_x + direction, from_y) is None:
                return True
        return False

    def is_diagonal_capture(self, from_x, from_y, to_x, to_y, direction):
        # Movimiento de captura en diagonal
        if abs(to_y - from_y) == 1 and from_x + direction == to_x:
            other_piece = self.__board__.get_piece(to_x, to_y)
            return other_piece is not None and other_piece.get_color() != self.get_color()
        return False

    def get_possible_positions(self, from_row, from_col):
        possibles = self.get_possible_positions_move(from_row, from_col)
        possibles.extend(self.get_possible_positions_eat(from_row, from_col))
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        possibles = []
        direction = 1 if self.get_color() == "BLACK" else -1
        # Captura diagonal derecha
        if from_col + 1 < 8:
            other_piece = self.__board__.get_piece(from_row + direction, from_col + 1)
            if other_piece and other_piece.get_color() != self.get_color():
                possibles.append((from_row + direction, from_col + 1))
        # Captura diagonal izquierda
        if from_col - 1 >= 0:
            other_piece = self.__board__.get_piece(from_row + direction, from_col - 1)
            if other_piece and other_piece.get_color() != self.get_color():
                possibles.append((from_row + direction, from_col - 1))
        return possibles

    def get_possible_positions_move(self, from_row, from_col):
        possibles = []
        direction = 1 if self.get_color() == "BLACK" else -1
        start_row = 1 if self.get_color() == "BLACK" else 6
        # Movimiento hacia adelante
        if self.__board__.get_piece(from_row + direction, from_col) is None:
            possibles.append((from_row + direction, from_col))
            if from_row == start_row and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                possibles.append((from_row + 2 * direction, from_col))
        return possibles
