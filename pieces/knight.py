from .piece import Piece

class Knight(Piece):
    def get_symbol(self):
        return "Kb" if self.__color__ == "white" else "kn"