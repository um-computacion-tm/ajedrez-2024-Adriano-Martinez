from .piece import Piece
from exceptions import InvalidMoveBishopMove

class Bishop(Piece):
    def __str__(self):
        return "♗" if self.__color__ == "WHITE" else "♝"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verifica que el movimiento sea diagonal
        if abs(to_x - from_x) != abs(to_y - from_y):
            raise InvalidMoveBishopMove("Movimiento no válido para el alfil.")
        
        # Verifica que el camino esté despejado
        direction_x = 1 if to_x > from_x else -1
        direction_y = 1 if to_y > from_y else -1
        x, y = from_x + direction_x, from_y + direction_y

        while x != to_x and y != to_y:
            piece = self.__board__.get_piece(x, y)
            if piece is not None:
                if piece.get_color() == self.get_color():
                    raise InvalidMoveBishopMove("Movimiento bloqueado por una pieza propia.")
                else:
                    raise InvalidMoveBishopMove("Movimiento bloqueado por una pieza rival.")
            x += direction_x
            y += direction_y
        
        return True

    def get_possible_positions(self, from_row, from_col):
     possibles = []

    # Define las cuatro direcciones diagonales
     directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    
     for step_row, step_col in directions:
        row, col = from_row + step_row, from_col + step_col
        while 0 <= row < 8 and 0 <= col < 8:
            piece = self.__board__.get_piece(row, col)
            if piece is None:
                possibles.append((row, col))  # Casilla vacía, movimiento válido
            elif piece.get_color() != self.get_color():
                possibles.append((row, col))  # Captura posible
                break  # Se detiene después de capturar una pieza
            else:
                break  # Movimiento bloqueado por una pieza propia
            row += step_row
            col += step_col

     return possibles


     


