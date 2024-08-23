from .piece import Piece



class Pawn(Piece):
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"
    

    def mov_correcto(self, x, y):
        ...