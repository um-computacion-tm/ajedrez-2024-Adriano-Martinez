from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__history__ = []   # lista de movimientos 
    
    def is_playing(self):
        return True

    def move(self, from_row,from_col, to_row, to_col,): #MOVIMIENTO
        # validate coords 
        piece = self.__board__.get_piece(from_row, from_col)
        
        if piece is None:
            raise ValueError("No hay pieza en la posición de origen.")
        
        if piece.get_color() != self.__turn__:
            raise ValueError("No es tu turno para mover esta pieza.")
        
        is_valid, message = self.__board__.is_valid_move(from_row, from_col, to_row, to_col, piece)
        if not is_valid:
            raise ValueError(message)
        
        self.__board__.move_piece(from_row, from_col, to_row, to_col)
        self.__history__.append((from_row, from_col, to_row, to_col))
    
        self.change_turn()

    def show_board(self):
        return str(self.__board__)
    
    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK" #cambia a negro
        else:
            self.__turn__ = "WHITE" #cambia a blanco
        print(f"Es el turno de {self.__turn__}") # Muestra de quien es el turno

