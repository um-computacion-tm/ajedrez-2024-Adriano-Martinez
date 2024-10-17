from .piece import Piece
from game.exceptions import InvalidPieceMove

class Queen(Piece):
    def __init__(self, color, board):
        """
        Inicializa una reina con un color y un tablero.

        Args:
            color (str): El color de la reina, debe ser "WHITE" o "BLACK".
            board (Board): Referencia al tablero en el que se encuentra la reina.
        """
        super().__init__(color, board)
        
    def __str__(self):
        """
        Representación en cadena de la reina.

        Returns:
            str: Un símbolo que representa la reina, "♕" para blanca y "♛" para negra.
        """
        return "♕" if self.get_color() == "WHITE" else "♛"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        """
        Verifica si el movimiento de la reina es válido.

        Args:
            from_x (int): La fila de la posición de origen.
            from_y (int): La columna de la posición de origen.
            to_x (int): La fila de la posición de destino.
            to_y (int): La columna de la posición de destino.

        Raises:
            InvalidPieceMove: Si el destino no es una posición ortogonal o diagonal válida.

        Returns:
            bool: True si el movimiento es válido.
        """
        # Combina las posibles posiciones ortogonales y diagonales
        possible_positions = (
            self.possible_orthogonal_positions(from_x, from_y) +
            self.possible_diagonal_positions(from_x, from_y)
        )

        # Verifica si el destino está dentro de las posiciones válidas
        if (to_x, to_y) not in possible_positions:
            raise InvalidPieceMove(piece_name="la Reina")

        return True

    def get_possible_positions(self, from_row, from_col):
        """
        Obtiene las posiciones posibles para la reina, combinando movimientos ortogonales y diagonales.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.

        Returns:
            list: Una lista de tuplas que representan las posiciones posibles a las que puede moverse la reina.
        """
        # Combina los movimientos ortogonales y diagonales posibles
        return self.possible_orthogonal_positions(from_row, from_col) + self.possible_diagonal_positions(from_row, from_col)
