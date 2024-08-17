from .piece import Piece

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return"Kb"if self.__color__ == "white"else"kn"