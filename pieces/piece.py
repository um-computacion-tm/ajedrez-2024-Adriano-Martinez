class Piece:
    def __init__(self, color):
        self.__color__ = color
    
    def __str__(self):
        return self.get_symbol()

    def get_symbol(self):
        raise NotImplementedError("implementar metodo en subclases")