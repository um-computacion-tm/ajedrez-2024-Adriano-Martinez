from game.board import Board
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn, ErrorChess, InvalidPieceMove
import pickle

class Chess:
    def __init__(self):
        # Inicializa el tablero, el turno de juego, el historial de movimientos y el estado del juego
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__history__ = []  # lista de movimientos 
        self.__game_over__ = False
    
    # Verifica si el juego está activo o ha terminado
    def is_playing(self):
        return not self.__game_over__
    
    # Convierte una posición en notación ajedrecística (e.g., 'e2') a coordenadas en el tablero
    def parse_position(self, pos):
        if len(pos) != 2 or pos[0] not in 'abcdefgh' or pos[1] not in '12345678':
            raise ValueError("Posición inválida. Usa el formato 'e2'.")
        col = ord(pos[0]) - ord('a') # Convierte la letra a una columna (0-7)
        row = 8 - int(pos[1]) # Convierte el número a una fila (0-7)
        return row, col

    # Mueve una pieza de una posición a otra
    def move(self, from_input, to_input):
        try:
            # Convierte las entradas de posiciones en coordenadas
            from_row, from_col = self.parse_position(from_input)
            to_row, to_col = self.parse_position(to_input)

            # Valida que las coordenadas estén dentro del tablero
            self.validate_coords(from_row, from_col, to_row, to_col)

            # Obtiene la pieza de la posición inicial
            piece = self.__board__.get_piece(from_row, from_col)

            # Si no hay una pieza en la posición inicial, lanza un error
            if piece is None:
                raise PieceNotFound()

            self.validate_turn(piece)

            is_valid, message = self.__board__.is_valid_move(from_row, from_col, to_row, to_col, piece)

            if not is_valid:
                raise InvalidMove(message)

            self.__board__.mover_pieza(from_row, from_col, to_row, to_col)
            self.__history__.append((from_input, to_input))
            self.change_turn()

            # Mostrar conteo de piezas después de cada movimiento
            self.show_piece_count()

        except (PieceNotFound, InvalidMove, InvalidTurn, ValueError) as e:
            print(f"Error: {str(e)}")  

    # Obtiene turno actual
    def get_turn(self):
        return self.__turn__
    
    # Cambia el turno
    def change_turn(self):
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
    
    # Valida que la pieza sea del color correspondiente al turno actual
    def validate_turn(self, piece):
        if piece.get_color() != self.__turn__:
            raise InvalidTurn("No es tu turno para mover esta pieza.")

    def validate_coords(self, from_row, from_col, to_row, to_col):
        if not (0 <= from_row < 8 and 0 <= from_col < 8 and 0 <= to_row < 8 and 0 <= to_col < 8):
            raise ValueError("Coordenadas fuera del rango. Deben estar entre 0 y 7.")
        
    # Muestra el tablero actual
    def show_board(self):
        return str(self.__board__)

    @property
    def turn(self):
        return self.__turn__

    # Muestra el conteo de piezas blancas y negras
    def show_piece_count(self):
        white_count, black_count = self.__board__.count_pieces()
        print(f"Piezas blancas: {white_count}, Piezas negras: {black_count}")

    def end_game(self):
     white_count, black_count = self.__board__.count_pieces()

    # Si no quedan piezas blancas, el jugador negro gana
     if white_count == 0:
        print("¡Las negras han ganado! Las blancas no tienen piezas.")
        self.__game_over__ = True
        return True
    # Si no quedan piezas negras, el jugador blanco gana
     elif black_count == 0:
        print("¡Las blancas han ganado! Las negras no tienen piezas.")
        self.__game_over__ = True
        return True

     return False
    
    # Solicita a ambos jugadores si están de acuerdo en un empate
    def request_draw(self):
        decision_white = input("¿Blancas quieren terminar la partida en empate? (s/n): ").lower()
        decision_black = input("¿Negras quieren terminar la partida en empate? (s/n): ").lower()

        if decision_white == 's' and decision_black == 's':
            print("La partida ha terminado en empate por mutuo acuerdo.")
            self.__game_over__ = True

    # Guarda el estado actual del juego en un archivo usando pickle
    def save_game(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def load_game(cls, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
