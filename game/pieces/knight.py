from .piece import Piece
from game.exceptions import InvalidMoveKnightMove


class Knight(Piece):

    def __init__(self, color, board):
        super().__init__(color, board) 
        
    def __str__(self):
        return "♘" if self.__color__ == "WHITE" else "♞"
    

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verifica si el movimiento sigue el patrón en forma de L
        if (abs(to_x - from_x), abs(to_y - from_y)) not in [(2, 1), (1, 2)]:
            raise InvalidMoveKnightMove("Movimiento inválido para el caballo.")

        # Verifica si hay una pieza del mismo color en la posición de destino
        pieza_destino = self.__board__.get_piece(to_x, to_y)
        if pieza_destino and pieza_destino.get_color() == self.__color__:
            raise InvalidMoveKnightMove("No se puede capturar una pieza propia.")

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

            if self.__is_valid_position(new_row, new_col):
                positions.append((new_row, new_col))

        return positions

    def __is_valid_position(self, row, col):
        # Verifica si la posición está dentro del rango válido del tablero
        return 0 <= row < 8 and 0 <= col < 8