from game.pieces.rook import Rook
from game.pieces.piece import Piece
from game.pieces.knight import Knight
from game.pieces.bishop import Bishop
from game.pieces.queen import Queen
from game.pieces.king import King
from game.pieces.pawn import Pawn
from game.exceptions import OutOfBoard, PieceNotFound, InvalidMove, InvalidPieceMove

class Board:
    """
    Representa el tablero de ajedrez, compuesto por una matriz 8x8 donde cada posición puede contener una pieza o estar vacía.
    """
    def __init__(self):
        """Inicializa el tablero de ajedrez con una disposición vacía y luego configura las piezas en sus posiciones iniciales."""
        self.__positions__ = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces() 

    def setup_pieces(self):
        """Configura las piezas de ajedrez en sus posiciones iniciales para ambos colores."""
        # Posiciones de piezas negras
        self.__positions__[0][0] = Rook("BLACK", self)   #torre
        self.__positions__[0][1] = Knight("BLACK", self)  #caballo
        self.__positions__[0][2] = Bishop("BLACK", self)  #alfil
        self.__positions__[0][3] = Queen("BLACK", self)   #reina
        self.__positions__[0][4] = King("BLACK", self)    #rey
        self.__positions__[0][5] = Bishop("BLACK", self)  #alfil
        self.__positions__[0][6] = Knight("BLACK", self)  #caballo
        self.__positions__[0][7] = Rook("BLACK", self)    #torre

        # Inicializar peones negros
        self.initialize_pawns(1, "BLACK")

        # Posiciones de piezas blancas
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
        """
        Inicializa una fila de peones en la fila dada para el color especificado.
        
        Args:
            row (int): Fila donde se colocarán los peones.
            color (str): Color de los peones ("WHITE" o "BLACK").
        """
        for i in range(8):
            self.__positions__[row][i] = Pawn(color, self)

    def __str__(self):
        """
        Retorna una representación en cadena del tablero de ajedrez.

        Returns:
            str: Representación textual del tablero.
        """
        board_str = "  a b c d e f g h\n"
        for i, row in enumerate(self.__positions__):
            row_label = str(8 - i)
            row_str = row_label + " "
            for cell in row:
                row_str += str(cell) + " " if cell else ". "
            board_str += row_str + "\n"
        return board_str

    def is_position_valid(self, row, col):
        """
        Verifica si una posición (fila, columna) está dentro de los límites del tablero.
        
        Args:
            row (int): Fila de la posición.
            col (int): Columna de la posición.
        
        Returns:
            bool: True si la posición es válida, False de lo contrario.
        """
        return 0 <= row < 8 and 0 <= col < 8

    def get_piece(self, row, col):
        """
        Obtiene la pieza en la posición especificada.

        Args:
            row (int): Fila de la pieza.
            col (int): Columna de la pieza.
        
        Returns:
            Piece: La pieza en la posición dada, o None si está vacía.
        
        Raises:
            OutOfBoard: Si la posición está fuera del tablero.
        """
        if not self.is_position_valid(row, col):
            raise OutOfBoard()
        return self.__positions__[row][col]

    def set_piece(self, row, col, piece):
        """
        Coloca una pieza en la posición dada.

        Args:
            row (int): Fila donde colocar la pieza.
            col (int): Columna donde colocar la pieza.
            piece (Piece): Pieza a colocar.
        
        Raises:
            OutOfBoard: Si la posición está fuera del tablero.
        """
        if not self.is_position_valid(row, col):
            raise OutOfBoard()
        self.__positions__[row][col] = piece

    def remove_piece(self, row, col):
        """
        Elimina una pieza de una posición específica en el tablero.

        Args:
            row (int): Fila de la pieza a eliminar.
            col (int): Columna de la pieza a eliminar.
        
        Raises:
            OutOfBoard: Si la posición está fuera del tablero.
            PieceNotFound: Si no hay pieza en la posición indicada.
        """
        if not self.is_position_valid(row, col):
            raise OutOfBoard()

        piece = self.get_piece(row, col)
        if piece is None:
            raise PieceNotFound()

        self.set_piece(row, col, None)

    def mover_pieza(self, from_row, from_col, to_row, to_col):
        """
        Mueve una pieza de una posición a otra en el tablero.

        Args:
            from_row (int): Fila de origen.
            from_col (int): Columna de origen.
            to_row (int): Fila de destino.
            to_col (int): Columna de destino.
        
        Raises:
            OutOfBoard: Si las posiciones de origen o destino están fuera del tablero.
            PieceNotFound: Si no hay pieza en la posición de origen.
            InvalidMove: Si el movimiento no es válido según las reglas del juego.
        """
        if not self.is_position_valid(from_row, from_col) or not self.is_position_valid(to_row, to_col):
            raise OutOfBoard()

        piece = self.get_piece(from_row, from_col)
        if piece is None:
            raise PieceNotFound()

        target_piece = self.get_piece(to_row, to_col)
        if target_piece is not None and target_piece.get_color() == piece.get_color():
            raise InvalidMove("No puedes mover a una posición ocupada por tu propia pieza.")

        try:
            piece.mov_correcto(from_row, from_col, to_row, to_col)
        except InvalidPieceMove as e:
            raise InvalidMove(str(e))

        self.set_piece(to_row, to_col, piece)
        self.set_piece(from_row, from_col, None)

    def count_pieces(self):
        """
        Cuenta el número de piezas de cada color en el tablero.
        """
        white_count = 0
        black_count = 0
        for row in self.__positions__:
            for piece in row:
                if piece:
                    if piece.get_color() == "WHITE":
                        white_count += 1
                    elif piece.get_color() == "BLACK":
                        black_count += 1
        return white_count, black_count

    def remove_all_pieces(self, color):
        """
        Elimina todas las piezas de un color específico del tablero.
        """
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.get_color() == color:
                    self.remove_piece(row, col)

    