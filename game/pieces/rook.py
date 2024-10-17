from .piece import Piece
from game.exceptions import InvalidPieceMove

class Rook(Piece):
    def __init__(self, color, board):
        """
        Inicializa una torre con un color y un tablero.

        Args:
            color (str): El color de la torre, debe ser "WHITE" o "BLACK".
            board (Board): Referencia al tablero en el que se encuentra la torre.
        """
        super().__init__(color, board)

    def __str__(self):
        """
        Representación en cadena de la torre.

        Returns:
            str: Un símbolo que representa la torre, "♖" para blanca y "♜" para negra.
        """
        return "♖" if self.get_color() == "WHITE" else "♜"

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        """
        Verifica si el movimiento de la torre es válido.

        Args:
            from_x (int): La fila de la posición de origen.
            from_y (int): La columna de la posición de origen.
            to_x (int): La fila de la posición de destino.
            to_y (int): La columna de la posición de destino.

        Raises:
            InvalidPieceMove: Si el movimiento no es horizontal o vertical, 
                              o si el destino no es una posición ortogonal válida.

        Returns:
            bool: True si el movimiento es válido.
        """
        # Verificar que el movimiento es horizontal o vertical
        if from_x != to_x and from_y != to_y:
            raise InvalidPieceMove(piece_name="la Torre")
        
        # Usar la lógica para calcular las posiciones ortogonales válidas
        if (to_x, to_y) not in self.possible_orthogonal_positions(from_x, from_y):
            raise InvalidPieceMove(piece_name="la Torre")
        return True

