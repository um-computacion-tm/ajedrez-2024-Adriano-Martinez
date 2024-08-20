from pieces.rook import Rook
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from pieces.pawn import Pawn

# Inicializar un tablero de 8x8, donde cada posicion esta vacia 
class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
# Asignando posiciones de cada pieza negra
        self.__positions__[0][0] = Rook("BLACK")           # Torre, caballo, alfil, rebina y rey
        self.__positions__[0][1] = Knight("BLACK")
        self.__positions__[0][2] = Bishop("BLACK")
        self.__positions__[0][3] = Queen("BLACK")
        self.__positions__[0][4] = King("BLACK")
        self.__positions__[0][5] = Bishop("BLACK")
        self.__positions__[0][6] = Knight("BLACK")
        self.__positions__[0][7] = Rook("BLACK")
# Se crea una lista con 8 peones negros y se les asigna en la fila 1 
        self.__positions__[1] = [Pawn("BLACK") for _ in range(8)]
# # Asignando posiciones de cada pieza blanca (fila 0 y 1)     
        self.__positions__[7][0] = Rook("WHITE") 
        self.__positions__[7][1] = Knight("WHITE")
        self.__positions__[7][2] = Bishop("WHITE")
        self.__positions__[7][3] = Queen("WHITE")
        self.__positions__[7][4] = King("WHITE")
        self.__positions__[7][5] = Bishop("WHITE")
        self.__positions__[7][6] = Knight("WHITE")
        self.__positions__[7][7] = Rook("WHITE")
        self.__positions__[6] = [Pawn("WHITE") for _ in range(8)]
# Devuelve la pieza en la posicion segun cada pieza
    def get_piece(self, row, col):
        return self.__positions__[row][col]
    
    def move_piece(self, from_row, from_col, to_row, to_col):
     piece = self.get_piece(from_row, from_col)
     if piece is not None:
        self.__positions__[to_row][to_col] = piece
        self.__positions__[from_row][from_col] = None