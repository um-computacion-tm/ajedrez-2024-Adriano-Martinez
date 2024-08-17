from piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def __str__(self):
        return"KIb"if self.__color__ == "white"else"kin"
