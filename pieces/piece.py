class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board
        
    def get_color(self):
        return self.__color__

    def __str__(self):
        return ""

    @staticmethod
    def is_position_valid(x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if not (self.is_position_valid(from_x, from_y) and self.is_position_valid(to_x, to_y)):
            return False  
        if from_x == to_x and from_y == to_y:
            return False  
        raise NotImplementedError("Implementar en subclases específicas.")

    def valid_positions(self, from_row, from_col, to_row, to_col):
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions

    def possible_diagonal_positions(self, from_row, from_col):
        return ()

    def possible_orthogonal_positions(self, from_row, from_col):
        return (
            self.possible_positions_vd(from_row, from_col) +
            self.possible_positions_va(from_row, from_col)
        )

    def possible_positions_vd(self, row, col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))
                break
            possibles.append((next_row, col))
        return possibles

    def possible_positions_va(self, row, col):
        possibles = []
        for next_row in range(row - 1, -1, -1):
            possibles.append((next_row, col))
        return possibles

