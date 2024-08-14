from board import Board

class Chess:
    def __init__(self):
        self.board = Board()
        self.turn = "WHITE"

    def move(
         self,
        from_row,
        from_col,
        to_row,
        to_col,
        ): #MOVIMIENTO

        # validate coords 
        piece = self.board.get_piece(from_row, from_col)
        self.change_turn()

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__trun__ = "WHITE"

