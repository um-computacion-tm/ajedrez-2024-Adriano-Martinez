from .piece import Piece

class Rook(Piece):
    def get_symbol(self):
     return "Rb" if self.__color__ == "white" else "rn"