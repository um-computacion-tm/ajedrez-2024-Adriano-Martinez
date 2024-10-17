class ErrorChess(Exception):
    """Clase base para las excepciones de ajedrez."""
    def __init__(self, message="Error en el juego de ajedrez"):
        super().__init__(message)  

class InvalidMove(ErrorChess):
    def __init__(self, message="Movimiento no valido"):
        super().__init__(message)  

class InvalidTurn(ErrorChess):
    """Excepción cuando se intenta mover una pieza que no es el turno actual."""
    def __init__(self, message="No es tu turno para mover esta pieza."):
        super().__init__(message)

class InvalidFormat(ErrorChess):
    """Excepción cuando se ingresa una entrada no válida."""
    def __init__(self, message="Formato de entrada inválido o fuera del tablero, Usa el formato 'e2'."):
        super().__init__(message)

class PieceNotFound(ErrorChess):
    """Excepción cuando no se encuentra una pieza en una posición."""
    def __init__(self, message="No hay pieza en la posición de origen."):
        super().__init__(message)  

class InvalidPieceMove(InvalidMove):
    """Excepción cuando un movimiento no es válido para cierta pieza."""
    def __init__(self, piece_name, message=None):
        if message is None:
            message = f"Movimiento no válido para {piece_name}."
        super().__init__(message)
        
class OutOfBoard(ErrorChess):
    """Excepción cuando se intenta acceder a una posición fuera del tablero."""
    def __init__(self, message="La posición indicada se encuentra fuera del tablero"):
        super().__init__(message)  
