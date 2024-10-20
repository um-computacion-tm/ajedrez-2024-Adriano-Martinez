import unittest
from game.board import Board
from game.pieces.queen import Queen
from game.exceptions import InvalidPieceMove

class TestQueen(unittest.TestCase):
    """
    Clase de prueba para la clase Queen (reina). Utiliza la biblioteca unittest 
    para verificar el comportamiento y la funcionalidad de las reinas en el juego.
    """

    def setUp(self):
        """
        Método que se ejecuta antes de cada prueba. Inicializa un nuevo tablero 
        y coloca una reina blanca en la posición d5 (3, 3).
        """
        self.__board__ = Board()  # Inicializa un nuevo tablero
        self.__queen_white__ = Queen("WHITE", self.__board__)  # Crea una reina blanca
        self.__board__.set_piece(3, 3, self.__queen_white__)  # Coloca la reina 

    def test_valid_vertical_move(self):
        """
        Prueba que la reina puede realizar un movimiento vertical permitido 
        """
        # Verifica que el camino esté despejado para un movimiento vertical
        for row in range(4, 8):  
            self.__board__.set_piece(row, 3, None)
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 7, 3)) 

    def test_valid_horizontal_move(self):
        """
        Prueba que la reina puede realizar un movimiento horizontal permitido 
        """
        # Verifica que el camino esté despejado para un movimiento horizontal
        for col in range(4, 8):  
            self.__board__.set_piece(3, col, None)
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 3, 7)) 

    def test_valid_diagonal_move(self):
        """
        Prueba que la reina puede realizar un movimiento diagonal permitido 
        """
        # Verifica que el camino esté despejado para un movimiento diagonal
        for i in range(1, 4):  # Despeja las posiciones diagonales 
            self.__board__.set_piece(3 + i, 3 + i, None)
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 6, 6))  

    def test_capture_move(self):
        """
        Prueba que la reina puede capturar una pieza enemiga al moverse a su 
        posición. 
        """
        # Coloca una pieza enemiga 
        enemy_piece = Queen("BLACK", self.__board__)
        self.__board__.set_piece(7, 3, enemy_piece)

        # Limpia cualquier otra pieza en el camino
        for row in range(4, 7):
            self.__board__.set_piece(row, 3, None)

        # Verifica que la reina blanca puede capturar la pieza enemiga
        self.assertTrue(self.__queen_white__.mov_correcto(3, 3, 7, 3))  

    def test_no_capture_own_piece(self):
        """
        Prueba que la reina no puede capturar una pieza amiga al intentar 
        moverse a su posición. 
        """
        # Coloca una pieza amiga (reina blanca) 
        friendly_piece = Queen("WHITE", self.__board__)
        self.__board__.set_piece(7, 3, friendly_piece)

        # La reina blanca no debería poder moverse a la posición de su propia pieza
        with self.assertRaises(InvalidPieceMove):
            self.__queen_white__.mov_correcto(3, 3, 7, 3)  # no debería permitir mover

    def test_out_of_bounds_move(self):
        """
        Prueba que se lanza un InvalidPieceMove si la reina intenta 
        moverse fuera de los límites del tablero.
        """
        # La Reina intenta moverse fuera de los límites del tablero
        with self.assertRaises(InvalidPieceMove):
            self.__queen_white__.mov_correcto(3, 3, 8, 3)  # Movimiento fuera del tablero 

    def test_blocked_move(self):
        """
        Prueba que la reina no puede moverse a una posición bloqueada 
        por otra pieza. 
        """
        # Coloca una pieza en el camino de la Reina 
        blocking_piece = Queen("BLACK", self.__board__)
        self.__board__.set_piece(4, 3, blocking_piece)

        # La Reina no debería poder moverse porque está bloqueada 
        with self.assertRaises(InvalidPieceMove):
            self.__queen_white__.mov_correcto(3, 3, 5, 3)  

if __name__ == "__main__":
    unittest.main()
