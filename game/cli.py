from game.chess import Chess
from game.exceptions import *
import os

class Cli:
    def __init__(self):
        self.__chess__ = Chess()

    def mostrar_menu(self):
        while True:
            self.clear_terminal()  # Limpia la pantalla antes de mostrar el menú
            print("\nBienvenido al Juego de Ajedrez")
            print("------------------------------")
            print("1. Iniciar Partida")
            print("2. Ver Instrucciones")
            print("3. Salir")
            opcion = input("\nSelecciona una opción (1, 2, 3): ")

            if opcion == '1':
                print("\nIniciando partida...\n")
                self.iniciar_partida()  # Llama a la función que inicia la partida
                break
            elif opcion == '2':
                self.mostrar_instrucciones()  # Llama a la función que muestra las instrucciones
            elif opcion == '3':
                print("\nSaliendo del juego... ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Por favor, intenta de nuevo.")

    def iniciar_partida(self):
        print("Partida iniciada...\n")
        print("Las blancas comienzan el juego.\n")  # Mensaje inicial
        self.play() 

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
        print("Escribe 'draw' para solicitar un empate o realiza un movimiento.")
        from_input, to_input = self.get_move_input()
        
        if from_input == 'draw':
            self.__chess__.request_draw()
            continue
        
        result = self.attempt_move(from_input, to_input)
        if result:
            print(f'\nError: {result}')  # Muestra el mensaje de error
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
        from_input = input('Desde (e.g. e2 o draw): ').strip().lower()  # Permite 'draw' como entrada
        if from_input == 'draw':
            return 'draw', None  # Retorna 'draw' si se solicita un empate

        to_input = input('Hasta (e.g. e4): ').strip().lower()
        
        try:
            self.__chess__.parse_position(from_input)  # Verifica formato de entrada
            self.__chess__.parse_position(to_input)  # Verifica formato de entrada
            return from_input, to_input
        except InvalidMove as e:  
            print(f'\nError: {e}\nPor favor, ingresa una posición válida.')

    def attempt_move(self, from_input, to_input):
        try:
            from_row, from_col = self.__chess__.parse_position(from_input)
            to_row, to_col = self.__chess__.parse_position(to_input)
            self.__chess__.move(from_row, from_col, to_row, to_col)
            return None
        except InvalidMove as e:
            return str(e)  
        except Exception as e:
            return f"Ocurrió un error inesperado: {e}"

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')