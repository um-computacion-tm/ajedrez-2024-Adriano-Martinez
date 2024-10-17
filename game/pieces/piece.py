class Piece:
    def __init__(self, color, board):  
        """
        Inicializa una pieza con un color y un tablero.

        :param color: Color de la pieza (blanco o negro).
        :param board: Referencia al tablero en el que está la pieza.
        """
        self.__color__ = color  # Color de la pieza
        self.__board__ = board  # Referencia al tablero

    def get_color(self):
        """
        Devuelve el color de la pieza.

        :return: Color de la pieza.
        """
        return self.__color__

    def __str__(self):
        """
        Representación en cadena de la pieza.
        """
        return ""

    @staticmethod
    def is_position_valid(x, y):
        """
        Verifica si una posición está dentro de los límites del tablero.

        :param x: Coordenada x (fila).
        :param y: Coordenada y (columna).
        :return: True si la posición es válida, False en caso contrario.
        """
        return 0 <= x < 8 and 0 <= y < 8

    def mov_correcto(self, from_x, from_y, to_x, to_y):
        """
        Verifica si un movimiento es válido.

        :param from_x: Coordenada x de origen.
        :param from_y: Coordenada y de origen.
        :param to_x: Coordenada x de destino.
        :param to_y: Coordenada y de destino.
        :return: True si el movimiento es válido, False en caso contrario.
        :raises NotImplementedError: Si no se implementa en subclases específicas.
        """
        if not (self.is_position_valid(from_x, from_y) and self.is_position_valid(to_x, to_y)):
            return False  # Movimiento fuera del tablero
        if from_x == to_x and from_y == to_y:
            return False  # No se permite mover a la misma posición
        raise NotImplementedError("Implementar en subclases específicas.")

    def valid_positions(self, from_row, from_col, to_row, to_col):
        """
        Verifica si el destino está entre las posiciones válidas.

        :param from_row: Fila de origen.
        :param from_col: Columna de origen.
        :param to_row: Fila de destino.
        :param to_col: Columna de destino.
        :return: True si el destino es válido, False en caso contrario.
        """
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions  # Verifica si el destino está en las posiciones posibles

    def get_possible_positions(self, from_row, from_col):
        """
        Obtiene las posiciones ortogonales posibles para la pieza.

        :param from_row: Fila de origen.
        :param from_col: Columna de origen.
        :return: Lista de posiciones posibles.
        """
        return self.possible_orthogonal_positions(from_row, from_col)

    def possible_diagonal_positions(self, from_row, from_col):
        """
        Movimiento en diagonales.

        :param from_row: Fila de origen.
        :param from_col: Columna de origen.
        :return: Lista de posiciones diagonales posibles.
        """
        possibles = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Direcciones de movimiento en diagonal
        for step_row, step_col in directions:
            possibles += self.scan_direction(from_row, from_col, step_row, step_col)  # Escanea las direcciones diagonales
        return possibles

    def possible_orthogonal_positions(self, from_row, from_col):
        """
        Devuelve las posiciones posibles en líneas rectas (ortogonales).

        :param from_row: Fila de origen.
        :param from_col: Columna de origen.
        :return: Lista de posiciones ortogonales posibles.
        """
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Direcciones: arriba, abajo, derecha, izquierda
        possibles = []
        for step_row, step_col in directions:
            possibles += self.scan_direction(from_row, from_col, step_row, step_col)  # Escanea las direcciones ortogonales
        return possibles

    def scan_direction(self, from_row, from_col, row_increment, col_increment):
        """
        Explora posiciones en cualquier dirección.

        :param from_row: Fila de origen.
        :param from_col: Columna de origen.
        :param row_increment: Incremento de fila para la dirección.
        :param col_increment: Incremento de columna para la dirección.
        :return: Lista de posiciones posibles en la dirección explorada.
        """
        possibles = []
        row, col = from_row + row_increment, from_col + col_increment

        while self.is_position_valid(row, col):  # Continúa mientras la posición sea válida
            piece = self.__board__.get_piece(row, col)
            if piece is None:
                possibles.append((row, col))  # Agrega una casilla vacía como posible
            elif piece.get_color() != self.get_color():
                possibles.append((row, col))  # Agrega la casilla con pieza enemiga como posible captura
                break  # Detiene la exploración después de capturar
            else:
                break  # Detiene si hay una pieza propia bloqueando
            row += row_increment  # Avanza a la siguiente casilla en la dirección dada
            col += col_increment

        return possibles  # Devuelve las posiciones posibles en la dirección explorada.
