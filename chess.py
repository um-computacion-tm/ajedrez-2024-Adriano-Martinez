from board import Board
from .pieces.pawn import Pawn
from .pieces.queen import Queen
from .pieces.rook import Rook
from .pieces.knight import Knight
from .pieces.bishop import Bishop
from .pieces.king import King

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"
        self.history = []   # lista de movimientos 

    def move(self, from_row,from_col, to_row, to_col,): #MOVIMIENTO

        # validate coords 
        piece = self.board.get_piece(from_row, from_col)

        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Coordenadas fuera del rango del tablero.")

        if piece is None:
            raise ValueError("No hay pieza en la posición de origen.")
        
        if piece.get_color() != self.turn:
         raise ValueError("No es tu turno para mover esta pieza.")
        
        # Validar el movimiento de la pieza
        if not piece.is_valid_move(from_row, from_col, to_row, to_col, self.board):
            raise ValueError("Movimiento no válido para esta pieza.")
        
      # Mover la pieza en el tablero
        self.board.move_piece(from_row, from_col, to_row, to_col)
        self.history.append((from_row, from_col, to_row, to_col))
        
        self.change_turn()
    
        
    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK" #cambia a negro
        else:
            self.__turn__ = "WHITE" #cambia a blanco
        print(f"Es el turno de {self.__turn__}") # Muestra de quien es el turno

