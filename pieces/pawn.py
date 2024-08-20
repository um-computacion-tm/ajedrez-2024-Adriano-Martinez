from .piece import Piece

class Pawn(Piece):
     def get_symbol(self):
        return "Pb" if self.__color__ == "white" else "pn"

     
       