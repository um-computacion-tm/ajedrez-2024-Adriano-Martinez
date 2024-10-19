# JUEGO DEL AJEDREZ
Proyecto creado por Adriano Salvador Martinez Barbuzza

# Como Instalar el Juego

El juego se ejecuta utilizando Docker. Sigue los siguientes pasos para instalar y correr el juego:

1. **Instalar Docker**  
   Si no tienes Docker instalado, ejecuta el siguiente comando:
```bash
    $ sudo apt install docker
```
2. **Crear la imagen de Docker del juego**  
   Para construir la imagen Docker del juego, ejecuta:
```bash
    $ sudo docker build -t ajedrez-2024-adriano-martinez . --no-cache
```
3. **Ejecutar los tests e iniciar el juego**  
   Una vez creada la imagen, puedes ejecutar el siguiente comando para correr los tests e iniciar el juego:
```bash
    $ sudo docker run -i ajedrez-2024-adriano-martinez
```

## Reglas del Juego
El juego sigue las reglas básicas del ajedrez con algunas modificaciones:
- `Reglas originales del ajedrez`: Consultarlas [aquí](https://es.wikipedia.org/wiki/Leyes_del_ajedrez)
- `Reglas de este juego`: En este ajedrez se respetan los movimientos de las piezas como en el ajedrez tradicional. Sin embargo, no se implementan reglas como jaque, jaque mate, ni movimientos especiales.
## Cómo Jugar
- El juego sigue las reglas del ajedrez tradicional y se desarrolla por turnos alternos entre los jugadores.A continuacion, se detalla la interacción en las dos fases principales: el **menú principal** y el menu de la **fase de juego**:
## Menú Principal
- Al iniciar el juego, los jugadores verán las siguientes opciones:
- `Iniciar Partida`: Comienza una nueva partida de ajedrez.
- `Ver Instrucciones`: Muestra las reglas básicas del juego.
- `Salir del Juego`: Cierra el juego.
## Fase de Juego
- Una vez que la partida comienza, los jugadores alternan turnos y tienen las siguientes opciones disponibles:
- `Mover una pieza`: Mueve una pieza en el tablero. Debes ingresar la posición inicial y final de la pieza usando notación algebraica (Ej: a2 a a4).
  - Si el movimiento es válido, se actualizará el tablero.
  - Si el movimiento no es válido, se te pedirá ingresar nuevamente una posición válida.
- `Solicitar empate` (Pedir Tablas): Puedes ofrecer un empate al oponente escribiendo `draw` en la terminal. Si ambos jugadores aceptan, el juego termina en tablas. Si el oponente rechaza, la partida continúa.
- `Rendirse`: Puedes rendirte escribiendo `3` en la terminal, lo que otorga la victoria a tu oponente.
- `Volver al menu principal`: Puedes escribir `4` en la terminal en cualquier momento para volver al menú principal sin terminar la partida.
- Si selecionaste una opcion que no querias puedes cancelarla escribiendo `back` en la terminal.
## Cómo Ganar
Para ganar, debes capturar todas las piezas del oponente. Es decir, que el primero que se quede sin piezas, pierde.

## Integraciones 

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Adriano-Martinez/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Adriano-Martinez/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/9c10ec6adcf817de38ab/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Adriano-Martinez/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/9c10ec6adcf817de38ab/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Adriano-Martinez/test_coverage)