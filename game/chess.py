from game.board import Board
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn, ErrorChess , InvalidPieceMove
import pickle

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__history__ = []  # lista de movimientos 
        self.__game_over__ = False
    
    
    def get_turn(self):
        return self.__turn__

    def is_playing(self):
        return not self.__game_over__

    def parse_position(self, pos):
        if len(pos) != 2 or pos[0] not in 'abcdefgh' or pos[1] not in '12345678':
            raise ValueError("Posición inválida. Usa el formato 'e2'.")
        col = ord(pos[0]) - ord('a')
        row = 8 - int(pos[1])
        return row, col

    def move(self, from_input, to_input):
     try:
        from_row, from_col = self.parse_position(from_input)
        to_row, to_col = self.parse_position(to_input)

        self.validate_coords(from_row, from_col, to_row, to_col)

        piece = self.__board__.get_piece(from_row, from_col)

        if piece is None:
            raise PieceNotFound()

        self.validate_turn(piece)

        is_valid, message = self.__board__.is_valid_move(from_row, from_col, to_row, to_col, piece)

        if not is_valid:
            raise InvalidMove(message)

        self.__board__.mover_pieza(from_row, from_col, to_row, to_col)
        self.__history__.append((from_input, to_input))
        self.change_turn()

     except (PieceNotFound, InvalidMove, InvalidTurn, ValueError) as e:
        print(f"Error: {str(e)}")  

    def validate_turn(self, piece):
     if piece.get_color() != self.__turn__:
        raise InvalidTurn("No es tu turno para mover esta pieza.")

    def validate_coords(self, from_row, from_col, to_row, to_col):
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Coordenadas fuera del rango. Deben estar entre 0 y 7.")

    def show_board(self):
        return str(self.__board__)

    @property
    def turn(self):
        return self.__turn__

    def change_turn(self):
     self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"

    def end_game(self):
        white_pieces = self.__board__.get_all_pieces("WHITE")
        black_pieces = self.__board__.get_all_pieces("BLACK")

        if not white_pieces:
            print("¡Las negras han ganado! Las blancas no tienen piezas.")
            self.__game_over__ = True
            return True
        elif not black_pieces:
            print("¡Las blancas han ganado! Las negras no tienen piezas.")
            self.__game_over__ = True
            return True

        return False

    def request_draw(self):
        decision_white = input("¿Blancas quieren terminar la partida en empate? (s/n): ").lower()
        decision_black = input("¿Negras quieren terminar la partida en empate? (s/n): ").lower()

        if decision_white == 's' and decision_black == 's':
            print("La partida ha terminado en empate por mutuo acuerdo.")
            self.__game_over__ = True

    def save_game(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_game(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
