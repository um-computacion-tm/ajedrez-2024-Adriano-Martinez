class InvalidMove(Exception):
    def __init__(self, message="Movimiento inválido"):
        self.message = message
        super().__init__(self.message)

class PieceNotFound(InvalidMove):
    def __init__(self, message="No hay pieza en la posición de origen."):
        super().__init__(message)

class InvalidPieceMove(InvalidMove):
    def __init__(self, piece_name, message=None):
        if not message:
            message = f"Movimiento no válido para {piece_name}."
        super().__init__(message)

class InvalidMoveRookMove(InvalidPieceMove):
    def __init__(self, message=None):
        super().__init__("la torre", message)

class InvalidMoveKingMove(InvalidPieceMove):
    def __init__(self, message=None):
        super().__init__("el rey", message)

class InvalidMoveBishopMove(InvalidPieceMove):
    def __init__(self, message=None):
        super().__init__("el alfil", message)

class InvalidMoveQueenMove(InvalidPieceMove):
    def __init__(self, message=None):
        super().__init__("la Reina", message)

class InvalidMoveKnightMove(InvalidPieceMove):
    def __init__(self, message=None):
        super().__init__("el caballo", message)

class InvalidMovePawnMove(InvalidPieceMove):
    def __init__(self, message=None):
        super().__init__("el peón", message)


class OutOfBoard(InvalidMove):
    def __init__(self, message="La posición indicada se encuentra fuera del tablero"):
        super().__init__(message)