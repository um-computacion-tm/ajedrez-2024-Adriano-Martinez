from .piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return"Bb"if self.__color__ == "white"else"bn"