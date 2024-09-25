from game.pieces.rook import Rook
from game.pieces.piece import Piece
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.pawn import Pawn
from game.exceptions import OutOfBoard, InvalidMoveNoPiece, InvalidMove

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
        self.__positions__[0][0] = Rook("BLACK", self)           # Torre, caballo, alfil, reina y rey
        self.__positions__[0][1] = Knight("BLACK", self)
        self.__positions__[0][2] = Bishop("BLACK", self)
        self.__positions__[0][3] = Queen("BLACK", self)
        self.__positions__[0][4] = King("BLACK", self)
        self.__positions__[0][5] = Bishop("BLACK", self)
        self.__positions__[0][6] = Knight("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)

     # Inicializar peones negros
        self.initialize_pawns(1, "BLACK")

     # Asignando posiciones de cada pieza blanca (fila 0 y 1)     
        self.__positions__[7][0] = Rook("WHITE", self)
        self.__positions__[7][1] = Knight("WHITE", self)
        self.__positions__[7][2] = Bishop("WHITE", self)
        self.__positions__[7][3] = Queen("WHITE", self)
        self.__positions__[7][4] = King("WHITE", self)
        self.__positions__[7][5] = Bishop("WHITE", self)
        self.__positions__[7][6] = Knight("WHITE", self)
        self.__positions__[7][7] = Rook("WHITE", self)
    
    # Inicializar peones blancos
        self.initialize_pawns(6, "WHITE")


    def initialize_pawns(self, row, color):
        for i in range(8):
            self.__positions__[row][i] = Pawn(color, self)

        
    def __str__(self):
        board_str = "  a b c d e f g h\n"
        for i, row in enumerate(self.__positions__):
            row_label = str(8 - i)  # Etiquetas de filas 8-1
            row_str = row_label + " "  # Agregar etiqueta de fila
            for cell in row:
                if cell is not None:
                    row_str += str(cell) + " "
                else:
                    row_str += ". "
            board_str += row_str + "\n"
        return board_str


# Devuelve la pieza en la posicion segun cada pieza
    def get_piece(self, row, col):
        if not (
            0 <= row < 8 and 0 <= col < 8
        ):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        self.__positions__[row][col] = piece
    
    def mover_pieza(self, from_row, from_col, to_row, to_col):
     piece = self.get_piece(from_row, from_col)
     if piece is None:
        raise InvalidMoveNoPiece()  # Lanza la excepción personalizada
    
     is_valid, message = self.is_valid_move(from_row, from_col, to_row, to_col, piece)
     if not is_valid:
        raise InvalidMove(message)  # Lanza la excepción personalizada

    # Mueve la pieza si el movimiento es válido 
     self.set_piece(to_row, to_col, piece)
     self.set_piece(from_row, from_col, None)

    def is_valid_move(self, from_row, from_col, to_row, to_col, piece):
     if not (Piece.is_position_valid(from_row, from_col) and Piece.is_position_valid(to_row, to_col)):
       return False, "Coordenadas fuera del rango del tablero."
    
     destination_piece = self.get_piece(to_row, to_col)
     if destination_piece is not None and destination_piece.get_color() == piece.get_color():
       return False, "No puedes capturar tu propia pieza."
    
     if not piece.mov_correcto(from_row, from_col, to_row, to_col):
       return False, "Movimiento no válido para esta pieza."

     return True, "Movimiento válido."
    
    def get_all_pieces(self, color):
     pieces = []
     for row in self.__positions__:
        for piece in row:
            if piece is not None and piece.get_color() == color:
                pieces.append(piece)
     return pieces