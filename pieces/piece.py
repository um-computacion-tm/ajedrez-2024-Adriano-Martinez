class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    def __str__(self):
        return ""
    
    def mov_correcto(self, x, y):
        raise NotImplementedError("Implementar")