from board import Board

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__history__ = []   # lista de movimientos 
        self.__game_over__ = False
    
    def is_playing(self):
        return True
    
    def parse_position(self, pos):
     if len(pos) != 2 or pos[0] not in 'abcdefgh' or pos[1] not in '12345678':
        raise ValueError("Posición inválida. Usa el formato 'e2'.")
    
     col = ord(pos[0]) - ord('a')  
     row = 8 - int(pos[1])  
     return row, col

    def move(self, from_row,from_col, to_row, to_col,): #MOVIMIENTO
        
        piece = self.__board__.get_piece(from_row, from_col)

        if piece is None:
            raise ValueError("No hay pieza en la posición de origen.")
        
        if piece.get_color() != self.__turn__:
            raise ValueError("No es tu turno para mover esta pieza.")
        
        is_valid, message = self.__board__.is_valid_move(from_row, from_col, to_row, to_col, piece)
        if not is_valid:
            raise ValueError(message)
        
        self.__board__.mover_pieza(from_row, from_col, to_row, to_col)
        self.__history__.append((from_row, from_col, to_row, to_col))
    
        self.change_turn()


    def validate_coords(self, from_row, from_col, to_row, to_col):
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Coordenadas fuera del rango. Deben estar entre 0 y 7.")


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

    def end_game(self):
        self.__game_over__ = True
        print("El juego ha terminado.")

