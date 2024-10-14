from game.chess import Chess
from game.exceptions import *
import os

class Cli:
    def __init__(self):
        self.__chess__ = None

    def mostrar_menu(self):
        while True:
            self.clear_terminal()
            self.mostrar_opciones_menu()
            opcion = input("\nSelecciona una opción (1-5): ")
            if opcion == '1':
                self.iniciar_partida()
            elif opcion == '2':
                self.mostrar_instrucciones()
            elif opcion == '3':
                self.salir_juego()
                break
            elif opcion == '4':
                self.guardar_partida()
            elif opcion == '5':
                self.cargar_partida()
            else:
                print("\nOpción no válida. Por favor, intenta de nuevo.")

    def mostrar_opciones_menu(self):
        print("\nBienvenido al Juego de Ajedrez")
        print("------------------------------")
        print("1. Iniciar Partida")
        print("2. Ver Instrucciones")
        print("3. Salir")
        print("4. Guardar Partida")
        print("5. Cargar Partida")

    def iniciar_partida(self):
        if self.__chess__ is None:
            self.__chess__ = Chess()
            print("Partida iniciada...\n")
            print("Las blancas comienzan el juego.\n")
            self.play()
        else:
            if self.confirmar_accion("Ya hay una partida activa. ¿Quieres continuar con la partida actual? (s/n): "):
                self.play()
            else:
                self.__chess__ = Chess()  # Reinicia la partida
                print("Se ha iniciado una nueva partida...\n")
                print("Las blancas comienzan el juego.\n")
                self.play()

    def confirmar_accion(self, mensaje):
        while True:
            respuesta = input(mensaje).strip().lower()
            if respuesta in ['s', 'n']:
                return respuesta == 's'
            print("Entrada no válida. Por favor, ingresa 's' o 'n'.")

    def request_draw(self):
        # Pregunta a las blancas si aceptan el empate
        white_accepts_input = input("¿Blancas quieren terminar la partida en empate? (s/n): ").lower().strip()

        # Pregunta a las negras si aceptan el empate
        black_accepts_input = input("¿Negras quieren terminar la partida en empate? (s/n): ").lower().strip()

        # Convertimos 's' en True y 'n' en False
        white_accepts = white_accepts_input == 's'
        black_accepts = black_accepts_input == 's'

        # Llamamos al método offer_draw con valores booleanos
        if self.__chess__.offer_draw(white_accepts, black_accepts):
            return  # Terminar el juego si hay empate
        else:
            print("\nEl empate ha sido rechazado. La partida continúa.")

    def guardar_partida(self):
        if self.__chess__ is None:
            print("No hay ninguna partida activa para guardar.")
            return
        game_id = self.solicitar_id_partida("Introduce un identificador para guardar la partida: ")
        if game_id:
            try:
                self.__chess__.save_game(game_id)
                print(f"Partida guardada con ID {game_id}.")
            except Exception as e:
                print(f"Error al guardar la partida: {e}")

    def cargar_partida(self):
        game_id = self.solicitar_id_partida("Introduce el ID de la partida que deseas cargar: ")
        if game_id:
            try:
                self.__chess__ = Chess()
                self.__chess__.load_game(game_id)
                if self.__chess__.is_playing():
                    print(f"Partida cargada desde {game_id}.")
                    print("Estado actual del juego:")
                    print(self.__chess__.show_board())
                    self.play()
                else:
                    print(f"No se pudo cargar la partida con ID {game_id}.")
            except Exception as e:
                print(f"Error al cargar la partida: {e}")

    def solicitar_id_partida(self, mensaje):
        game_id = input(mensaje).strip()
        if not game_id:
            print("El ID de la partida no puede estar vacío.")
            return None
        return game_id
    
    def mostrar_instrucciones(self):
        self.clear_terminal()
        print("\nInstrucciones del Juego:")
        print("1. El juego de ajedrez se juega en un tablero de 8x8.")
        print("2. Cada jugador mueve una pieza por turno.")
        print("3. El objetivo es hacer jaque mate al rey del oponente.")
        print("4. Para mover una pieza, selecciona primero la posición de origen y luego la de destino.")
        input("\nPresiona Enter para volver al menú...")

    def play(self):
        error_message = None
        while self.__chess__.is_playing():
            self.display_board_and_turn()

            if error_message:
                print(f'\nError: {error_message}')
                error_message = None

            print("Escribe 'draw' para solicitar un empate, 'rendirse' para rendirte, 'menu' para volver al menú o realiza un movimiento.")
            from_input, to_input = self.get_move_input()

            if from_input == 'draw':
                self.request_draw()
                if not self.__chess__.is_playing():
                    break  # Termina el juego si hay empate
                continue  # Si no hay empate, continúa con el siguiente turno (no pide movimiento)
            
            elif from_input == 'rendirse':
                self.__chess__.rendirse()
                print("\n¡Te has rendido! Fin de la partida.")
                break

            elif from_input == 'menu':
                print("\nVolviendo al menú...")
                return

            result = self.attempt_move(from_input, to_input)
            if result:
                error_message = result
            elif self.__chess__.end_game():
                print("\n¡Fin del juego!")
                break
        
        self.__chess__ = None
        self.wait_for_menu()

    def wait_for_menu(self):
        while input("\nEscribe 'menu' para volver al inicio: ").strip().lower() != 'menu':
            pass
        print("\nVolviendo al menú principal...")


    def display_board_and_turn(self):
        self.clear_terminal()
        print("\nEs el turno de las", "blancas" if self.__chess__.turn == "WHITE" else "negras")
        print(self.__chess__.show_board())

    def get_move_input(self):
        while True:
            from_input = input('Desde (e.g. e2, draw, rendirse o menu): ').strip().lower()
            if from_input in ['draw', 'menu', 'rendirse']:
                return from_input, None
            to_input = input('Hasta (e.g. e4): ').strip().lower()
            try:
                self.__chess__.parse_position(from_input)
                self.__chess__.parse_position(to_input)
                return from_input, to_input
            except InvalidMove as e:
                print(f'\nError en la entrada: {e}\nPor favor, ingresa una posición válida.')
            except Exception as e:
                print(f'\nError inesperado en la entrada: {e}\nPor favor, intenta de nuevo.')

    def attempt_move(self, from_input, to_input):
        try:
            self.__chess__.move(from_input, to_input)
        except (PieceNotFound, InvalidTurn, InvalidPieceMove, InvalidMove, OutOfBoard, InvalidFormat) as e:
            return str(e)
        except Exception as e:
            return f"Ocurrió un error inesperado: {e}"
        return None
    
    def salir_juego(self):
     print("Saliendo del juego...")

    def clear_terminal(self):
     os.system('cls' if os.name == 'nt' else 'clear')