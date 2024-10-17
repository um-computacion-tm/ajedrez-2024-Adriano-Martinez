import os
import redis
import pickle
from game.board import Board
from game.exceptions import PieceNotFound, InvalidMove, InvalidTurn, ErrorChess, InvalidPieceMove, InvalidFormat

class Chess:
    def __init__(self):
        """
        Inicializa el tablero, el turno de juego, el historial de movimientos y el estado del juego.
        También configura la conexión a Redis para almacenar los datos del juego.
        """
        self.__board__ = Board()
        self.__turn__ = "WHITE"
        self.__history__ = []  # lista de movimientos 
        self.__game_over__ = False
        redis_host = os.getenv('REDIS_HOST', 'localhost')  # Obtiene el host de Redis desde la variable de entorno
        self.__redis__ = redis.StrictRedis(host=redis_host, port=6379, db=0)
        
    def surrender(self):
        """
        Permite a un jugador rendirse, declarando ganador al oponente.
        """
        if self.__turn__ == "WHITE":
            print("Las blancas se han rendido. Las negras ganan la partida.")
        else:
            print("Las negras se han rendido. Las blancas ganan la partida.")
        self.__game_over__ = True  # Marcar que el juego ha terminado
    
    def offer_draw(self, white_accepts: bool, black_accepts: bool):
        """
        Permite ofrecer un empate si ambos jugadores están de acuerdo.
        """
        if white_accepts and black_accepts:
            print("La partida ha terminado en empate por mutuo acuerdo.")
            self.__game_over__ = True
            return True
        else:
            print("El empate ha sido rechazado. La partida continúa.")
            return False
    
    def is_playing(self):
        """
        Verifica si el juego está en curso o ha terminado.
        """
        return not self.__game_over__
    
    def parse_position(self, pos):
        """
        Convierte una posición en notación ajedrecística (e.g., 'e2') a coordenadas en el tablero.
        Lanza una excepción si el formato de la posición es inválido.
        """
        if len(pos) != 2 or pos[0] not in 'abcdefgh' or pos[1] not in '12345678':
            raise InvalidFormat()
        col = ord(pos[0]) - ord('a')  # Convierte la letra a una columna (0-7)
        row = 8 - int(pos[1])  # Convierte el número a una fila (0-7)
        return row, col

    def move(self, from_input, to_input):
        """
        Realiza un movimiento en el tablero desde una posición inicial a una posición final,
        validando que el movimiento sea legal y que sea el turno correcto.
        """
        try:
            from_row, from_col = self.parse_position(from_input)
            to_row, to_col = self.parse_position(to_input)

            piece = self.__board__.get_piece(from_row, from_col)

            if piece is None:
                raise PieceNotFound()

            self.validate_turn(piece)

            self.__board__.mover_pieza(from_row, from_col, to_row, to_col)
        
            self.__history__.append((from_input, to_input))
            self.change_turn()

            self.show_piece_count()

            if self.end_game():
                return  # Si el juego ha terminado, no sigue el siguiente turno

        except (PieceNotFound, InvalidMove, InvalidTurn, ValueError, InvalidPieceMove) as e:
            raise

    def get_turn(self):
        """
        Obtiene el turno actual del juego.
        """
        return self.__turn__
    
    def change_turn(self):
        """
        Cambia el turno del jugador actual (de blancas a negras o viceversa).
        """
        self.__turn__ = "BLACK" if self.__turn__ == "WHITE" else "WHITE"
    
    def validate_turn(self, piece):
        """
        Valida que la pieza seleccionada sea del color correspondiente al turno actual.
        Lanza una excepción si el turno no es correcto.
        """
        if piece.get_color() != self.__turn__:
            raise InvalidTurn("No es tu turno para mover esta pieza.")
        
    def show_board(self):
        """
        Devuelve una representación en cadena del tablero de ajedrez actual.
        """
        return str(self.__board__)

    @property
    def turn(self):
        """
        Devuelve el turno actual.
        """
        return self.__turn__

    def show_piece_count(self):
        """
        Muestra el número de piezas blancas y negras que quedan en el tablero.
        """
        white_count, black_count = self.__board__.count_pieces()
        print(f"Piezas blancas: {white_count}, Piezas negras: {black_count}")

    def end_game(self):
        """
        Verifica si el juego ha terminado al no quedar piezas de un color.
        """
        white_count, black_count = self.__board__.count_pieces()

        if white_count == 0:
            print("¡Las negras han ganado! Las blancas no tienen piezas.")
            self.__game_over__ = True
            return True
        elif black_count == 0:
            print("¡Las blancas han ganado! Las negras no tienen piezas.")
            self.__game_over__ = True
            return True
        return False
    
    def create_piece(self, color, piece_type):
        """
        Crea una nueva pieza del tipo especificado y del color dado.
        Lanza un error si el tipo de pieza no es válido.
        """
        piece_class = Board.get_piece_class(piece_type)
        if piece_class:
            return piece_class(color, self.__board__)
        raise ValueError(f"Tipo de pieza desconocido: {piece_type}")

    def save_game(self, game_id):
        """
        Guarda el estado actual del juego en Redis utilizando el ID de juego dado.
        """
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
            raise  

    def load_game(self, game_id):
        """
        Carga un juego guardado desde Redis utilizando el ID de juego dado.
        """
        game_data = self.__redis__.get(game_id)
        if game_data:
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
