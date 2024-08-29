class Piece:
    def __init__(self, color, board):
        self.__color__ = color
        self.__board__ = board
        
    def get_color(self):
        return self.__color__

    def __str__(self):
        return ""
    
    def mov_correcto(self, from_x, from_y, to_x, to_y):
        raise NotImplementedError("Implementar")