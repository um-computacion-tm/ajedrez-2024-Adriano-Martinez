from .piece import Piece
from game.exceptions import InvalidPieceMove

class King(Piece):
    def __init__(self, color, board):
        """
        Inicializa un rey con un color y un tablero.

        Args:
            color (str): El color del rey, debe ser "WHITE" o "BLACK".
            board (Board): Referencia al tablero en el que se encuentra el rey.
        """
        super().__init__(color, board) 
        
    def __str__(self):
        """
        Representación en cadena del rey.

        Returns:
            str: Un símbolo que representa el rey, "♔" para blanco y "♚" para negro.
        """
        return "♔" if self.get_color() == "WHITE" else "♚"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        """
        Verifica si el movimiento del rey es válido.

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
        # Verificar si el movimiento está dentro de las posiciones válidas
        if not self.valid_positions(from_x, from_y, to_x, to_y):
            raise InvalidPieceMove(piece_name="el Rey")

        # Si el movimiento es válido, devuelve True
        return True

    def get_possible_positions(self, from_row, from_col):
        """
        Obtiene las posiciones posibles a las que puede moverse el rey.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.

        Returns:
            list: Una lista de tuplas que representan las posiciones posibles a las que puede moverse el rey.
        """
        possibles = []
        # Considera todas las posiciones adyacentes
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                to_row, to_col = from_row + dx, from_col + dy
                if self.is_position_valid(to_row, to_col):
                    if not self.__is_blocked_by_own_piece(to_row, to_col):
                        possibles.append((to_row, to_col))
        
        return possibles

    def __is_blocked_by_own_piece(self, x, y):
        """
        Verifica si una posición está bloqueada por una pieza del mismo color.

        Args:
            x (int): La fila de la posición a verificar.
            y (int): La columna de la posición a verificar.

        Returns:
            bool: True si hay una pieza del mismo color en la posición; de lo contrario, False.
        """
        piece = self.__board__.get_piece(x, y)
        return piece is not None and piece.get_color() == self.get_color()
