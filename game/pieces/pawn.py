from .piece import Piece
from game.exceptions import InvalidPieceMove

class Pawn(Piece):
    def __init__(self, color, board):
        """
        Inicializa un peón con un color y un tablero.

        Args:
            color (str): El color del peón, debe ser "WHITE" o "BLACK".
            board (Board): Referencia al tablero en el que se encuentra el peón.
        """
        super().__init__(color, board)
        
    def __str__(self):
        """
        Representación en cadena del peón.

        Returns:
            str: Un símbolo que representa el peón, "♙" para blanco y "♟" para negro.
        """
        return "♙" if self.get_color() == "WHITE" else "♟"
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        """
        Verifica si el movimiento del peón es válido.

        Args:
            from_x (int): La fila de la posición de origen.
            from_y (int): La columna de la posición de origen.
            to_x (int): La fila de la posición de destino.
            to_y (int): La columna de la posición de destino.

        Raises:
            InvalidPieceMove: Si el movimiento no es válido.

        Returns:
            bool: True si el movimiento es válido.
        """
        # Verificar que las posiciones son válidas
        if not (self.is_position_valid(from_x, from_y) and self.is_position_valid(to_x, to_y)):
            raise InvalidPieceMove(piece_name="el Peón")
        
        direction = -1 if self.get_color() == "WHITE" else 1
        start_row = 6 if self.get_color() == "WHITE" else 1

        # Agrupar posiciones en tuplas
        from_pos = (from_x, from_y)
        to_pos = (to_x, to_y)

        # Movimiento hacia adelante
        if self.is_forward_move(from_pos, to_pos, direction, start_row):
            return True
        
        # Captura diagonal
        if self.is_diagonal_capture(from_pos, to_pos, direction):
            return True

        # Si el movimiento no es válido
        raise InvalidPieceMove(piece_name="el Peón")

    def is_forward_move(self, from_pos, to_pos, direction, start_row):
        """
        Verifica si el movimiento es un avance hacia adelante.

        Args:
            from_pos (tuple): La posición de origen como (fila, columna).
            to_pos (tuple): La posición de destino como (fila, columna).
            direction (int): Dirección del movimiento (1 o -1).
            start_row (int): Fila de inicio para el peón.

        Returns:
            bool: True si el movimiento es hacia adelante, False en caso contrario.
        """
        from_x, from_y = from_pos
        to_x, to_y = to_pos
        if to_y == from_y:  # Movimiento vertical
            if to_x == from_x + direction and self.__board__.get_piece(to_x, to_y) is None:
                return True
            if from_x == start_row and to_x == from_x + 2 * direction and self.__board__.get_piece(from_x + direction, from_y) is None:
                return True
        return False

    def is_diagonal_capture(self, from_pos, to_pos, direction):
        """
        Verifica si el movimiento es una captura diagonal.

        Args:
            from_pos (tuple): La posición de origen como (fila, columna).
            to_pos (tuple): La posición de destino como (fila, columna).
            direction (int): Dirección del movimiento (1 o -1).

        Returns:
            bool: True si el movimiento es una captura diagonal, False en caso contrario.
        """
        from_x, from_y = from_pos
        to_x, to_y = to_pos
        if abs(to_y - from_y) == 1 and to_x == from_x + direction:
            other_piece = self.__board__.get_piece(to_x, to_y)
            return other_piece is not None and other_piece.get_color() != self.get_color()
        return False

    def get_possible_positions(self, from_row, from_col):
        """
        Obtiene las posiciones posibles a las que puede moverse el peón.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.

        Returns:
            list: Una lista de tuplas que representan las posiciones posibles a las que puede moverse el peón.
        """
        possibles = self.get_possible_positions_move(from_row, from_col)
        possibles.extend(self.get_possible_positions_eat(from_row, from_col))
        return possibles

    def get_possible_positions_eat(self, from_row, from_col):
        """
        Obtiene las posiciones donde el peón puede capturar.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.

        Returns:
            list: Una lista de tuplas que representan las posiciones donde el peón puede capturar.
        """
        possibles = []
        direction = 1 if self.get_color() == "BLACK" else -1
        for col in [from_col - 1, from_col + 1]:
            if 0 <= col < 8:
                other_piece = self.__board__.get_piece(from_row + direction, col)
                if other_piece and other_piece.get_color() != self.get_color():
                    possibles.append((from_row + direction, col))
        return possibles

    def get_possible_positions_move(self, from_row, from_col):
        """
        Obtiene las posiciones a las que el peón puede moverse sin capturar.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.

        Returns:
            list: Una lista de tuplas que representan las posiciones a las que el peón puede moverse.
        """
        possibles = []
        direction = 1 if self.get_color() == "BLACK" else -1
        start_row = 1 if self.get_color() == "BLACK" else 6
        if self.__board__.get_piece(from_row + direction, from_col) is None:
            possibles.append((from_row + direction, from_col))
            if from_row == start_row and self.__board__.get_piece(from_row + 2 * direction, from_col) is None:
                possibles.append((from_row + 2 * direction, from_col))
        return possibles
