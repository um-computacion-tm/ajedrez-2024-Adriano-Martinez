from piece import Piece

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return"Qb"if self.__color__ == "white"else"qn"
