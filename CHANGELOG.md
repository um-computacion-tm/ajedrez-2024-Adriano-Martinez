# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

##  [0.4.7] - 2024-10-16
### Agregando
- **game/cli.py**:
  - Añadiendo método `aplicar_accion` para aplicar acciones en el menú principal.
- **test_chess.py**:
  - Se han añadido pruebas para completar cobertura de codigo.
### Cambios
- **game/cli.py**:
  - Solucionando problemas de duplicación en `play`.
  - Refactorizando código.
- **test_cli.py**:
  - Solucionando pruebas.


##  [0.4.6] - 2024-10-15
### Cambios
- **test_cli.py**:
  - Solucionando prueba.
- **CHANGELOG.md**:
  - Mejorando **changelog.md**

##  [0.4.5] - 2024-10-14
### Agregando
- **game/cli.py**:
  - Añadido el método `menu_partida_activa` para mostrar opciones durante la partida.

### Cambios
- **game/cli.py**:
  - Mejoras en el código.
- **test_cli.py**:
  - Se han añadido pruebas.
- **README.py**:
  - Se han corregido instrucciones.

##  [0.4.4] - 2024-10-12
### Agregando
- **README.py**:
  - Añadiendo presentaciones e instrucciones para iniciar el juego.
- **test_queen.py**:
  - Subiendo más pruebas.
- **game/cli.py**:
  - Funcion `mostrar_opciones_menu` para imprimir las opciones disponibles..
  - Funcion `confirmar_accion` para confirmar acciones del usuario.

### Cambios
- **CHANGELOG.md**:
  - Corrección en el formato del changelog
- **game/chess.py**
  - Moviendo metodo para pedir empate a **chess.py**
  - Reorganización del código.
- **test_chess.py**:
  - Corrección en las pruebas.
- **game/cli.py**:
  - Refactorizacion del codigo.

##  [0.4.3] - 2024-10-11
### Cambios
- **test**:
  - Completando cobertura en board y chess.
- **pawn**:
  - Solucionando problemas de duplicación.

##  [0.4.2] - 2024-10-10
### Cambios
- **game/board.py**:
  - Refactorización de `mover_pieza` y `is_valid_move` en un solo método.
- **pieces**:
  - Refactorización del código para king, pawn, queen y rook.

##  [0.4.1] - 2024-10-08
### Cambios
- **test**:
- Cobertura completa de código para piece, knight y pawn.

##  [0.4.0] - 2024-10-07
### Agregando:
- **test_cli.py**:
  - Se ha añadido metodos de prueba.

### Cambios
- Ajustes en **config.yml**.
- Cambiando logica para solicitar empate de **chess** a **cli**

##  [0.3.9] - 2024-10-06
### Agregando
- **game/chess.py**:
- Importacion de`redis` 
- Metodo para guardar partidas usando redis.

### Cambios
- **game/chess.py**:
  - Modificados `save_game`y `load_game` para usar redis.
- **game/cli.py**:
  - Modificando `iniciar_partida` para que que se pueda reiniciar una partida o volver a la misma.
  - Actualizados `guardar_partida` y `cargar_partida` para funcionar con Redis.
- **test_pawn.py**:
  - Logrando 100% de cobertura de codigo en el test para la pieza pawn.
- **test_chess.py**:
  - Corrección de errores.

##  [0.3.8] - 2024-10-05
### Agregando
- **game/chess.py**:
  - Funcion `rendirse`metodo para que el jugador pueda rendirce si no quiere continuar la partida.
- **game/chess.py**:
  - Funcion `wait_for_menu` si estas en la partida si escribes "menu" puedes volver al inicio.

### Cambios
- **game/cli.py**:
  - Modificacion de la logica en `get_move_input`.
- **test_exceptions.py**:
  - Corrección de errores en las pruebas.
- **test_chess.py**:
  - Corrección de errores en las pruebas.

##  [0.3.7] - 2024-10-04
### Cambios
- Corrección de la visualización de mensajes de error para excepciones en **cli**.
- **game/exceptions**:
  - Refactorizacion del codigo.

##  [0.3.6] - 2024-10-03
### Agregando
- **game/board.py**:
  - Funcion `is_position_valid` para validar si una posición es correcta.
  - Refactorización del código.
- **game/pieces/piece**:
  - Funcion `scan_direction` generalización para explorar en cualquier dirección.

### Cambios
- **game/board.py**:
  - Refactorizacion del codigo.
- **game/cli.py**:
  - Arreglando error en `attempt_move` que no se mostraban el mensaje de las excepciones.
- **pieces**:
  - Refactorizando codigo en **piece** y en todas las piezas.
- **test**:
  - Modificando pruebas en todos los test de las piezas.

##  [0.3.5] - 2024-10-02
### Agregando
- **game/board.py**:
  - Funcion `count_pieces` para contar piezas negras y blancas.
- **game/chess.py**:
  - Reorganizanddo metodos.
  - Funcion `show_piece_count` muestar el conteo de piezas blancas y negras.

## Cambios
- **game/chess.py**:
  - Reorganizanddo metodos.
- **game/board.py**:
  - Eliminando metodo `get_all_pieces` y reorganizando codigo.

## [0.3.4] - 2024-09-30
### Agregando
- **game/board.py**:
  - Funcion `remove_piece` verifica la pieza.
- **game/chess.py**:
  - Funcion `get_turn` para obtener el turno.
  - Funcion `validate_turn` metodo para validar el turno.
- **game/exceptions**:
  - Funcion `ErrorChess` para errores generales del ajedres.
- **test_exceptions.py**: Creado archivo test para realizar pruebas de las excepciones.
  - Se han creado pruebas.

### Cambios
- **game/board.py**:
  - Modificando codigo para simplificar en `get_all_pieces`, `remove_all_pieces`, `is_valid_move` y `mover_pieza`.
-  **pieces**:
  - Modificando y arreglando movimiento para todas las piezas.
-  **tests**:
  - Modificando y agregando test para todas las piezas.

## [0.3.3] - 2024-09-29
### Agregando
- **game/board.py**:
  - Funcion `remove_all_pieces` para eliminar las piezas del tablero. 
- **test_board.py**:
  - Añadiendo mas pruebas.
- **test_chess.py**: Creando archivo test para chess.
  - Añadiendo pruebas.

### Cambios
- **game/board.py**:
  - Arreglando funcion `get_piece`.

## [0.3.2] - 2024-09-28
### Agregando
- **test_board.py**:
  - Añadiendo mas pruebas.
- **game/chess.py**:
  - Funcion `save_game`para guardar la partida con id.
  - Funcion `load_game` para cargar la partida guardada.
  - Importando pickle.
- **game/cli.py**:
  - Funcion `guardar_partida` para introducir en la terminal el nombre de la partida a guardar. 
  - Funcion `cargar_partida` para cargar el nombre de la partida guardada en la terminal y empezar en esa partida.

### Cambios
- **game/board.py**:
  - Modificando la funcion `mover_pieza` para excepciones.
- **game/pieces/bishop.py**:
  - Modificando logica de movimiento en `mov_correcto` para agregar exxcepciones. 

## [0.3.1] - 2024-09-26
### Cambios
- **game/chess.py**:
  - Mejorando el metodo `move`. 
- **game/cli.py**:
  - Modificando y arreglando el metodo `attempt_move`.
- **test_cli.py**:
  - Eliminando codigo para intenatarlo denuevo mas adelante. 

## [0.3.0] - 2024-09-25
### Agregando
- Se ha creado un archivo **game** para reorganizar los archivos de **chess.py**, **cli.py**, **board.py**, **exceptions.py** y el archivo **pieces** con todas las piezas del ajedres.
- **game/board.py**:
  - Funcion `get_all_pieces`
- **game/chess.py**:
  - Funcion `request_draw` metodo para pedir el empate en el juego.

### Cambios
- Reorganizando para todas las importaciones de los archivos con **game** incluidos test.
- **game/cli**:
  - Refactorizacion del codigo.
- **game/chess.py**:
  - Refactorizacion del codigo.

## [0.2.9] - 2024-09-22
### Agregando
- **test_cli.py**: Creando archivo test para la clase cli.
  - Se han añadido pruebas.

### Cambios 
- **cli.py**:
  - Cambiando nombre la funcion `play_game` a `play`.
  - Mejorando funcion `get_move_input` y `attempt_move`.

## [0.2.8] - 2024-09-21
### Agregando
- **pieces/queen.py**
  - Funcion `get_possible_positions`obtiene las posiciones ortogonales posibles para la pieza.

### Cambios
- **chess.py**:
  - Corrigiendo metodo `move`. 
- **cli.py**:
  - Arreglando errores en codigo.
- **piece.py**:
  - Mejorando funcion `possible_diagonal_positions` y `possible_positions_vertical`.
- **pieces/queen.py**:
  - Arreglando funcion `mov_correcto`.
- **test_queen.py**:
  - Corrigiendo pruebas.

## [0.2.7] - 2024-09-18
### Agregando
- **chess.py**:
  - Funcion `parce_position` Convierte una posición en notación ajedrecística.
- **cli.py**:
  - Funcion `__init__` permite incializar.
  - Funcion `mostrar_menu` muestra el menú principal.
  - Funcion `iniciar_partida` inicia una partida de ajedrez.
  - Funcion `mostrar instrucciones` muestra las instruccio nes del juego.
  - Funcion `play_game` maneja las opciones del juego.
  - Funcion `display_board_and_turn` Muestra el tablero y el turno actual.
  - Funcion `get_move_input` obtiene las entradas para mover una pieza.
  - Funcion `attempt_move` se encarga de mover la pieza.
  - Funcion `clear_terminal` que permite limpiar la terminal.
  - Importando `os`
- **main.py**:
  -

## [0.2.6] - 2024-09-17
### Cambios
- **board.py**:
  - Mejorando funcion `mover_pieza` y `is_valid_move`.
- **pieces/pawn.py**:
  - Refactorizando codigo.
- **pieces/piece.py**:
  - Refactorizando codigo.

## [0.2.5] - 2024-09-15
### Agregando
- **pieces/bishop.py**:
  - Agregando funcion `get_possible_positions`
- **pieces/king.py**:
  - Agregando funcion `get_possible_positions` y `is_in_check_after_move`
- **pieces/knight.py**:
  - Agregando funcion `get_possible_positions` y `__is_valid_position`
  
### Cambios
- **pieces/bishop.py**:
  - Corrigiendo errores en `mov_correcto` para los movimientos y agregando excepciones.
- **tests**:
  - Corrigiendo y agregando test en bishop, king y knight.

## [0.2.4] - 2024-09-14
### Agregando
- **exception.py**:
  - Se ha añadido funcion `OutOfBoard` excepcion por si la posicion esta fuera del rango del tablero.
- Implementando metodo para testear la pieza pawn
- **pieces/piece.py**:
  - Se ha añadido funcion `valid_position`, `possible_diagonal_positions`, `possible_orthogonal_positions`, `possible_positions_vd`,`possible_positions_va`

### Cambios
- **pieces/pawn.py**:
  - Mejorando logica en la funcion `is_forward_move` e `is_diagonal_capture`
- **tests**:
  - Se han mejorado y arreglado los test en board, knight y pawn.
  

## [0.2.3] - 2024-09-09
### Agregando
- **test_knight.py**: Se ha creado archivo para testear el caballo.
  - Se han añadido pruebas.
- **test_pawn.py**: Se ha creado archivo para testear al peon. 
  - Se han añadido pruebas. 

## [0.2.2] - 2024-09-08
### Cambios
- **test_queen.py**:
  - Arreglando error en las pruebas. 
  - Se han añadido mas pruebas.

## [0.2.1] - 2024-09-07
### Agregando
- **test_queen.py**: Se ha creado archivo para testear la reina
  - Se han añadido pruebas.

## [0.2.0] - 2024-09-06
### Agregando
- **exceptions.py**:
  - Refactorizando codigo.
  - Se ha añadido funcion `InvalidPieceMove`
- **pawn.py**:
  - Funcion `is_forward_move`
  - Funcion `is_diagonal_capture`

### Cambios
- **exceptions.py**:
  - Refactorizando codigo.
- **pieces/queen.py**:
  - Refactorizando codigo.

## [0.1.9] - 2024-09-05
### Agregando
- **pieces/pawn.py**:
  - Implementando movimientos en la funcion `mov_correcto` para el peon.
- **exceptions.py**:
  - Añadiendo funcion `InvalidMovePawnMove` para movimientos invalidos del peon.
- **README.py**:
  - Subiendo presentacion.

## [0.1.8] - 2024-09-03
### Agregando
- **exceptions.py**:
  - Añadiendo funcion `InvalidMoveKnightMove` para movimientos invalidos del caballo.
- **pieces/knight.py**:
  - Mejorando funcion `mov_correcto` para el movimiento del caballo.

### Cambios
- **queen.py**:
  - Modificando y mejorando movimiento en la pieza queen.

## [0.1.7] - 2024-08-31
### Agregando
- **exceptions.py**:
  - Añadiendo funcion `InvalidMoveQueenMove`.
- **pieces/queen.py**:
  - Implementando funcion `_is_path_clear`, `_check_diagonal_path`, `_check_horizontal_path`, `_check_vertical_path`, `_check_path` para los movimientos validos e invalidos para la reina. 
- **test_queen.py**: Creado archivo para testear la pieza de la reina
  - Se han añadido pruebas. 

## [0.1.6] - 2024-08-30
### Cambios
- Refactorizando codigo en bishop, board y rook

## [0.1.5] - 2024-08-29
### Agregando
- **exceptions**:
  - Añadiendo funcion `InvalidMoveBishopMove` y `InvalidMoveKingMove`
- **test_bishop.py**: Creado archivo para testear la pieza alfil
  - Se han añadido pruebas.
- **test_king.py**:
  - Se han añadido mas pruebas.
- **test_rook.py**:
  - Se han añadido mas pruebas.

### Cambios
- **pieces/bishop.py**:
  - Mejorando funcion `mov_correcto` para el movimiento del alfil.
- **pieces/king.py**:
  - Mejorando funcion `mov_correcto` para el movimiento del rey.

## [0.1.4] - 2024-08-28
### Agregando
- **pieces/rook.py**:
  - Implementado en el metodo `mov_correcto` para que la  pieza rook no pueda moverse en caso de que haya una pieza en su camino.
- **pieces/piece.py**:
  - Añadiendo atributo board en la funcion `__init__`.
- **exceptions**:
  - Añadiendo funcion `InvalidPieceNoMove` y `InvalidMoveRookMove`

### Cambios
- **tests**:
  - Corrigiendo y agregando tests en rook, king y piece. 


## [0.1.3] - 2024-08-24
### Agregando
- **test_king.py**: Archivo para testear los  movimientos del rey
  - Se han añadido pruebas 
- **test_rook.py**:
  - Se han añadido mas pruebas

## [0.1.2] - 2024-08-23
### Agregando
- **test_piece.py**: Archivo para testear y comprobar los metodos en `piece.py`
  - Se han agregado pruebas. 
- **test_rook.py**: Archivo para testear y comprobar los metodos de movimiento de la pieza `rook.py`
  - Se han agregado pruebas.

### Cambios
- **board.py**:
  - Mejorando funcion `mover_pieza`

## [0.1.1] - 2024-08-22
### Agregando
- **exeptions.py**: para definir excepciones
  - Implementando funcion `InvalidMove`
- **chess.py**:
  - Funcion `validate_coords` 
  - Funcion `end_game` 
- **pieces/king,pawn,queen,rook,bishop,knight**:
  - Funcion `mov_correcto` 
   
### Cambios
- **board.py**:
  - Modificando logica en `mover_pieza`
- **test_board.py**:
  - Arreglado un error en el test del tablero

### Eliminando
- **rook**:
  - Funcion `mover_pieza`.

## [0.1.0] - 2024-08-21
### Agregando
- **board.py**:
  - Método `show_board` para mostrar el estado actual del tablero.
  - Implementación del método `__str__` para una mejor visualización del tablero.
  - Metodo `is_valid_move` valida si el movimiento esta dentro del rango del tablero. 
- **chess.py**:
  - Funcion `turn` 
  - Funcion `show_board`
  - Funcion `is_playin` 
- **test_board**:
  - Nuevo metodo de testeo unitario para verificar la implementación de __str__ en `board.py`.
- **pieces/pawn,king,queen,knight,rook,bishop**:
  - funcion `_str_` para representar el simbolo de cada pieza 
- **pieces/piece**:
  - Funcion `get_color`

### Cambios
- **board.py**:
  - Metodo `move-piece` simplificando logica

## [0.0.9] - 2024-08-19
### Agregando
- **board.py**:
  - Metodo `move_piece` para que se pueda mover la pieza 

### Cambios
- **chess.py**:
  - Modificando validacion de movimiento en `move`

## [0.0.8] - 2024-08-17
### Agregando
- Carpeta tests para probar funcionalidad de board.py, pieces y cheess.py

### Cambios
- Modificando correctamente archivo .coveragerc
- En el codigo del archivo main.py, implementacion para iniciar el juego 

## [0.0.7] - 2024-08-16
### Agregando
- Implementando atributos a las piezas de ajedres

## [0.0.6] - 2024-08-15
### Agregando
- **cli.py**: una interfaz de usuario en la línea de comandos para interactuar con el juego de ajedrez.
  - Metodo `play` que gestiona la interacción del usuario para mover piezas en el tablero.
  - Función `main` que inicializa el juego

## [0.0.5] - 2024-08-14
### Agregando
- Carpeta piece, con todas las piezas del ajedres.

### Cambios
- En el archivo **board.py* me falto agregar los peones en el tablero. 

## [0.0.4] - 2024-08-13
### Agregando
- Archivo Dockerfile
- Archivo **chess.py** clase que sirve para gestionar la logica del juego.
- Archivo **board.py** creacion del tablero de ajedres

## [0.0.3] - 2024-08-12
### Agregando
- Archivo **CHANGELOG.md** para registrar cambios.

## [0.0.2] - 2024-08-11
### Agregando
- Archivo codeclimate.yml para la configuración de CodeClimate.

## [0.0.1] - 2024-08-10
### Agregando
- Archivo README con información básica.
- Archivo **main.py** con función suma() para probar la funcionalidad.
- Archivo **test.py** con pruebas unitarias que verifican la correcta implementación de la función suma.
- Archivo .gitignore para excluir archivos innecesarios.
- Archivo .coveragerc
- Archivo **requirements.txt** con las dependencias del proyecto.
- Integracion con CircleCI.
- Archivo .circleci/config.yml para configurar el pipeline de CircleCI
- Archivo **.coveragerc** creado