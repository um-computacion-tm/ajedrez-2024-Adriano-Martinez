class Piece:  
    def __init__(self, color, board):  # Inicializa una pieza con un color y un tablero
        self.__color__ = color  # Color de la pieza (blanco o negro)
        self.__board__ = board  # Referencia al tablero en el que está la pieza

    def get_color(self):  # Devuelve el color de la pieza
        return self.__color__

    def __str__(self):  # Representación en cadena de la pieza.
        return ""

    @staticmethod
    def is_position_valid(x, y):  # Verifica si una posición está dentro de los límites del tablero
        return 0 <= x < 8 and 0 <= y < 8

    def mov_correcto(self, from_x, from_y, to_x, to_y):  # Verifica si un movimiento es válido 
        if not (self.is_position_valid(from_x, from_y) and self.is_position_valid(to_x, to_y)):
            return False  # Movimiento fuera del tablero
        if from_x == to_x and from_y == to_y:
            return False  # No se permite mover a la misma posición
        raise NotImplementedError("Implementar en subclases específicas.")  

    def valid_positions(self, from_row, from_col, to_row, to_col):  # Verifica si el destino está entre las posiciones válidas
        possible_positions = self.get_possible_positions(from_row, from_col)
        return (to_row, to_col) in possible_positions  # Verifica si el destino está en las posiciones posibles
    
    # Obtiene las posiciones ortogonales posibles para la pieza
    def get_possible_positions(self, from_row, from_col):  
        return self.possible_orthogonal_positions(from_row, from_col)

    # Movimiento en diagonales
    def possible_diagonal_positions(self, from_row, from_col):  
        possibles = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # Direcciones de movimiento en diagonal
        for step_row, step_col in directions:
            possibles += self.scan_direction(from_row, from_col, step_row, step_col)  # Escanea las direcciones diagonales
        return possibles

    # Movimiento en líneas rectas (ortogonales)
    def possible_orthogonal_positions(self, from_row, from_col):  # Devuelve las posiciones posibles en líneas rectas
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Direcciones: arriba, abajo, derecha, izquierda
        possibles = []
        for step_row, step_col in directions:
            possibles += self.scan_direction(from_row, from_col, step_row, step_col)  # Escanea las direcciones ortogonales
        return possibles

    # Exploración de posiciones en cualquier dirección
    def scan_direction(self, from_row, from_col, row_increment, col_increment):  # Explora posiciones en una dirección dada
        possibles = []
        row, col = from_row + row_increment, from_col + col_increment

        while self.is_position_valid(row, col):  # Continua mientras la posición sea válida
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
