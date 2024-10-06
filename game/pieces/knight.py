from .piece import Piece
from game.exceptions import InvalidPieceMove

class Knight(Piece):
    
    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♘" if self.get_color() == "WHITE" else "♞"
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verifica si el movimiento es a una posición válida
        if not self.valid_positions(from_x, from_y, to_x, to_y):
            raise InvalidPieceMove(piece_name="Caballo")

        # Verifica si el movimiento sigue el patrón en forma de L
        if (abs(to_x - from_x), abs(to_y - from_y)) not in [(2, 1), (1, 2)]:
            raise InvalidPieceMove(piece_name="Caballo")

        # Verifica si hay una pieza del mismo color en la posición de destino
        pieza_destino = self.__board__.get_piece(to_x, to_y)
        if pieza_destino and pieza_destino.get_color() == self.get_color():
            raise InvalidPieceMove("No puedes mover a una posición ocupada por tu propia pieza.")

        return True

    def get_possible_positions(self, from_row, from_col):
        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        positions = []

        for move in possible_moves:
            new_row = from_row + move[0]
            new_col = from_col + move[1]

            # Usa el método de la clase base para validar la posición
            if self.is_position_valid(new_row, new_col):
                positions.append((new_row, new_col))  # Agregar posición válida

        return positions
