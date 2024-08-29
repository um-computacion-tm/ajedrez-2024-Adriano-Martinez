
class InvalidMove(Exception):
    pass

class InvalidMoveNoPiece(InvalidMove):
    def __init__(self, message="No hay pieza en la posición de origen."):
        self.message = message
        super().__init__(self.message)


class InvalidMoveRookMove(InvalidMove):
     def __init__(self, message="Movimiento no válido para la torre."):
        self.message = message
        super().__init__(self.message)
