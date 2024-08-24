from .piece import Piece



class Pawn(Piece):
    def __str__(self):
        return "♙" if self.get_color() == "WHITE" else "♟"
    

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        ...
     