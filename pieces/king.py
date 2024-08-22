from .piece import Piece

class King(Piece):
    def __str__(self):
        return "♔" if self.__color__ == "WHITE" else "♚"
