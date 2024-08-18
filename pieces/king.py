from .piece import Piece

class King(Piece):
    def get_symbol(self):
         return "KIb" if self.__color__ == "white" else "kin"
