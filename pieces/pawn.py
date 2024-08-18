from .piece import Piece

class Pawn(Piece):
     def get_symbol(self):
        return "Pb" if self._color == "white" else "pn"
