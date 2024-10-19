from game.chess import Chess
from game.exceptions import *
import os

class Cli:
    def __init__(self):
        self.__chess__ = None # Inicializa el objeto Cli sin una partida de ajedrez activa

    def mostrar_menu(self):
     """Muestra el menú principal del juego de ajedrez y procesa la selección del jugador."""
     try:
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
     except EOFError:
        print("Error: No se recibió entrada. Finalizando.")
     except KeyboardInterrupt:
        print("\nInterrupción detectada, saliendo del menú.")

    def mostrar_opciones_menu(self):
        """Muestra las opciones del menú principal del juego de ajedrez."""
        print("\nBienvenido al Juego de Ajedrez")
        print("------------------------------")
        print("1. Iniciar Partida")
        print("2. Ver Instrucciones")
        print("3. Salir")
        print("4. Guardar Partida")
        print("5. Cargar Partida")

    def iniciar_partida(self):
        """Inicia una nueva partida o continúa una partida activa."""
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
        """Solicita confirmación del usuario para realizar una acción.
        Devuelve True si la respuesta es 's', False si es 'n'.
        """
        while True:
            respuesta = input(mensaje).strip().lower()
            if respuesta in ['s', 'n']:
                return respuesta == 's'
            print("Entrada no válida. Por favor, ingresa 's' o 'n'.")

    def request_draw(self):
     """Solicita un empate a ambos jugadores. Devuelve True si ambos aceptan el empate."""
    # Pregunta a las blancas si aceptan el empate
     white_accepts_input = input("¿Blancas quieren terminar la partida en empate? (s/n): ").lower().strip()

    # Pregunta a las negras si aceptan el empate
     black_accepts_input = input("¿Negras quieren terminar la partida en empate? (s/n): ").lower().strip()

    # Convertimos 's' en True y 'n' en False
     white_accepts = white_accepts_input == 's'
     black_accepts = black_accepts_input == 's'

    # Llamamos al método offer_draw con valores booleanos
     draw= self.__chess__.offer_draw(white_accepts, black_accepts)
     if draw:
        print("\n¡El juego ha terminado en empate!")  # Mensaje cuando ambos aceptan
     else:
        print("\nEl empate ha sido rechazado. La partida continúa.")  # Mensaje cuando se rechaza
     return draw
    
    def guardar_partida(self):
        """Guarda la partida activa en Redis con un identificador proporcionado por el usuario."""
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
     """Carga una partida guardada desde Redis utilizando un identificador."""
     game_id = self.solicitar_id_partida("Introduce el ID de la partida que deseas cargar: ")
     if game_id:
        try:
            # No inicializar un nuevo Chess si ya existe uno
            if self.__chess__ is None:
                self.__chess__ = Chess()
            self.__chess__.load_game(game_id)
            if self.__chess__.is_playing():
                print(f"Partida cargada desde {game_id}.")
                self.play()  
            else:
                print(f"No se pudo cargar la partida con ID {game_id}.")
        except Exception as e:
            print(f"Error al cargar la partida: {e}")


    def solicitar_id_partida(self, mensaje):
        """Solicita al usuario un identificador de partida y valida que no esté vacío."""
        game_id = input(mensaje).strip()
        if not game_id:
            print("El ID de la partida no puede estar vacío.")
            return None
        return game_id
    
    def mostrar_instrucciones(self):
        """Muestra las instrucciones básicas del juego de ajedrez."""
        self.clear_terminal()
        print("\nInstrucciones del Juego:")
        print("1. El juego de ajedrez se juega en un tablero de 8x8.")
        print("2. Cada jugador mueve una pieza por turno.")
        print("3. El objetivo es capturar todas las piezas del oponente para ganar.")
        print("4. Para mover una pieza, selecciona primero la posición de origen y luego la de destino esto en forma algebraica(a2 a a4).")
        input("\nPresiona Enter para volver al menú...")
    
    def aplicar_accion(self, opcion):
        """Ejecuta la acción seleccionada en el menú de partida activa. 
        Devuelve un mensaje de error, si hay, y si debe salir o volver al menú.
        """
        should_break = False
        should_return = False
        error_message = None
        if opcion == '1':
            error_message = self.handle_move()  # Maneja el movimiento de la pieza
        elif opcion == '2':
            if self.request_draw():  # Solicita un empate
             should_break = True
        elif opcion == '3':
            if self.confirmar_accion("¿Estás seguro de que quieres rendirte? (s/n): "):
                self.__chess__.surrender()  # Rinde al jugador
                print("\n¡Te has rendido! Fin de la partida.")
                should_break = True
        elif opcion == '4':
            if self.confirmar_accion("¿Estás seguro de que quieres volver al menú principal? (s/n): "):
                should_return = True
        return error_message, should_return, should_break

    def play(self):
     """Ejecuta el bucle principal de la partida, permitiendo al jugador mover piezas, solicitar empate, rendirse o volver al menú."""
     error_message = None
     while self.__chess__.is_playing():
        self.display_board_and_turn()  # Muestra el tablero y el turno

        if error_message:
            print(f'\nError: {error_message}')  # Muestra mensaje de error si existe
            error_message = None  # Reinicia mensaje de error

        opcion = self.menu_partida_activa()  # Obtiene la opción del menú
        error_message, should_return, should_break = self.aplicar_accion(opcion)
        if should_break:
            break
        if should_return:
            return
        
     self.__chess__ = None  # Reinicia el objeto Chess
     print("\nVolviendo al menú principal...")  # Mensaje de retorno al menú
     input("\nPresiona Enter para volver al menu principal...")

    def handle_move(self):
     """Obtiene y procesa las entradas para mover una pieza. Devuelve un mensaje de error si el movimiento no es válido."""
     from_input, to_input = self.get_move_input()  # Obtiene las entradas del movimiento

     if from_input == 'back':
        return None  # Vuelve al menú de opciones sin errores

     return self.attempt_move(from_input, to_input)  # Intenta mover la pieza

    def menu_partida_activa(self):
     """Muestra las opciones disponibles durante una partida activa."""
     print("\nOpciones de la partida:")
     print("1. Mover una pieza")
     print("2. Solicitar empate")
     print("3. Rendirse")
     print("4. Volver al menú principal")
    
     while True:
        opcion = input("\nSelecciona una opción (1-4): ").strip()
        if opcion in ['1', '2', '3', '4']:
            return opcion
        else:
            print("\nOpción no válida. Intenta de nuevo.")

    def display_board_and_turn(self):
        """Muestra el tablero de ajedrez y el turno actual."""
        self.clear_terminal()
        print("\nEs el turno de las", "blancas" if self.__chess__.turn == "WHITE" else "negras")
        print(self.__chess__.show_board())

    def get_move_input(self):
     """Solicita al jugador las posiciones de origen y destino de una pieza. Devuelve las posiciones ingresadas."""
     while True:
        from_input = input('Desde (e.g. e2, escribe "back" para cancelar accion): ').strip().lower()
        if from_input in ['back']:
            return from_input, None
        to_input = input('Hasta (e.g. e4 o back para regresar): ').strip().lower()
        if to_input == 'back':
            return 'back', None  # Vuelve al menú de opciones
        try:
            self.__chess__.parse_position(from_input)
            self.__chess__.parse_position(to_input)
            return from_input, to_input
        except InvalidMove as e:
            print(f'\nError en la entrada: {e}\nPor favor, ingresa una posición válida.')
        except Exception as e:
            print(f'\nError inesperado en la entrada: {e}\nPor favor, intenta de nuevo.')

    def attempt_move(self, from_input, to_input):
        """Intenta mover una pieza de la posición de origen a la de destino. 
    Devuelve un mensaje de error si el movimiento es inválido.
    """
        try:
            self.__chess__.move(from_input, to_input)
        except (PieceNotFound, InvalidTurn, InvalidPieceMove, InvalidMove, OutOfBoard, InvalidFormat) as e:
            return str(e)
        except Exception as e:
            return f"Ocurrió un error inesperado: {e}"
        return None
    
    def salir_juego(self):
     """Muestra un mensaje de despedida y termina la ejecución del juego."""
     print("Saliendo del juego...")

    def clear_terminal(self):
     """Limpia la pantalla de la terminal."""
     try:
        os.system('cls' if os.name == 'nt' else 'clear')
     except Exception as e:
        print(f"Error al limpiar la terminal: {e}")