from .piece import Piece
from game.exceptions import InvalidPieceMove

class King(Piece):

    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♔" if self.get_color() == "WHITE" else "♚"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
     if not self.valid_positions(from_x, from_y, to_x, to_y):
        raise InvalidPieceMove(piece_name="Rey")

     target_piece = self.__board__.get_piece(to_x, to_y)
     if target_piece is not None and target_piece.get_color() == self.get_color():
        raise InvalidPieceMove("No puedes mover a una posición ocupada por tu propia pieza.")

     return True


    def get_possible_positions(self, from_row, from_col):
        possibles = []
        # Considera todas las posiciones adyacentes
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                to_row, to_col = from_row + dx, from_col + dy
                if self.is_position_valid(to_row, to_col):
                    if not self.__is_blocked_by_own_piece(to_row, to_col):
                        possibles.append((to_row, to_col))
        
        return possibles

    def __is_blocked_by_own_piece(self, x, y):
        piece = self.__board__.get_piece(x, y)
        return piece is not None and piece.get_color() == self.get_color()