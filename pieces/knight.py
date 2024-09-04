from .piece import Piece
from exceptions import InvalidMoveKnightMove


class Knight(Piece):
    def __str__(self):
        return "♘" if self.__color__ == "WHITE" else "♞"
    
        
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        if (abs(to_x - from_x), abs(to_y - from_y)) not in [(2, 1), (1, 2)]:
            raise InvalidMoveKnightMove("Movimiento inválido para el caballo.")

        # Verifica si hay una pieza del mismo color en la posición de destino
        pieza_destino = self.__board__.get_piece(to_x, to_y)
        if pieza_destino and pieza_destino.get_color() == self.__color__:
            raise InvalidMoveKnightMove("No se puede capturar una pieza propia.")

        return True