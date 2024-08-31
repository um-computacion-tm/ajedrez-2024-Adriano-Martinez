from .piece import Piece
from exceptions import InvalidMoveNoPiece, InvalidMoveRookMove

class Rook(Piece):
    def __str__(self):
        return "♖" if self.__color__ == "WHITE" else "♜"
   
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        # Verifica si la torre no se mueve
        if from_x == to_x and from_y == to_y:
            raise InvalidMoveRookMove("La torre debe moverse a una posición diferente.")
        
        if from_x == to_x:  # Movimiento vertical
            self._check_path(from_x, from_y, to_x, to_y, vertical=True)
        elif from_y == to_y:  # Movimiento horizontal
            self._check_path(from_x, from_y, to_x, to_y, vertical=False)
        else:
            raise InvalidMoveRookMove("Movimiento no válido para la torre.")
        
        return True
    
    def _check_path(self, from_x, from_y, to_x, to_y, vertical):
        if vertical:
            step = 1 if to_y > from_y else -1
            for y in range(from_y + step, to_y, step):
                piece = self.__board__.get_piece(from_x, y)
                if piece is not None:
                    raise InvalidMoveRookMove("Movimiento bloqueado por otra pieza.")
        else:
            step = 1 if to_x > from_x else -1
            for x in range(from_x + step, to_x, step):
                piece = self.__board__.get_piece(x, from_y)
                if piece is not None:
                    raise InvalidMoveRookMove("Movimiento bloqueado por otra pieza.")

