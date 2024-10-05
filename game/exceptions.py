class ErrorChess(Exception):
    def __init__(self, message="Error en el juego de ajedrez"):
        super().__init__(message)  

class InvalidMove(ErrorChess):
    def __init__(self, message="Movimiento no valido"):
        super().__init__(message)  

class InvalidTurn(ErrorChess):
    def __init__(self, message="No es tu turno para mover esta pieza."):
        super().__init__(message)


class PieceNotFound(ErrorChess):
    def __init__(self, message="No hay pieza en la posición de origen."):
        super().__init__(message)  

class InvalidPieceMove(InvalidMove):
    def __init__(self, piece_name, message=None):
        if message is None:
            message = f"Movimiento no válido para la pieza seleccionada."
        super().__init__(message)  

class OutOfBoard(ErrorChess):
    def __init__(self, message="La posición indicada se encuentra fuera del tablero"):
        super().__init__(message)  
