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
    
    def get_possible_positions(self, from_row, from_col):
        return self.possible_orthogonal_positions(from_row, from_col)

    # Diagonales
    def possible_diagonal_positions(self, from_row, from_col):
        possibles = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonales
        for step_row, step_col in directions:
            possibles += self.scan_direction(from_row, from_col, step_row, step_col)
        return possibles

    # Ortogonales
    def possible_orthogonal_positions(self, from_row, from_col):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Arriba, abajo, derecha, izquierda
        possibles = []
        for step_row, step_col in directions:
            possibles += self.scan_direction(from_row, from_col, step_row, step_col)
        return possibles

    # Generalización para explorar en cualquier dirección
    def scan_direction(self, from_row, from_col, row_increment, col_increment):
        possibles = []
        row, col = from_row + row_increment, from_col + col_increment

        while self.is_position_valid(row, col):
            piece = self.__board__.get_piece(row, col)
            if piece is None:
                possibles.append((row, col))  # Casilla vacía
            elif piece.get_color() != self.get_color():
                possibles.append((row, col))  # Captura posible
                break  # Detener después de capturar
            else:
                break  # Bloqueado por pieza propia
            row += row_increment
            col += col_increment

        return possibles

