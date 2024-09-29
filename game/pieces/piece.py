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
            row, col = from_row + step_row, from_col + step_col
            while 0 <= row < 8 and 0 <= col < 8:
                piece = self.__board__.get_piece(row, col)
                if piece is None:
                    possibles.append((row, col))  # Casilla vacía
                elif piece.get_color() != self.get_color():
                    possibles.append((row, col))  # Captura posible
                    break  # Detener después de capturar
                else:
                    break  # Bloqueado por pieza propia
                row += step_row
                col += step_col
        return possibles

    # Ortogonales
    def possible_orthogonal_positions(self, from_row, from_col):
        return (
            self.possible_positions_vertical(from_row, from_col) +
            self.possible_positions_horizontal(from_row, from_col)
        )

    def possible_positions_vertical(self, row, col):
        possibles = []

        # Movimiento hacia abajo
        for next_row in range(row + 1, 8):
            piece = self.__board__.get_piece(next_row, col)
            if piece is None:
                possibles.append((next_row, col))  # Casilla vacía
            elif piece.get_color() != self.get_color():
                possibles.append((next_row, col))  # Captura posible
                break  # Detener después de capturar
            else:
                break  # Bloqueado por pieza propia

        # Movimiento hacia arriba
        for next_row in range(row - 1, -1, -1):
            piece = self.__board__.get_piece(next_row, col)
            if piece is None:
                possibles.append((next_row, col))  # Casilla vacía
            elif piece.get_color() != self.get_color():
                possibles.append((next_row, col))  # Captura posible
                break  # Detener después de capturar
            else:
                break  # Bloqueado por pieza propia

        return possibles

    def possible_positions_horizontal(self, row, col):
        possibles = []

        # Movimiento hacia la derecha
        for next_col in range(col + 1, 8):
            piece = self.__board__.get_piece(row, next_col)
            if piece is None:
                possibles.append((row, next_col))  # Casilla vacía
            elif piece.get_color() != self.get_color():
                possibles.append((row, next_col))  # Captura posible
                break  # Detener después de capturar
            else:
                break  # Bloqueado por pieza propia

        # Movimiento hacia la izquierda
        for next_col in range(col - 1, -1, -1):
            piece = self.__board__.get_piece(row, next_col)
            if piece is None:
                possibles.append((row, next_col))  # Casilla vacía
            elif piece.get_color() != self.get_color():
                possibles.append((row, next_col))  # Captura posible
                break  # Detener después de capturar
            else:
                break  # Bloqueado por pieza propia

        return possibles
