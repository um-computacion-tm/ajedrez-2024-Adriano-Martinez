from game.pieces.rook import Rook
from game.pieces.piece import Piece
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.pawn import Pawn
from game.exceptions import OutOfBoard, PieceNotFound, InvalidMove, InvalidPieceMove

# Inicializar un tablero de 8x8, donde cada posición está vacía 
class Board:
    def __init__(self):
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()  # Configura las piezas al crear el tablero

    def setup_pieces(self):
        # Asignando posiciones de cada pieza negra
        self.__positions__[0][0] = Rook("BLACK", self)
        self.__positions__[0][1] = Knight("BLACK", self)
        self.__positions__[0][2] = Bishop("BLACK", self)
        self.__positions__[0][3] = Queen("BLACK", self)
        self.__positions__[0][4] = King("BLACK", self)
        self.__positions__[0][5] = Bishop("BLACK", self)
        self.__positions__[0][6] = Knight("BLACK", self)
        self.__positions__[0][7] = Rook("BLACK", self)

        # Inicializar peones negros
        self.initialize_pawns(1, "BLACK")

        # Asignando posiciones de cada pieza blanca
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

    def is_position_valid(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row, col):
        if not self.is_position_valid(row, col):
            raise OutOfBoard()
        
        piece = self.__positions__[row][col]
        return piece

    def set_piece(self, row, col, piece):
        if not self.is_position_valid(row, col):
            raise OutOfBoard()
        self.__positions__[row][col] = piece

    def remove_piece(self, row, col):
        # Verifica si la posición está fuera del tablero
        if not self.is_position_valid(row, col):
            raise OutOfBoard()  # Lanza la excepción si está fuera del tablero
        
        piece = self.get_piece(row, col)
        if piece is None:
            raise PieceNotFound()  # Lanza la excepción si no hay pieza en esa posición
        
        # Si todo es correcto, elimina la pieza
        self.set_piece(row, col, None)

    def mover_pieza(self, from_row, from_col, to_row, to_col):
        # Verifica si la posición de origen está fuera del tablero
        if not self.is_position_valid(from_row, from_col):
            raise OutOfBoard()

        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise PieceNotFound()

        # Verifica si la posición de destino está fuera del tablero
        if not self.is_position_valid(to_row, to_col):
            raise OutOfBoard()

        # Verifica si hay una pieza propia en la posición de destino
        target_piece = self.get_piece(to_row, to_col)
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise InvalidMove("No puedes mover a una posición ocupada por tu propia pieza.")

        # Verifica si el movimiento es válido
        try:
            is_valid, message = self.is_valid_move(from_row, from_col, to_row, to_col, piece)
        except InvalidPieceMove as e:
            raise

        if not is_valid:
            raise InvalidMove(message)

        # Mueve la pieza
        self.set_piece(to_row, to_col, piece)
        self.set_piece(from_row, from_col, None)

    def is_valid_move(self, from_row, from_col, to_row, to_col, piece):
        if not Piece.is_position_valid(from_row, from_col) or not Piece.is_position_valid(to_row, to_col):
            return False, "Coordenadas fuera del rango del tablero."
        
        destination_piece = self.get_piece(to_row, to_col)
        if destination_piece is not None and destination_piece.get_color() == piece.get_color():
            return False, "No puedes capturar tu propia pieza."
        
        if not piece.mov_correcto(from_row, from_col, to_row, to_col):
            return False, "Movimiento no válido para esta pieza."

        return True, "Movimiento válido."

    def count_pieces(self):
        white_count = 0
        black_count = 0
        for row in self.__positions__:
            for piece in row:
                if piece is not None:
                    if piece.get_color() == "WHITE":
                        white_count += 1
                    elif piece.get_color() == "BLACK":
                        black_count += 1
        return white_count, black_count
    
    def remove_all_pieces(self, color):
        # Elimina todas las piezas de un color del tablero.
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.get_color() == color:
                    self.remove_piece(row, col)  # Usa el nuevo método para eliminar piezas
    
    @staticmethod
    def get_piece_class(piece_type):
        piece_classes = {
            'rook': Rook,
            'knight': Knight,
            'bishop': Bishop,
            'queen': Queen,
            'king': King,
            'pawn': Pawn,
        }
        return piece_classes.get(piece_type.lower(), None)