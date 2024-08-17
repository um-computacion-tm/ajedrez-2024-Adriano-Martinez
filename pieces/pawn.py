from .piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return"Pb"if self.__color__ == "white"else"pn"
