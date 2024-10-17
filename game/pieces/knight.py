from .piece import Piece
from game.exceptions import InvalidPieceMove

class Knight(Piece):
    def __init__(self, color, board):
        """
        Inicializa un caballo con un color y un tablero.

        Args:
            color (str): El color del caballo, debe ser "WHITE" o "BLACK".
            board (Board): Referencia al tablero en el que se encuentra el caballo.
        """
        super().__init__(color, board) 
        
    def __str__(self):
        """
        Representación en cadena del caballo.

        Returns:
            str: Un símbolo que representa el caballo, "♘" para blanco y "♞" para negro.
        """
        return "♘" if self.get_color() == "WHITE" else "♞"
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        """
        Verifica si el movimiento del caballo es válido.

        Args:
            from_x (int): La fila de la posición de origen.
            from_y (int): La columna de la posición de origen.
            to_x (int): La fila de la posición de destino.
            to_y (int): La columna de la posición de destino.

        Raises:
            InvalidPieceMove: Si el movimiento no es válido o si el destino está ocupado por una pieza del mismo color.

        Returns:
            bool: True si el movimiento es válido.
        """
        # Verifica si el movimiento es a una posición válida
        if not self.valid_positions(from_x, from_y, to_x, to_y):
            raise InvalidPieceMove(piece_name="el Caballo")

        # Verifica si hay una pieza del mismo color en la posición de destino
        pieza_destino = self.__board__.get_piece(to_x, to_y)
        if pieza_destino and pieza_destino.get_color() == self.get_color():
            raise InvalidPieceMove("No puedes mover a una posición ocupada por tu propia pieza.")

        return True

    def get_possible_positions(self, from_row, from_col):
        """
        Obtiene las posiciones posibles a las que puede moverse el caballo.

        Args:
            from_row (int): La fila de la posición de origen.
            from_col (int): La columna de la posición de origen.

        Returns:
            list: Una lista de tuplas que representan las posiciones posibles a las que puede moverse el caballo.
        """
        possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        positions = []

        for move in possible_moves:
            new_row = from_row + move[0]
            new_col = from_col + move[1]

            # Usa el método de la clase base para validar la posición
            if self.is_position_valid(new_row, new_col):
                positions.append((new_row, new_col))  # Agregar posición válida

        return positions
