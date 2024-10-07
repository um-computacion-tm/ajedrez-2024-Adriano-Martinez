# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

##  [0.4.0] - 2024-10-07
### Agregando

### Cambios
- Ajustando codigo en config.yml

##  [0.3.9] - 2024-10-06
### Agregando
- Metodo para guardar partidas en redis

### Cambios
- Logrando 100% de cobertura de codigo en el test para  la pieza pawn 
- Solucionando errores en test_chess.py

##  [0.3.8] - 2024-10-05
### Agregando
- Metodo para rendirce en chess

### Cambios
- Arreglando test de exceptions
- Intentando arreglar test en chess

##  [0.3.7] - 2024-10-04
### Cambios
- Arreglando problema para mostrar mensaje de error en el juego 

##  [0.3.6] - 2024-10-03
### Cambios
- Refactorizando codigo en board, cli y piezas

##  [0.3.5] - 2024-10-02
### Agregando
- Metodo para contar piezas negras y blancas para mayor eficiencia en el codigo

## Cambios
- Eliminando metodo get_all_pieces y reorganizando codigo.

## [0.3.4] - 2024-09-30
### Agregando
- Metodo para remover pieza.
- Implementado metodo para testear las excepciones.
- Metodo para validar turno

## [0.3.3] - 2024-09-29
### Agregando
- Implementado metodo para Testear Chess

## [0.3.2] - 2024-09-28
### Agregando
- Implementado metodo para guardar y cargar partida en chess
- Agregando nuevos metodos para testear el archivo board

## [0.3.1] - 2024-09-26
### Cambios
- Modificacion para el movimiento en el metodo Move de chess

## [0.3.0] - 2024-09-25
### Cambios
- Reorganizando archivos
- Implementado metodo para rendirce en el ajedres

## [0.2.9] - 2024-09-22
### Agregando
- Implementando Tests para cli.py

## [0.2.8] - 2024-09-21
### Cambios
- Arreglando error en cli.py
- Arreglando movimiento en queen.py

## [0.2.7] - 2024-09-18
### Agregando
- Implementando mejoras para cli.py 

## [0.2.6] - 2024-09-17
### Cambios
- Refactorizando codigo en piece y board

## [0.2.5] - 2024-09-15
### Cambios
- Corrigiendo errores de movimientos en la pieza bishop, king y knihgt
- Corriendo test de piezas de bishop, king y knight

## [0.2.4] - 2024-09-14
### Agregando
- Implementando metodo para testear la pieza pawn

## [0.2.3] - 2024-09-9
### Agregando
- Subiendo archivo test_kniht.py e implementando metodos para testear
- subiendo archivo test_pawn.py 

## [0.2.2] - 2024-09-8
### Cambios
- Arreglando error de test en queen.py

## [0.2.1] - 2024-09-7
### Agregando
- Implementando tests para queen.py 

## [0.2.0] - 2024-09-6
### Agregando
- Refactorizando codigo de queen.py y exceptions.py

## [0.1.9] - 2024-09-5
### Agregando
- Implementando movimientos para el peon

## [0.1.8] - 2024-09-3
### Agregando
- Implementando movimientos para el caballo 

### Cambios
- Modificando movimiento en la pieza queen


## [0.1.7] - 2024-08-31
### Agregando
- Implementando movimientos para la reina y agregando movimientos inavalidos en caso de que el movimiento no sea el correcro para esta pieza 
- Agregando archivo test  para la reina

## [0.1.6] - 2024-08-30
### Agregando
- Refactorizando codigo en bishop, board y rook

## [0.1.5] - 2024-08-29
### Agregando
- Implementando movimiento para el rey y el alfil
- Archivo de tests para el alfil

## [0.1.4] - 2024-08-28
### Agregando
- Implementado codigo en rook.py para que la  pieza rook no pueda moverce en caso de que haya una 
pieza en su camino

### Cambios
- Corrigiendo errores en los tests 


## [0.1.3] - 2024-08-24
### Agregando
- Implementado codigo para el test de la pieza rook y la pieza king



## [0.1.2] - 2024-08-23
### Agregando
- Movimiento del rey y la torre
- Test de piece.py y rook.py

## [0.1.1] - 2024-08-22
### Agregando
- Archivo exeptions.py para definir excepciones
- Metodo para mover piezas 
### Cambios
- Arreglado un error en el test del tablero 

## [0.1.0] - 2024-08-21
### Agregando
- Método show_board para mostrar el estado actual del tablero.
- Implementación del método __str__ para una mejor visualización del tablero.
- Nuevo metodo de testeo unitario para verificar la implementación de __str__ en board.py

### Cambios
- Arreglado un error en la validación de movimientos 
- Reformulando codigo en piezas 


## [0.0.9] - 2024-08-19
### Agregando
- Implementando metodos para que el jugador pueda mover su pieza en board.py
- Implementando metodos para validar el movimiento de la pieza en chess.py


## [0.0.8] - 2024-08-17
### Agregando
- Carpeta tests para probar funcionalidad de board.py, pieces y cheess.py

### Cambios
- En archivo .coveragerc
- En el codigo del archivo main.py, implementacion para iniciar el juego 

## [0.0.7] - 2024-08-16
### Agregando
- Implementando atributos a las piezas de ajedres

## [0.0.6] - 2024-08-15
### Agregando
- Archivo cli.py una interfaz de usuario en la línea de comandos para interactuar con el juego de ajedrez.

## [0.0.5] - 2024-08-14
### Agregando
- Carpeta piece, con todas las piezas del ajedres.

### Cambios
- En el archivo board.py me falto agregar a los peones en el tablero. 

## [0.0.4] - 2024-08-13
### Agregando
- Archivo Dockerfile
- Archivo chess.py clase que sirve para gestionar el tablero  
- Archivo board.py creacion del tablero de ajedres

## [0.0.3] - 2024-08-12
### Agregando
- Archivo CHANGELOG.md para registrar cambios.

## [0.0.2] - 2024-08-11
### Agregando
- Archivo codeclimate.yml para la configuración de CodeClimate.

## [0.0.1] - 2024-08-10
### Agregando
- Archivo README con información básica.
- Archivo main.py con función suma() para probar la funcionalidad.
- Archivo test.py con pruebas unitarias que verifican la correcta implementación de la función suma.
- Archivo .gitignore para excluir archivos innecesarios.
- Archivo .coveragerc
- Archivo requirements.txt con las dependencias del proyecto.
- Integracion con CircleCI.
- Archivo .circleci/config.yml para configurar el pipeline de CircleCI
- Archivo .coveragerc creado