from .piece import Piece
from game.exceptions import InvalidPieceMove

class Pawn(Piece):

    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verifica si las posiciones son válidas
        if not (self.is_position_valid(from_x, from_y) and self.is_position_valid(to_x, to_y)):
            raise InvalidPieceMove(piece_name="Peón")
        
        # Verifica si el movimiento es válido
        if not self.valid_positions(from_x, from_y, to_x, to_y):
            raise InvalidPieceMove(piece_name="Peón")

        direction = -1 if self.get_color() == "WHITE" else 1
        start_row = 6 if self.get_color() == "WHITE" else 1

        # Crear diccionarios para las posiciones
        from_position = {'x': from_x, 'y': from_y}
        to_position = {'x': to_x, 'y': to_y}

        if self.is_forward_move(from_position, to_position, direction, start_row):
            return True
        if self.is_diagonal_capture(from_x, from_y, to_x, to_y, direction):
            return True
        #raise InvalidPieceMove(piece_name="Peón")
    
    def is_forward_move(self, from_pos, to_pos, direction, start_row):
        from_x = from_pos['x']
        from_y = from_pos['y']
        to_x = to_pos['x']
        to_y = to_pos['y']

        if to_y == from_y:
            if to_x == from_x + direction and self.__board__.get_piece(to_x, to_y) is None:
                return True
            if from_x == start_row and to_x == from_x + 2 * direction and self.__board__.get_piece(from_x + direction, from_y) is None:
                return True
        return False

    def is_diagonal_capture(self, from_x, from_y, to_x, to_y, direction):
        if abs(to_y - from_y) == 1 and to_x == from_x + direction:
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
        for col in [from_col - 1, from_col + 1]:
            if 0 <= col < 8:
                other_piece = self.__board__.get_piece(from_row + direction, col)
                if other_piece and other_piece.get_color() != self.get_color():
                    possibles.append((from_row + direction, col))
        return possibles

    def get_possible_positions_move(self, from_row, from_col):
        possibles = []
        direction = 1 if self.get_color() == "BLACK" else -1
        start_row = 1 if self.get_color() == "BLACK" else 6
        if self.__board__.get_piece(from_row + direction, from_col) is None:
            possibles.append((from_row + direction, from_col))
            if from_row == start_row and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                possibles.append((from_row + 2 * direction, from_col))
        return possibles
