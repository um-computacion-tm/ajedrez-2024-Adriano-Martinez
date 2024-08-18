from .piece import Piece

class Bishop(Piece):
    def get_symbol(self):
      return "Bb" if self.__color__ == "white" else "bn"