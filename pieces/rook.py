from .piece import Piece

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return"Rb"if self.__color__ == "white"else"rn"