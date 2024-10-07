import os
import redis
import pickle
from game.board import Board
from game.exceptions import OutOfBoard, PieceNotFound, InvalidMove, InvalidTurn, ErrorChess, InvalidPieceMove, InvalidFormat


class Chess:
    def __init__(self):
        # Inicializa el tablero, el turno de juego, el historial de movimientos y el estado del juego
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__history__ = []  # lista de movimientos 
        self.__game_over__ = False
        redis_host = os.getenv('REDIS_HOST', 'localhost')  # Obtiene el host de Redis desde la variable de entorno
        self.__redis__ = redis.StrictRedis(host=redis_host, port=6379, db=0)
        

    #Permite al jugador rendirse
    def rendirse(self):
        if self.__turn__ == "WHITE":
            print("Las blancas se han rendido. Las negras ganan la partida.")
        else:
            print("Las negras se han rendido. Las blancas ganan la partida.")
        self.__game_over__ = True  # Marcar que el juego ha terminado
    
    # Verifica si el juego está activo o ha terminado
    def is_playing(self):
        return not self.__game_over__
    
    # Convierte una posición en notación ajedrecística (e.g., 'e2') a coordenadas en el tablero
    def parse_position(self, pos):
        if len(pos) != 2 or pos[0] not in 'abcdefgh' or pos[1] not in '12345678':
            raise InvalidFormat()
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

        except (PieceNotFound, InvalidMove, InvalidTurn, ValueError, InvalidPieceMove) as e:
            raise 

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
            raise OutOfBoard("Coordenadas fuera del rango. Deben estar entre 0 y 7.")
        
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

    def create_piece(self, color, piece_type):
     piece_class = Board.get_piece_class(piece_type)
     if piece_class:
        return piece_class(color, self.__board__)
     raise ValueError(f"Tipo de pieza desconocido: {piece_type}")

    def save_game(self, game_id):
     try:
        game_data = {
            'turn': self.__turn__,
            'history': self.__history__,
            'board': [[(piece.get_color(), piece.__class__.__name__) if piece else None for piece in row] for row in self.__board__.__positions__]
        }
        print(f"Guardando datos de la partida: {game_data}")
        self.__redis__.set(game_id, pickle.dumps(game_data))
     except Exception as e:
        print(f"Error al guardar la partida: {e}")

    def load_game(self, game_id):
     game_data = self.__redis__.get(game_id)
     if game_data:
        try:
            game_data = pickle.loads(game_data)
            self.__turn__ = game_data['turn']
            self.__history__ = game_data['history']
            
            # Reconstruye el tablero a partir de la información guardada
            for row in range(8):
                for col in range(8):
                    piece_data = game_data['board'][row][col]
                    if piece_data:
                        color, piece_type = piece_data
                        piece_type = piece_type.lower()  # Convertir a minúsculas
                        self.__board__.__positions__[row][col] = self.create_piece(color, piece_type)
                    else:
                        self.__board__.__positions__[row][col] = None
        except Exception as e:
            print(f"Error al deserializar los datos: {e}")
     else:
        print(f"No se encontró la partida con ID: {game_id}")
