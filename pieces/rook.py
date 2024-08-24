from .piece import Piece

class Rook(Piece):
    def __str__(self):
        return "♖" if self.__color__ == "WHITE" else "♜"
   
 
 
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        return from_x == to_x or from_y == to_y