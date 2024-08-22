from .piece import Piece

class Rook(Piece):
    def __str__(self):
        return "♖" if self.__color__ == "WHITE" else "♜"




    def mover_pieza(self, from_row, from_col):
       if from_row == from_col:
           return [from_row, from_col + 1]
       elif from_row == from_col - 1:
           return [from_row, from_col - 1]
       elif from_row + 1 == from_col:
           return [from_row + 1, from_col]
       elif from_row - 1 == from_col:
           return [from_row - 1, from_col]  
       
