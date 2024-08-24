class Piece:
    def __init__(self, color):
        self.__color__ = color

    def get_color(self):
        return self.__color__

    def __str__(self):
        return ""
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        raise NotImplementedError("Implementar")