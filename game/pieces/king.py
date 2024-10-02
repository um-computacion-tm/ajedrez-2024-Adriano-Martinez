from .piece import Piece
from game.exceptions import InvalidPieceMove

class King(Piece):

    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♔" if self.__color__ == "WHITE" else "♚"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if abs(from_x - to_x) > 1 or abs(from_y - to_y) > 1:
            raise InvalidPieceMove("Movimiento no válido para el rey.")
        
        if self.__is_blocked_by_own_piece(to_x, to_y):
            raise InvalidPieceMove("Movimiento bloqueado por una pieza propia.")
        
        return True

    def __is_blocked_by_own_piece(self, x, y):
        piece = self.__board__.get_piece(x, y)
        return piece is not None and piece.get_color() == self.__color__

    def get_possible_positions(self, from_row, from_col):
        possibles = []
        # Considera todas las posiciones adyacentes
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                to_row, to_col = from_row + dx, from_col + dy
                if 0 <= to_row < 8 and 0 <= to_col < 8:
                    if not self.__is_blocked_by_own_piece(to_row, to_col) and not self.is_in_check_after_move(from_row, from_col, to_row, to_col):
                        possibles.append((to_row, to_col))
        
        return possibles

    def is_in_check_after_move(self, from_row, from_col, to_row, to_col):
        # Mueve el rey temporalmente
        original_piece = self.__board__.get_piece(to_row, to_col)
        self.__board__.set_piece(to_row, to_col, self)
        self.__board__.set_piece(from_row, from_col, None)

        # Verifica si el rey está en jaque
        in_check = self.__board__.is_in_check(self.__color__)

        # Restaura el tablero
        self.__board__.set_piece(from_row, from_col, self)
        self.__board__.set_piece(to_row, to_col, original_piece)

        return in_check
