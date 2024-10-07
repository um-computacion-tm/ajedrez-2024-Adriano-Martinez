from game.chess import Chess
from game.exceptions import *
import os

class Cli:
    def __init__(self):
        self.__chess__ = None

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
     if self.__chess__ is None:  # Crea un nuevo objeto solo si no hay una partida activa
        self.__chess__ = Chess()
        print("Partida iniciada...\n")
        print("Las blancas comienzan el juego.\n")
        self.play()
     else:
        continuar = input("Ya hay una partida activa. ¿Quieres continuar con la partida actual? (s/n): ").strip().lower()
        if continuar == 's':
            self.play()
        else:
            # Reiniciar la partida
            self.__chess__ = Chess()  # Reinicia la partida
            print("Se ha iniciado una nueva partida...\n")
            print("Las blancas comienzan el juego.\n")
            self.play()


    def guardar_partida(self):
     if self.__chess__ is None:
            print("No hay ninguna partida activa para guardar.")
            return
     game_id = input("Introduce un identificador para guardar la partida: ").strip()
     if not game_id:
        print("El ID de la partida no puede estar vacío.")
        return
     try:
        self.__chess__.save_game(game_id)
        print(f"Partida guardada con ID {game_id}.")
     except Exception as e:
        print(f"Error al guardar la partida: {e}")

    def cargar_partida(self):
     game_id = input("Introduce el ID de la partida que deseas cargar: ").strip()
     if not game_id:
        print("El ID de la partida no puede estar vacío.")
        return
     try:
        self.__chess__ = Chess()  # Asegurarse de que se crea una nueva instancia
        self.__chess__.load_game(game_id)
        if self.__chess__.is_playing():  # Verifica si la partida se cargó correctamente
            print(f"Partida cargada desde {game_id}.")
            print("Estado actual del juego:")
            print(self.__chess__.show_board())
            self.play()  # Comenzar el juego inmediatamente
        else:
            print(f"No se pudo cargar la partida con ID {game_id}.")
     except Exception as e:
        print(f"Error al cargar la partida: {e}")

    def mostrar_instrucciones(self):
        self.clear_terminal()  # Limpia la pantalla para mostrar las instrucciones
        print("\nInstrucciones del Juego:")
        print("1. El juego de ajedrez se juega en un tablero de 8x8.")
        print("2. Cada jugador mueve una pieza por turno.")
        print("3. El objetivo es hacer jaque mate al rey del oponente.")
        print("4. Para mover una pieza, selecciona primero la posición de origen y luego la de destino.")
        input("\nPresiona Enter para volver al menú...")  

    def play(self):
     error_message = None  # Variable para almacenar el mensaje de error temporalmente

     while self.__chess__.is_playing():  # Mientras el juego no haya terminado
        self.display_board_and_turn()

        # Mostrar cualquier mensaje de error que se haya producido
        if error_message:
            print(f'\nError: {error_message}')
            error_message = None  # Restablecer el mensaje de error

        print("Escribe 'draw' para solicitar un empate, 'rendirse' para rendirte, 'menu' para volver al menú o realiza un movimiento.")
        from_input, to_input = self.get_move_input()

        if from_input == 'draw':
            self.__chess__.request_draw()
            print("\n¡Empate solicitado! Fin de la partida.")
            break
        elif from_input == 'rendirse':
            self.__chess__.rendirse()  # Llamar al método rendirse
            print("\n¡Te has rendido! Fin de la partida.")
            break  # Terminar el bucle ya que el juego ha finalizado
        elif from_input == 'menu':
            print("\nVolviendo al menú...")
            return  # Salir del juego y volver al menú

        result = self.attempt_move(from_input, to_input)
        if result:
            error_message = result
        elif self.__chess__.end_game():  # Verificar si el juego ha terminado después de cada movimiento
            print("\n¡Fin del juego!")
            break

    # Reiniciar el objeto Chess para permitir una nueva partida
     self.__chess__ = None  # Resetea para que no haya partida activa

    # Mensaje de finalización y espera por 'menu'
     self.wait_for_menu()

    def wait_for_menu(self):
        while True:
            option = input("\nEscribe 'menu' para volver al inicio: ").strip().lower()
            if option == 'menu':
                print("\nVolviendo al menú principal...")
                return

    def display_board_and_turn(self):
        self.clear_terminal()
        print("\nEs el turno de las", "blancas" if self.__chess__.turn == "WHITE" else "negras")  # Muestra el turno
        print(self.__chess__.show_board())  # Muestra el tablero

    def get_move_input(self):
     while True:
        print('\nIntroduce tu movimiento')
        from_input = input('Desde (e.g. e2, draw, rendirse o menu): ').strip().lower()
        
        if from_input == 'draw':
            return 'draw', None  # Retorna 'draw' si se solicita un empate
        elif from_input == 'menu':
            return 'menu', None  # Retorna 'menu' si se solicita volver al menú
        elif from_input == 'rendirse':
            return 'rendirse', None  # Retorna 'rendirse' si se solicita rendirse

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
        except InvalidTurn as e:
            error_message = str(e) 
        except InvalidPieceMove as e:
            error_message = str(e)
        except InvalidMove as e:
            error_message = str(e) 
        except OutOfBoard as e:
            error_message = str(e)  
        except InvalidFormat as e:
            error_message = str(e)
        except Exception as e:
            error_message = f"Ocurrió un error inesperado: {e}"  # Devuelve el mensaje de error general

        return error_message if error_message != "No se produjo ningún error." else None

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')
