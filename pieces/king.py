from .piece import Piece


class King(Piece):
    def __str__(self):
        return "♔" if self.__color__ == "WHITE" else "♚"
    


    def mov_correcto(self, from_x, from_y, to_x, to_y):
        return max(abs(from_x - to_x), abs(from_y - to_y)) == 1