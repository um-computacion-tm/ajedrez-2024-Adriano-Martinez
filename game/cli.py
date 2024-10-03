from game.chess import Chess
from game.exceptions import *
import os

class Cli:
    def __init__(self):
        self.__chess__ = Chess()

    def mostrar_menu(self):
        while True:
            self.clear_terminal()
            print("\nBienvenido al Juego de Ajedrez")
            print("------------------------------")
            print("1. Iniciar Partida")
            print("2. Ver Instrucciones")
            print("3. Salir")
            print("4. Guardar Partida")
            print("5. Cargar Partida")
            opcion = input("\nSelecciona una opción (1-5): ")

            if opcion == '1':
                print("\nIniciando partida...\n")
                self.iniciar_partida()
            elif opcion == '2':
                self.mostrar_instrucciones()
            elif opcion == '3':
                print("\nSaliendo del juego... ¡Hasta luego!")
                break
            elif opcion == '4':
                self.guardar_partida()
            elif opcion == '5':
                self.cargar_partida()
            else:
                print("\nOpción no válida. Por favor, intenta de nuevo.")

    def iniciar_partida(self):
        print("Partida iniciada...\n")
        print("Las blancas comienzan el juego.\n")
        self.play()  # Llama a la función que maneja la partida

    def guardar_partida(self):
        filename = input("Introduce el nombre del archivo para guardar la partida (partida.pkl): ")
        self.__chess__.save_game(filename)
        print(f"Partida guardada en {filename}.")

    def cargar_partida(self):
        filename = input("Introduce el nombre del archivo para cargar la partida (partida.pkl): ")
        self.__chess__ = Chess.load_game(filename)
        print(f"Partida cargada desde {filename}.")

    def mostrar_instrucciones(self):
        self.clear_terminal()  # Limpia la pantalla para mostrar las instrucciones
        print("\nInstrucciones del Juego:")
        print("1. El juego de ajedrez se juega en un tablero de 8x8.")
        print("2. Cada jugador mueve una pieza por turno.")
        print("3. El objetivo es hacer jaque mate al rey del oponente.")
        print("4. Para mover una pieza, selecciona primero la posición de origen y luego la de destino.")
        input("\nPresiona Enter para volver al menú...")  

    def play(self):
        while self.__chess__.is_playing():
            self.display_board_and_turn()
            print("Escribe 'draw' para solicitar un empate, 'menu' para volver al menú o realiza un movimiento.")
            
            from_input, to_input = self.get_move_input()

            if from_input == 'draw':
                self.__chess__.request_draw()
                continue
            elif from_input == 'menu':
                print("\nVolviendo al menú...")
                return  # Regresa al menú principal

            result = self.attempt_move(from_input, to_input)
            if result:
                print(f'\nError: {result}')
            elif self.__chess__.end_game():
                print("\n¡Fin del juego!")
                break

    def display_board_and_turn(self):
        self.clear_terminal()
        print("\nEs el turno de las", "blancas" if self.__chess__.turn == "WHITE" else "negras")  # Muestra el turno
        print(self.__chess__.show_board())  # Muestra el tablero

    def get_move_input(self):
        while True:
            print('\nIntroduce tu movimiento')
            from_input = input('Desde (e.g. e2 o draw o menu): ').strip().lower()
            
            if from_input == 'draw':
                return 'draw', None  # Retorna 'draw' si se solicita un empate
            elif from_input == 'menu':
                return 'menu', None  # Retorna 'menu' si se solicita volver al menú

            to_input = input('Hasta (e.g. e4): ').strip().lower()
            
            try:
                self.__chess__.parse_position(from_input)  # Verifica formato de entrada
                self.__chess__.parse_position(to_input)  # Verifica formato de entrada
                return from_input, to_input
            except InvalidMove as e:  
                print(f'\nError en la entrada: {e}\nPor favor, ingresa una posición válida.')
            except Exception as e:  # Captura errores inesperados
                print(f'\nError inesperado en la entrada: {e}\nPor favor, intenta de nuevo.')

    def attempt_move(self, from_input, to_input):
        error_message = "No se produjo ningún error."
        try:
            self.__chess__.move(from_input, to_input)
        except PieceNotFound as e:
            error_message = str(e)  # Devuelve el mensaje de error específico
        except InvalidMove as e:
            error_message = str(e) 
        except OutOfBoard as e:
            error_message = str(e)  
        except Exception as e:
            error_message = f"Ocurrió un error inesperado: {e}"  # Devuelve el mensaje de error general

        return error_message if error_message != "No se produjo ningún error." else None

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
