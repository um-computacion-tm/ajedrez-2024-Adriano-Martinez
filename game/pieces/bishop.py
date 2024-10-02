from .piece import Piece
from game.exceptions import InvalidPieceMove

class Bishop(Piece):
    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♗" if self.__color__ == "WHITE" else "♝"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if not (abs(to_x - from_x) == abs(to_y - from_y)):
            raise InvalidPieceMove("el alfil", "Movimiento no válido para el alfil.")
        
        # Verifica el camino
        direction_x = 1 if to_x > from_x else -1
        direction_y = 1 if to_y > from_y else -1
        x, y = from_x + direction_x, from_y + direction_y

        while (x != to_x) and (y != to_y):
            piece = self.__board__.get_piece(x, y)
            if piece is not None:
                raise InvalidPieceMove("el alfil", "Movimiento bloqueado por una pieza.")
            x += direction_x
            y += direction_y

        return True  # Movimiento válido

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



