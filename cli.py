from chess import Chess
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
                self.iniciar_partida()  # Aquí llamas a la función que inicia la partida
                break
            elif opcion == '2':
                self.mostrar_instrucciones()  # Aquí llamas a la función que muestra las instrucciones
            elif opcion == '3':
                print("\nSaliendo del juego... ¡Hasta luego!")
                break
            else:
                print("\nOpción no válida. Por favor, intenta de nuevo.")

    def iniciar_partida(self):
        print("Partida iniciada...\n")
        self.play_game()  # Inicia el juego

    def mostrar_instrucciones(self):
        print("\nInstrucciones del Juego:")
        print("1. El juego de ajedrez se juega en un tablero de 8x8.")
        print("2. Cada jugador mueve una pieza por turno.")
        print("3. El objetivo es hacer jaque mate al rey del oponente.")
        print("4. Para mover una pieza, selecciona primero la posición de origen y luego la de destino.")

    def play_game(self):
        print("Las blancas comienzan el juego.\n")
        while self.__chess__.is_playing():
            self.display_board_and_turn()
            from_input, to_input = self.get_move_input()
            result = self.attempt_move(from_input, to_input)
            if result:
                print(f'\nError: {result}')
            elif self.__chess__.end_game():
                break

    def display_board_and_turn(self):
     self.clear_terminal()
     print(f"\n  {self.__chess__.turn} TO MOVE\n")
     print(self.__chess__.show_board())

    def get_move_input(self):
        while True:
            print('\nEnter your move')
            from_input = input('From (e.g. e2): ').strip().lower()
            to_input = input('To (e.g. e4): ').strip().lower()
            try:
                self.__chess__.parse_position(from_input)  # Verificar formato de entrada
                self.__chess__.parse_position(to_input)  # Verificar formato de entrada
                return from_input, to_input
            except ValueError as e:
                print(f'\nError: {e}\nPor favor, ingresa una posición válida.')

    def attempt_move(self, from_input, to_input):
        try:
            from_row, from_col = self.__chess__.parse_position(from_input)
            to_row, to_col = self.__chess__.parse_position(to_input)
            self.__chess__.move(from_row, from_col, to_row, to_col)
            return None  # No hay error
        except Exception as e:
            return str(e)

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
