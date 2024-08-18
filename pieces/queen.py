from .piece import Piece

class Queen(Piece):
    def get_symbol(self):
      return "Qw" if self.__color__ == "white" else "qn"