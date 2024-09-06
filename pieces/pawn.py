from .piece import Piece
from exceptions import InvalidMovePawnMove



class Pawn(Piece):
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"
    

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        direction = 1 if self.__color__ == "WHITE" else -1  
        start_row = 1 if self.__color__ == "WHITE" else 6  

        # Movimiento hacia adelante 
        if from_x == to_x:
            # Avance de una casilla
            if to_y == from_y + direction:
                if self.__board__.get_piece(to_x, to_y) is None:
                    return True
                else:
                    raise InvalidMovePawnMove("No puede capturar moviéndose hacia adelante.")
            # Avance de dos casillas (solo fila inicial)
            elif from_y == start_row and to_y == from_y + 2 * direction:
                if self.__board__.get_piece(to_x, to_y) is None and self.__board__.get_piece(to_x, from_y + direction) is None:
                    return True
                else:
                    raise InvalidMovePawnMove("El camino está bloqueado.")
        
        # Captura diagonal
        elif abs(from_x - to_x) == 1 and to_y == from_y + direction:
            target_piece = self.__board__.get_piece(to_x, to_y)
            if target_piece is not None and target_piece.get_color() != self.__color__:
                return True
            else:
                raise InvalidMovePawnMove("Solo puede capturar en diagonal.")
        
        # Solo si no cumple ninguna de las reglas anteriores
        raise InvalidMovePawnMove("Movimiento no válido para el peón.")
     